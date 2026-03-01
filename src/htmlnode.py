from textnode import TextNode, TextType

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplemented('to_html method is not implemented yet you can find this error raise in the HTMLNode class')

    def props_to_html(self):
        result = ''
        if self.props:
            for key in self.props:
                result += f' {key}="{self.props[key]}"'
            
        return result
    
    def __eq__(self, other):
        if self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props:
            return True
        return False

    def __repr__(self):
        return f'HTMLNode: tag={self.tag}, value={self.value}, children={self.children}, props={self.props}'
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Improper LeafNode: no value")
        if self.tag is None:
            return self.value
        if self.tag == 'p':
            return f'<p>{self.value}</p>'
        if self.tag == 'a':
            key = next(iter(self.props), None)
            return f'<a {key}="{self.props.get(key)}">{self.value}</a>'
        if self.tag == 'b':
            return f'<b>{self.value}</b>'
        if self.tag == 'code':
            return f'<code>{self.value}</code>'
        if self.tag == 'i':
            return f'<i>{self.value}</i>'
        if self.tag == 'div':
            return f'<div>{self.value}</div>'
        if self.tag == 'span':
            return f'<span>{self.value}</span>'
        
    def __repr__(self):
        return f'LeafNode: tag={self.tag}, value={self.value}, props={self.props}'
    
    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.props == other.props

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Improper ParentNode: no tag")
        if self.children is None:
            raise ValueError("Improper ParentNode: no children")
        
        result = f'<{self.tag}>'

        for child in self.children:
            result += f'{child.to_html()}'
        
        result += f"</{self.tag}>"
            
        return result
    
def text_node_to_html_node(text_node):
    if not isinstance(text_node.text_type, TextType):
        raise ValueError(f"invalid text type: {text_node.text_type}")
    
    type = text_node.text_type

    if type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if type == TextType.BOLD:
        return LeafNode('b', text_node.text)
    if type == TextType.ITALIC:
        return LeafNode('i', text_node.text)
    if type == TextType.CODE:
        return LeafNode('code', text_node.text)
    if type == TextType.LINK:
        return LeafNode('a', text_node.text, {'href': text_node.url})
    if type == TextType.IMAGE:
        return LeafNode('img', '', {'src': text_node.url, 'alt': text_node.text})
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
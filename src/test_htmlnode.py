import unittest
from htmlnode import HTMLNode, text_node_to_html_node
from textnode import TextNode, TextType

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode('a', 'this is the value', [HTMLNode(), HTMLNode()], {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode('a', 'this is the value', [HTMLNode(), HTMLNode()], {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = HTMLNode('p', 'this is the value', [HTMLNode(), HTMLNode()], {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode('a', 'this is the value', [HTMLNode(), HTMLNode()], {"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node, node2)

    def test_eq3(self):
        node = HTMLNode('p', 'this is the other value', [HTMLNode(), HTMLNode()], {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode('p', 'this is the value', [HTMLNode(), HTMLNode()], {"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node, node2)

    def test_eq4(self):
        node = HTMLNode('p', 'this is the other value', [HTMLNode()], {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode('p', 'this is the value', [HTMLNode(), HTMLNode()], {"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node, node2)

    def test_eq5(self):
        node = HTMLNode('p', 'this is the other value', [HTMLNode(), HTMLNode()], {"href": "https://www.google.com"})
        node2 = HTMLNode('p', 'this is the value', [HTMLNode(), HTMLNode()], {"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node, node2)

    def test_eq6(self):
        node = HTMLNode('p', 'this is the other value', [HTMLNode(), HTMLNode()], {"href": "https://www.google.com", "target": "_blank"})
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://www.google.com" target="_blank"')

    def test_eq7(self):
        node = HTMLNode('p', 'this is the other value', [HTMLNode(), HTMLNode()], {"href": "https://www.google.com", "target": "_blank"})
        result = repr(node)
        self.assertEqual(result, "HTMLNode: tag=p, value=this is the other value, children=[HTMLNode: tag=None, value=None, children=None, props=None, HTMLNode: tag=None, value=None, children=None, props=None], props={'href': 'https://www.google.com', 'target': '_blank'}")

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "This is a text node")

    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, "This is a text node")

    def test_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("This is a text node", TextType.LINK, "www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, {'href': 'www.google.com'})

    def test_image(self):
        node = TextNode("This is a cat image", TextType.IMAGE, "https://example.com/images/cat.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, '')
        self.assertEqual(html_node.props, {'src': "https://example.com/images/cat.jpg", 'alt': "This is a cat image"})


if __name__ == "__main__":
    unittest.main()
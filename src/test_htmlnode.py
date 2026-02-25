import unittest
from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()
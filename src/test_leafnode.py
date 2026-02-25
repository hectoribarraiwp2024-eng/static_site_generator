import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode('p', 'this is the value', {"href": "https://www.google.com"})
        node2 = LeafNode('p', 'this is the value', {"href": "https://www.google.com"})
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = LeafNode('p', 'this is the value', {"href": "https://www.google.gov"})
        node2 = LeafNode('p', 'this is the value', {"href": "https://www.google.com"})
        self.assertNotEqual(node, node2)

    def test_eq4(self):
        node = LeafNode('p', 'this is the wrong value', {"href": "https://www.google.com"})
        node2 = LeafNode('p', 'this is the value', {"href": "https://www.google.com"})
        self.assertNotEqual(node, node2)

    def test_eq5(self):
        node = LeafNode('a', 'this is the value', {"href": "https://www.google.com"})
        node2 = LeafNode('p', 'this is the value', {"href": "https://www.google.com"})
        self.assertNotEqual(node, node2)

    def test_LeafNode_to_html(self):
        result = LeafNode("p", "This is a paragraph of text.").to_html()
        self.assertEqual(result, "<p>This is a paragraph of text.</p>")

    def test_LeafNode_to_html2(self):
        result = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        self.assertEqual(result, '<a href="https://www.google.com">Click me!</a>')

    def test_LeafNode_to_repr(self):
        result = LeafNode('p', 'I AM SCREAMING')
        self.assertEqual(repr(result), 'LeafNode: tag=p, value=I AM SCREAMING, props=None')

if __name__ == "__main__":
    unittest.main()
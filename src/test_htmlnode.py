import unittest
from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(None, None, None, {
            "href": "https://www.google.com",
            "target": "_blank",
        })
        string = ' href="https://www.google.com" target="_blank"'
        line = node.props_to_html()

        self.assertEqual(line, string)

    def test_repr(self):
        node = HTMLNode("p", "hello", None, None)
        string = "HtmlNode(tag=p, value=hello, children=None, props=None)"
        line = node.__repr__()
        
        self.assertEqual(line, string)

    def test_eq(self):
        node = HTMLNode("a", "hello", None, {
            "href": "https://www.google.com",
            "target": "_blank",
        })
        node2 = HTMLNode("a", "hello", None, {
            "href": "https://www.google.com",
            "target": "_blank",
        })

        self.assertEqual(node, node2)
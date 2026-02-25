import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("something something", TextType.BOLD, 'link')
        node2 = TextNode('something different', TextType.CODE, 'image')
        self.assertNotEqual(node, node2)

    def test_eq3(self):
        node = TextNode("boring", TextType.ITALIC, 'image')
        node2 = TextNode("boring", TextType.LINK, 'link')
        self.assertNotEqual(node, node2)

    def test_eq4(self):
        node = TextNode("ew", TextType.CODE, 'blah')
        node2 = TextNode("ew", TextType.CODE, 'blah blah')
        self.assertNotEqual(node, node2)
    
    def test_eq5(self):
        node = TextNode("hard", TextType.BOLD, None)
        node2 = TextNode("hard", TextType.BOLD)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
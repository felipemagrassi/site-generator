import unittest

from textnode import (TextNode, TextType)

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode('this is a text node', TextType.BOLD)
        node2 = TextNode('this is a text node', TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_eq_url(self):
        node = TextNode('this is a text node', TextType.BOLD, 'www.google.com')
        node2 = TextNode('this is a text node', TextType.BOLD, 'www.google.com')
        self.assertEqual(node, node2)

    def test_eq_different_text(self):
        node = TextNode('this is a text node', TextType.BOLD)
        node2 = TextNode('this is not a text node', TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_different_text_type(self):
        node = TextNode('this is a text node', TextType.BOLD)
        node2 = TextNode('this is a text node', TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_different_url(self):
        node = TextNode('this is a text node', TextType.BOLD, "www.google.com")
        node2 = TextNode('this is a text node', TextType.BOLD, "www.google.com.br")
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode('this is a text node', TextType.BOLD, "www.google.com")
        self.assertEqual(node.url, "www.google.com")

    def test_repr(self):
        node = TextNode('this is a text node', TextType.BOLD)
        self.assertEqual(repr(node), "TextNode(this is a text node, bold, None)")

        
if __name__ == "__main__":
    unittest.main()



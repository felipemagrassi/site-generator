import unittest

from htmlnode import LeafNode
from textnode import (TextNode, TextType, text_note_to_html_node)

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

    def test_can_access(self):
        node = TextNode('this is a text node', TextType.BOLD, "www.google.com")
        self.assertEqual(node.text, 'this is a text node')
        self.assertEqual(node.text_type, TextType.BOLD)
        self.assertEqual(node.url, 'www.google.com')

    def test_url(self):
        node = TextNode('this is a text node', TextType.BOLD, "www.google.com")
        self.assertEqual(node.url, "www.google.com")

    def test_repr(self):
        node = TextNode('this is a text node', TextType.BOLD)
        self.assertEqual(repr(node), "TextNode(this is a text node, bold, None)")

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            text_note_to_html_node(node),
            LeafNode(None, node.text, None)
        )
    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertEqual(
            text_note_to_html_node(node),
            LeafNode("b", node.text, None)
        )
    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(
            text_note_to_html_node(node),
            LeafNode("i", node.text, None)
        )
    def test_code(self):
        node = TextNode("This is a text node", TextType.CODE, "https://www.boot.dev")
        self.assertEqual(
            text_note_to_html_node(node),
            LeafNode("code", node.text, None)
        )
    def test_link(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(
            text_note_to_html_node(node),
                LeafNode("a", node.text, {"href": node.url})
        )
    def test_image(self):
        node = TextNode("This is a text node", TextType.IMAGE, "https://www.boot.dev")
        self.assertEqual(
            text_note_to_html_node(node),
            LeafNode("img", "", {"src": node.url, "alt": node.text})
        )

    def test_invalid_type(self):
        with self.assertRaises(ValueError):
            text_note_to_html_node(TextNode("hello", "world"))

if __name__ == "__main__":
    unittest.main()



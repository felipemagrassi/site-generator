import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_can_create_leaf_node(self):
        node = LeafNode("p", "hello world")
        self.assertEqual(node.tag, "p") 

    def test_can_generate_html(self):
        node = LeafNode("p", "hello world")
        self.assertEqual(node.to_html(), "<p>hello world</p>")

    def test_can_generate_html_with_props(self):
        node = LeafNode("a", "hello world", {"href": "www.google.com"})
        self.assertEqual(node.to_html(), "<a href='www.google.com'>hello world</a>")

    def test_can_generate_html_without_tag(self):
        node = LeafNode(None, "hello world")
        self.assertEqual(node.to_html(), "hello world")

    def test_cannot_generate_html_without_value(self):
        with self.assertRaises(ValueError):
            LeafNode('p').to_html()

if __name__ == "__main__":
    unittest.main()

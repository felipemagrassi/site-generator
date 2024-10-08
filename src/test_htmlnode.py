import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html_without_props(self):
        html_node = HTMLNode()
        self.assertEqual(html_node.props_to_html(), "")

    def test_props_to_html_with_empty_props(self):
        html_node = HTMLNode(None, None, None, {})
        self.assertEqual(html_node.props_to_html(), "")

    def test_props_to_html_with_props(self):
        html_node = HTMLNode("a", "www.google.com", [HTMLNode()], {"href": "https://www.google.com", "target": "_blank"} )
        self.assertEqual(html_node.props_to_html(), " href='https://www.google.com' target='_blank'")

    def test_acessors(self):
        html_node = HTMLNode("a", "www.google.com", None, {"href": "https://www.google.com", "target": "_blank"} )

        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, 'www.google.com')
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, {"href": "https://www.google.com", "target": "_blank"})


    def test_repr(self):
        html_node = HTMLNode("a", "www.google.com", [HTMLNode()], {"href": "https://www.google.com", "target": "_blank"} )
        self.assertEqual(repr(html_node), "HTMLNode(a, www.google.com, [HTMLNode(None, None, None, None)], {'href': 'https://www.google.com', 'target': '_blank'})" )

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
            LeafNode(None).to_html()

class TestParentNode(unittest.TestCase):
    def test_can_generate_html_for_parent_node(self):
        node = ParentNode("p",[
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None,"Normal text")
        ])

        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_can_generate_html_for_parent_node_nested(self):

        node = ParentNode("p",[
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None,"Normal text")
        ])

        parent_node = ParentNode("div",[
            node
        ])

        self.assertEqual(parent_node.to_html(), "<div><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></div>")


    def test_cannot_generate_html_for_parent_node_without_children(self):
        with self.assertRaises(ValueError):
            ParentNode('p',None).to_html()
    def test_cannot_generate_html_for_parent_node_without_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("bold")]).to_html()


if __name__ == "__main__":
    unittest.main()

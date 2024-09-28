import unittest
from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html_without_props(self):
        html_node = HTMLNode()
        self.assertEqual(html_node.props_to_html(), "")

    def test_props_to_html_with_props(self):
        html_node = HTMLNode("a", "www.google.com", [HTMLNode()], {"href": "https://www.google.com", "target": "_blank"} )
        self.assertEqual(html_node.props_to_html(), "href=https://www.google.com target=_blank")

    def test_acessors(self):
        html_node = HTMLNode("a", "www.google.com", None, {"href": "https://www.google.com", "target": "_blank"} )

        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, 'www.google.com')
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, {"href": "https://www.google.com", "target": "_blank"})


    def test_repr(self):
        html_node = HTMLNode("a", "www.google.com", [HTMLNode()], {"href": "https://www.google.com", "target": "_blank"} )
        self.assertEqual(repr(html_node), "HTMLNode(a, www.google.com, [HTMLNode(None, None, None, None)], {'href': 'https://www.google.com', 'target': '_blank'})" )

if __name__ == "__main__":
    unittest.main()

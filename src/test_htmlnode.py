import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        # Test when props is None
        node = HTMLNode("div", "content")
        self.assertEqual(node.props_to_html(), "")
        
    def test_props_to_html_single_prop(self):
        # Test with a single property
        node = HTMLNode("div", "content", props={"class": "text"})
        self.assertEqual(node.props_to_html(), ' class="text"')
        
    def test_props_to_html_multiple_props(self):
        # Test with multiple properties
        node = HTMLNode("a", "link", props={"href": "https://example.com", "target": "_blank"})
        result = node.props_to_html()
        # Since dictionary order isn't guaranteed, check both possible combinations
        self.assertTrue(
            result == ' href="https://example.com" target="_blank"' or 
            result == ' target="_blank" href="https://example.com"'
        )

if __name__ == "__main__":
    unittest.main()
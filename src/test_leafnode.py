import unittest

from htmlnode import HTMLNode, LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_no_tag(self):
        # Test when tag is None
        node = LeafNode(tag=None, value="Just text")
        self.assertEqual(node.to_html(), "Just text")
        
    def test_to_html_with_tag(self):
        # Test with a tag and no properties
        node = LeafNode("p", "This is a paragraph.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph.</p>")
        
    def test_to_html_with_props(self):
        # Test with a tag and properties
        node = LeafNode("a", "Click here", props={"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com">Click here</a>')

if __name__ == "__main__":
    unittest.main()
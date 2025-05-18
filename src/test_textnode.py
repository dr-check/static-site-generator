import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        # Test basic equality
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_none_url(self):
        # Test equality with None URL
        node3 = TextNode("This is a different text node", TextType.IMAGE, url=None)
        node4 = TextNode("This is a different text node", TextType.IMAGE, url=None)
        self.assertEqual(node3, node4)
        
    
    def test_eq_different_text_type(self):
        # Test equality with different text types
        node5 = TextNode("This is a different text node", TextType.ITALIC, url="http://example.com")
        node6 = TextNode("This is a different text node", TextType.ITALIC, url="http://example.com")
        self.assertEqual(node5, node6)
        
    def test_neq_different_text(self):
        # Test inequality with different text
        node7 = TextNode("This is a different text node", TextType.TEXT, url="http://example.com")
        node8 = TextNode("This is a different text node", TextType.BOLD, url="http://example.com")
        self.assertNotEqual(node7, node8)


if __name__ == "__main__":
    unittest.main()
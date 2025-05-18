import unittest

from htmlnode import HTMLNode, ParentNode, LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_no_tag(self):
        # Test when tag is None
        node = ParentNode(tag=None, children=[])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_no_children(self):
        # Test when children is None
        node = ParentNode(tag="div", children=None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_empty_children(self):
        # Test with empty children list
        node = ParentNode("div", [])
        self.assertEqual(node.to_html(), "<div></div>")

    def test_to_html_with_tag(self):
        # Test with a tag and no properties
        node = ParentNode("p", [])
        self.assertEqual(node.to_html(), "<p></p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),"<div><span><b>grandchild</b></span></div>")

if __name__ == "__main__":
    unittest.main()
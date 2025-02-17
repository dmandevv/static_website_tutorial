import unittest
from functions import *
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        print("\nTESTING TEXTCODE\n")
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.IMAGE)
        self.assertNotEqual(node, node2)

        node = TextNode("This is a text node", TextType.CODE, None)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertEqual(node, node2)

        normalleafnode = text_node_to_html_node(TextNode("normal textnode to leafnode", TextType.TEXT, "www.test.com"))
        boldleafnode = text_node_to_html_node(TextNode("bold textnode to leafnode", TextType.BOLD, "www.test.com"))
        italicleafnode = text_node_to_html_node(TextNode("italic textnode to leafnode", TextType.ITALIC, "www.test.com"))
        codeleafnode = text_node_to_html_node(TextNode("code textnode to leafnode", TextType.CODE, "www.test.com"))
        linkleafnode = text_node_to_html_node(TextNode("link textnode to leafnode", TextType.LINK, "www.test.com"))
        imageleafnode = text_node_to_html_node(TextNode("image textnode to leafnode", TextType.IMAGE, "www.test.com"))

        print(normalleafnode.to_html())
        print(boldleafnode.to_html())
        print(italicleafnode.to_html())
        print(codeleafnode.to_html())
        print(linkleafnode.to_html())
        print(imageleafnode.to_html())

        self.assertRaises(TypeError, text_node_to_html_node, TextNode("wrong text type", None))

if __name__ == "__main__":
    unittest.main()
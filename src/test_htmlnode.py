import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test(self):
        print("\nTESTING HTMLCODE\n")
        node1 = HTMLNode("p", "body text", None, {"href":"https://www.test.com", "hidden":""})
        print("Node1 HTML: " + node1.props_to_html())
        print("Node1 __repr__: "  + node1.__repr__())

        leafnode1 = LeafNode("p", "This is a paragraph of text.")
        print("Leafnode1 HTML: " + leafnode1.to_html())

        leafnode2 = LeafNode("a", "Click me!", {"href": "https://www.test.com"})
        print("Leafnode2 HTML: " + leafnode2.to_html())
    
        parentnode1 = ParentNode("p", [leafnode1, leafnode2])
        print(parentnode1.to_html())

        parentnode2 = ParentNode("p", [parentnode1])
        print(parentnode2.to_html())

        parentnode3 = ParentNode("p", [])
        print(parentnode3.to_html())

        parentnode4 = ParentNode("p", [parentnode2])
        print(parentnode4.to_html())


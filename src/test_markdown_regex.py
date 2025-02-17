import unittest
from functions import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    compare_node_lists,
    split_nodes_link,
    text_to_textnodes,
    markdown_to_blocks,
)

from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
    def test_regex(self):
        print("\nTESTING MARKDOWN REGEX\n")

        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expecting = '[("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]'
        results = extract_markdown_images(text)
        print("Expecting: " + expecting)
        print("Results: " + str(results))


        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expecting = '[("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]'
        results = extract_markdown_links(text)
        print("Expecting: " + expecting)
        print("Results: " + str(results))

        print("\nTESTING IMAGE SPLITTING\n")

        node = TextNode(
            "This is text with an image ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            TextType.TEXT
        )
        results = split_nodes_image([node])
        expecting = [
            TextNode("This is text with an image ", TextType.TEXT),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
            ),
        ]
        compare_node_lists(self, expecting, results)

        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        results = split_nodes_link([node])
        expecting = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        compare_node_lists(self, expecting, results)

        print("\nTESTING TEXT TO TEXTNODE\n")

        raw_markdown_text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        results = text_to_textnodes(raw_markdown_text)
        expecting = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]  
        compare_node_lists(self, results, expecting)

        print("\nTESTING MARKDOWN TO BLOCKS\n")
        raw_markdown_text = """
        # This is a heading    

           This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item      
        *    This is another list item"""
        print("Raw Markdown: " + raw_markdown_text)
        blocked_markdown = markdown_to_blocks(raw_markdown_text)
        for block in blocked_markdown:
            print(f"Block {blocked_markdown.index(block)}:" + block)



if __name__ == "__main__":
    unittest.main()
import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("tag", "value", "children", {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("tag", "value", "children", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node, node2)

    def test_NOTprops_to_html(self):
        node = HTMLNode("tag", "value", "children", {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("bag", "zalue", "cildren", {"a": "https://www.google.com", "p": "_blank"})
        self.assertNotEqual(node.props_to_html(), node2.props_to_html())
    
    def test_props_to_html(self):
        node = HTMLNode("tag", "value", "children", {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("tag", "value", "children", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())
    
    def test_eq(self):
        node = HTMLNode("tag", "value", "children", {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("tag", "value", "children", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node, node2)

    def test_NOTeq(self):
        node = HTMLNode("tag", "value", "children", {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("not", "equal", "value", {"nothref": "https://www.notgoogle.com", "nottarget": "_blank"})
        self.assertNotEqual(node, node2)


test_node_1 = HTMLNode("tag", "value", "children", {"href": "https://www.google.com", "target": "_blank"})
test_node_2 = HTMLNode("tag", "value", "children", {"href": "https://www.google.com", "target": "_blank", "a":"value1", "b":"value2"})
test_node_3 = HTMLNode("tag", "value", "children", {"href": "https://www.google.com", "target": "_blank", "a":"value1", "b":"value2", "color": {"blue":90, "red":120, "green":75} })
test1 = LeafNode("p", "This is a paragraph of text.")
test2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
test3 = LeafNode("a", "Click me!", {"href": "https://www.google.com", "two": "https://www.google.com", "three": "https://www.google.com"})
test4 = LeafNode(None, "Click me!", {"href": "https://www.google.com", "two": "https://www.google.com", "three": "https://www.google.com"})
parent_node_1 = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
parent_node_2 = nested_node = ParentNode(
    "div",
    [
        ParentNode("p", [LeafNode(None, "Nested paragraph")]),
        LeafNode("b", "Bold text")
    ],
)
parent_node_3 = ParentNode(
    "ul",
    [
        LeafNode("li", "Item 1"),
        LeafNode("li", "Item 2"),
        LeafNode("li", "Item 3")
    ]
)
parent_node_4 = ParentNode(
    "div",
    [
        ParentNode(
            "p",
            [
                LeafNode(None, "Nested paragraph inside a div")
            ]
        ),
        LeafNode("b", "Bold text inside div")
    ]
)
parent_node_5 = ParentNode(
    "section",
    [
        ParentNode(
            "article",
            [
                ParentNode(
                    "header",
                    [
                        LeafNode("h1", "Article Title"),
                        LeafNode("p", "Subtitle")
                    ]
                ),
                LeafNode("p", "Article content")
            ]
        )
    ]
)
parent_node_6 = ParentNode(
    "ul",
    [
        LeafNode("li", "Item 1"),
        LeafNode("li", "Another item"),
        LeafNode("li", "Last item")
    ],
    props={"class": "list"}
)



#testx = LeafNode("a test of value error")



print("---------------------------")
print("---- Test HTML  Prints ----")
print(test_node_1.props_to_html())
print(test_node_2.props_to_html())
print(test_node_3.props_to_html())
print(f"tag = {test_node_1.tag}, value = {test_node_1.value}, props = {test_node_1.props}")
print("---------------------------")
print("-- Test TO___HTML Prints --")
print(test1.to_html())
print(test2.to_html())
print(test3.to_html())
print(test4.to_html())
print("---------------------------")
print("-ParentNode TO_HTML Prints-")
print("input:    " + parent_node_1.to_html())
print("Expected: <p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
print("input:    " + parent_node_2.to_html())
print("Expected: <div><p>Nested paragraph</p><b>Bold text</b></div>")
print("input:    " + parent_node_3.to_html())
print("Expected: <ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>")
print("input:    " + parent_node_4.to_html())
print("Expected: <div><p>Nested paragraph inside a div</p><b>Bold text inside div</b></div>")
print("input:    " + parent_node_5.to_html())
print("Expected: <section><article><header><h1>Article Title</h1><p>Subtitle</p></header><p>Article content</p></article></section>")
print("input:    " + parent_node_6.to_html())
print("Expected: <ul class='list'><li>Item 1</li><li>Another item</li><li>Last item</li></ul>")

#print(testx.to_html())



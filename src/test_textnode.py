import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_eq_false(self):
        node = TextNode("This is a word node", "text")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)
    
    def test_eq_2(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_eq_false_url(self):
        node = TextNode("This is a word node", "text", "www.gooba.com")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a word node", "text", "www.gooba.com")
        self.assertEqual("TextNode(This is a word node, text, www.gooba.com)", repr(node))


test_node_1 = TextNode("This is a word node", "text", "www.gooba.com")
test_node_2 = TextNode("this could be any string you know", "italic")
test_node_3 = TextNode("I am worried about my code", "bold", "wwww.davidspadefanboi.com")


print("--------------------------")
print("---- Test Text Prints ----")
print(test_node_1.__repr__())
print(test_node_2.__repr__())
print(test_node_3.__repr__())
print("--------------------------")



if __name__ == "__main__":
    unittest.main()
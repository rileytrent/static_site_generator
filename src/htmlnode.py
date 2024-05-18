class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __eq__(self, other):
        if self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props:
            return True
        else:
            return False
        
    def to_html(self):
        raise NotImplementedError ("to_html method not implemented")
    
    def props_to_html(self):
        hold = []
        if self.props == None:
            return ""
        else:
            for keys, values in self.props.items():
                 hold.append(f' {keys}="{values}"')
        return "".join(hold)

    def __repr__(self):
        return (f"{self.__class__.__name__}({self.tag}, {self.value}, {self.children}, {self.props})")




class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
        super().__init__(tag, value)
        self.props = props
        if value == None:
           raise ValueError("value required")
        
    def to_html(self):
        if self.tag == None:
            return (f"{self.value}")
        elif self.props == None:
            return (f"<{self.tag}>{self.value}</{self.tag}>")
        elif self.props != None:
            return (f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>")
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag)
        self.children = children
        self.props = props
        if self.tag == None or self.tag == "":
            raise ValueError("Tag Required")
        if self.children == None or self.children == []:
            raise ValueError("Children Required")
    
    def to_html(self):
        hold = []
        for node in self.children:
            hold.append(node.to_html())
        nodes = "".join(hold)
        return (f"<{self.tag}{self.props_to_html()}>{nodes}</{self.tag}>")
            
        

            




        


    







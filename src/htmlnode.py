

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise Exception(NotImplementedError)
    
    def props_to_html(self):
        props = ""
        if self.props == None:
            return props
        for key in self.props.keys():
            props += f' {key}="{self.props[key]}"'
        return props
    
    def __repr__(self):
        return f"{type(self).__name__}({self.tag}, {self.value}, {self.children},{self.props_to_html()})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise Exception(ValueError("No Tag"))
        if self.children == None:
            raise Exception(ValueError("No Children"))
        html = ""
        for child in self.children:
            html += child.to_html()
        return f"<{self.tag}>{html}</{self.tag}>"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise Exception(ValueError("No value set!"))
        if self.tag == None:
            return self.value
        html = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return html
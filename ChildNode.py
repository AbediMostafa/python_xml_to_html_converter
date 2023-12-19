
class ChildNode:
    name = ''
    children = []
    el_attributes = ''
    el_data = ''
    data_first = False

    def __init__(self, name, key=None, value=None, data=None):
        self.name = name

        if key:
            self.add_attribute(key, value)

        if data:
            self.add_data(data)

    def add_element(self, name, key=None, value=None, data=None, data_first=False):
        node = ChildNode(name)
        if key:
            node.add_attribute(key, value)

        if data:
            node.add_data(data)

        self.children = self.children + [node]
        node.data_first = data_first
        return node

    def add_class(self, el_class):
        self.add_attribute('class', el_class)

    def add_style(self, el_style):
        self.add_attribute('style', el_style)

    def add_data(self, data):
        self.el_data = data

    def add_attribute(self, key, value):
        self.el_attributes += f' {key}="{value}" '


def execute(node):
    node_elements = ''
    for child in node.children:
        node_elements += execute(child)

    content = f'{node.el_data}{node_elements}' if node.data_first else f'{node_elements} {node.el_data}'
    element = f'<{node.name} {node.el_attributes}> {content}</{node.name}>'

    f = open("index.html", "w")
    f.write(element)
    f.close()

    return element

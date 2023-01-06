class Node():
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def add_left(self, new_left):
        self.left = new_left
        return

    def __str__(self):
        return f"Node(value={self.value}, left={self.left}, right={self.right})"

class NewNode(Node):
    def __init__(self, value, left=None, right=None):
        super().__init__(value, left, right)

    def __str__(self):
        return "DIFFERENT METHOD LOL"

root_node = Node(value=5)
node1 = Node(value=4)
node2 = Node(value=6)
root_node.left = node1
root_node.right = node2

test_node = NewNode(value=10)
test_node.add_left(root_node)

print(f"node value, left, and right: {root_node}")
print(f"node value, left, and right: {node1}")
print(f"node value, left, and right: {node2}")
print(f"node value, left, and right: {test_node}")
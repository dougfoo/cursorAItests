
class Node:
    def __init__(self, num):
        self.num = num
        self.left = None
        self.right = None

    def __str__(self):
        return f"Node({self.num} and sum of children: {self.sum()}"

    def __repr__(self):
        return f"Node({self.num})"

    def sum(self):
        return self.num + (self.left.sum() if self.left is not None else 0) + (self.right.sum() if self.right is not None else 0)

def main():
    # Create a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    # Print the tree nodes
    print("Root:", root)
    print("Left subtree:", root.left)
    print("Right subtree:", root.right)
    print("Leaf nodes:", root.left.left, root.left.right, root.right.left, root.right.right)


if __name__ == "__main__":
    main()




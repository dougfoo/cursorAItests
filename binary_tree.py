class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.left = self.tail  # left pointer is previous node
            self.tail.right = new_node # right pointer is next node
            self.tail = new_node
            
    def print_list(self) -> None:
        """
        Prints the linked list in both forward directions using recursion and iteration.
        Used for testing that both approaches give the same result.
        
        Example:
            ll = LinkedList()
            ll.append(1)
            ll.append(2) 
            ll.append(3)
            ll.print_list()
            # Output:
            # 1 2 3 (recursive)
            # 1 2 3 (iterative)
        """
        def _print_recursive(node):
            if not node:
                return
            print(node.value, end=" ")
            _print_recursive(node.right)
            
        _print_recursive(self.head)
        print()
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.right
        print()
        
    def print_reverse(self):
        current = self.tail
        while current:
            print(current.value, end=" ")
            current = current.left
        print()


class BinaryTree:
    def __init__(self, name):
        self.name = name
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return
        
        def _insert_recursive(node, value):
            if value < node.value:
                if node.left is None:
                    node.left = Node(value)
                else:
                    _insert_recursive(node.left, value)
            else:  # value >= node.value
                if node.right is None:
                    node.right = Node(value)
                else:
                    _insert_recursive(node.right, value)
        
        _insert_recursive(self.root, value)
    
    def delete(self, value):
        if not self.root:
            return
        
        # Find the node to delete and its parent
        current = self.root
        parent = None
        is_left_child = False
        
        while current and current.value != value:
            parent = current
            if value < current.value:
                current = current.left
                is_left_child = True
            else:
                current = current.right
                is_left_child = False
        
        if not current:
            return  # Value not found
        
        # Case 1: Node has no children
        if not current.left and not current.right:
            if not parent:  # Root node
                self.root = None
            elif is_left_child:
                parent.left = None
            else:
                parent.right = None
            return
        
        # Case 2: Node has only one child
        if not current.left:  # Only right child
            if not parent:  # Root node
                self.root = current.right
            elif is_left_child:
                parent.left = current.right
            else:
                parent.right = current.right
            return
        
        if not current.right:  # Only left child
            if not parent:  # Root node
                self.root = current.left
            elif is_left_child:
                parent.left = current.left
            else:
                parent.right = current.left
            return
        
        # Case 3: Node has two children
        # Find the inorder successor (smallest value in right subtree)
        successor_parent = current
        successor = current.right
        
        while successor.left:
            successor_parent = successor
            successor = successor.left
        
        # Replace current node with successor
        current.value = successor.value
        
        # Remove the successor
        if successor_parent == current:
            successor_parent.right = successor.right
        else:
            successor_parent.left = successor.right

def main():
    # Create a binary tree named "TestTree"
    tree = BinaryTree("TestTree")
    
    # Insert 5 nodes with values 10, 20, 30, 40, 50
    print("Inserting nodes into the binary tree...")
    print("Inserted: 30")
    tree.insert(40)
    print("Inserted: 40")
    tree.insert(50)
    print("Inserted: 50")
    tree.insert(10)
    print("Inserted: 10")
    tree.insert(20)
    print("Inserted: 20")
    tree.insert(30)
    
    print("\nBinary tree '{}' has been created with 5 nodes.".format(tree.name))
    print("The tree structure is now:")
    def print_tree(node, level=0, prefix=""):
        if not node:
            return
        
        print("    " * level + prefix + str(node.value))
        
        if node.left or node.right:
            if node.left:
                print("    " * level + "    /")
                print_tree(node.left, level + 1)
            if node.right:
                if not node.left:
                    print("    " * level + "    \\") 
                else:
                    print("    " * level + "     \\")
                print_tree(node.right, level + 1)
    
    print_tree(tree.root)

    print("\nTesting LinkedList implementation...")
    ll = LinkedList()
    
    # Test appending nodes
    print("Appending values 1, 2, 3 to linked list...")
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(44)
    ll.append(55)
    ll.append(6663)
    
    print("\nPrinting list forward (recursive and iterative):") 
    ll.print_list()
    
    print("\nPrinting list in reverse:")
    ll.print_reverse()




if __name__ == "__main__":
    main() 
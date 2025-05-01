class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
        
    def __str__(self):
        return f"Node({self.name})"
        
    def __repr__(self):
        return self.__str__()

class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, name):
        if not self.root:
            self.root = Node(name)
            return
            
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            
            if not node.left:
                node.left = Node(name)
                return
            queue.append(node.left)
            
            if not node.right:
                node.right = Node(name)
                return
            queue.append(node.right)
            
    def delete(self, name):
        if not self.root:
            return
            
        if self.root.name == name and not self.root.left and not self.root.right:
            self.root = None
            return
            
        queue = [(self.root, None)]
        node_to_delete = None
        parent = None
        
        while queue:
            current, parent = queue.pop(0)
            if current.name == name:
                node_to_delete = current
                break
                
            if current.left:
                queue.append((current.left, current))
            if current.right:
                queue.append((current.right, current))
                
        if not node_to_delete:
            return
            
        deepest_node = None
        deepest_parent = None
        queue = [(self.root, None)]
        
        while queue:
            current, parent = queue.pop(0)
            deepest_node = current
            deepest_parent = parent
            
            if current.left:
                queue.append((current.left, current))
            if current.right:
                queue.append((current.right, current))
                
        node_to_delete.name = deepest_node.name
        
        if deepest_parent:
            if deepest_parent.left == deepest_node:
                deepest_parent.left = None
            else:
                deepest_parent.right = None
        else:
            self.root = None
            
    def print_preorder(self):
        def _preorder(node):
            if node:
                print(node, end=' ')
                _preorder(node.left)
                _preorder(node.right)
                
        _preorder(self.root)
        print()

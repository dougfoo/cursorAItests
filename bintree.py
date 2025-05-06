

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        """Returns concise string representation of tree structure"""
        return self.__repr__()
        
    def __repr__(self):
        """Returns concise recursive representation of tree structure"""
        left = str(self.left) if self.left else "None"
        right = str(self.right) if self.right else "None"
        return f"[{self.val}, L:{left}, R:{right}]"

class Solution:
    def __init__(self):
        self.ctr = 0

    def goodNodes(self, root: TreeNode) -> int:
        # iterate all paths
        #  if left, check cur.val < node.left.val
        #      continue go left
        # if good +1 else 0
#        return self.travCount(root, 0)
        return dfs(root, float("-inf"))  # Start with the smallest possible value

    def travCount(self, node: TreeNode, max: int) -> int:
        if (node is None):
            return 0

        ct = 0
        if (node.val >= max):
            max = node.val
#            print(f"good node {node}")
            ct = 1
            self.ctr += 1 

        if (node.left is None and node.right is None):
            return ct
        else:
            return ct + self.travCount(node.left, max) + self.travCount(node.right, max)

def dfs(node, max_so_far):
    if not node:
        return 0
    
    # Check if this is a "good node"
    good = 1 if node.val >= max_so_far else 0
    
    # Update the max value for the next path
    new_max = max(max_so_far, node.val)
    
    # Count good nodes from left and right children
    return good + dfs(node.left, new_max) + dfs(node.right, new_max)


# [3,1,4,3,null,1,5]

def test3():
    # Test tree structure:
    #                    -1
    #            5               -2
    #        4       4       2       -2
    #     -4                -2  3        -2
    #   0                 -1  -3      -4   -3
    # 3                     -3
    #
    # Create test tree: [-1,5,-2,4,4,2,-2,null,null,-4,null,-2,3,null,-2,0,null,-1,null,-3,null,-4,-3,3,null,null,null,null,null,null,null,3,-3]
    root = TreeNode(-1)
    root.left = TreeNode(5)
    root.right = TreeNode(-2)
    
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(-2)
    
    root.left.left.left = TreeNode(-4)
    root.right.left.left = TreeNode(-2)
    root.right.left.right = TreeNode(3)
    root.right.right.right = TreeNode(-2)
    
    root.left.left.left.left = TreeNode(0)
    root.right.left.left.left = TreeNode(-1)
    root.right.left.left.right = TreeNode(-3)
    root.right.right.right.left = TreeNode(-4)
    root.right.right.right.right = TreeNode(-3)
    
    root.left.left.left.left.left = TreeNode(3)
    root.right.left.left.right.left = TreeNode(-3)
    
    # Create solution instance and test
    solution = Solution()
    result = solution.goodNodes(root)
    print(f"Test 2 - Number of good nodes: {result}, {solution.ctr} vs expected (5)")

def test2():
    # Test tree structure:
    #       3
    #    1     4
    #  3     1   5
    # 2
    #
    # Create test tree: [3,1,4,3,null,1,5]
    root = TreeNode(3)
    root.left = TreeNode(1) 
    root.right = TreeNode(4)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(2)
    root.left.left.right = TreeNode(6)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)

    # Create solution instance
    solution = Solution()
    
    # Test goodNodes
    result = solution.goodNodes(root)
    print(f"Test 2 - Number of good nodes: {result}, {solution.ctr} vs expected (5)")

def test1():
    # Test tree structure:
    #       3
    #    1     4
    #  3     1   5
    #
    # Create test tree: [3,1,4,3,null,1,5]
    root = TreeNode(3)
    root.left = TreeNode(1) 
    root.right = TreeNode(4)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)

    # Create solution instance
    solution = Solution()
    
    # Test goodNodes
    result = solution.goodNodes(root)
    print(f"Test 1 - Number of good nodes: {result}, {solution.ctr} vs expected (4)")


def main():
    test1()
    print('')
    test2()
    print('')
    test3()

if __name__ == "__main__":
    main()



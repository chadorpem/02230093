#task 1
# Node Class
'''class Node:
    def __init__(self, value):
        self.value = value      
        self.left = None        
        self.right = None       
# Binary Tree Class
class BinaryTree:
    def __init__(self, root_value=None):
        if root_value is not None:
            self.root = Node(root_value)  
        else:
            self.root = None              
# Example Usage
tree = BinaryTree()
print("Created new Binary Tree")
print("Root:", tree.root)'''
#Task 2
# Node Class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# Binary Tree Class
class BinaryTree:
    def __init__(self, root_value=None):
        self.root = Node(root_value) if root_value is not None else None
# 1. Height of Tree
    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))
# 2. Size (Total Nodes)
    def size(self, node):
        if node is None:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)
# 3. Count Leaf Nodes
    def count_leaves(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self.count_leaves(node.left) + self.count_leaves(node.right)
# 4. Check Full Binary Tree
    def is_full_binary_tree(self, node):
        if node is None:
            return True
        if (node.left is None and node.right is None):
            return True
        if (node.left is not None and node.right is not None):
            return (self.is_full_binary_tree(node.left) and
                    self.is_full_binary_tree(node.right))
        return False
# 5. Check Complete Binary Tree
    def is_complete_binary_tree(self):
        if self.root is None:
            return True
        queue = [self.root]
        flag = False  # becomes True when a NULL is seen
        while queue:
            current = queue.pop(0)
            if current is None:
                flag = True
            else:
                if flag:
                    return False
                queue.append(current.left)
                queue.append(current.right)
                return True
# Example Usage
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
print("Tree Height:", tree.height(tree.root))
print("Total Nodes:", tree.size(tree.root))
print("Leaf Nodes Count:", tree.count_leaves(tree.root))
print("Is Full Binary Tree:", tree.is_full_binary_tree(tree.root))
print("Is Complete Binary Tree:", tree.is_complete_binary_tree())
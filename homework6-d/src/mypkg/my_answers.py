class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.data)
"""
QUESTION 1
============================================================
Write a function "build_tree" that takes a list and other arguments
to construct a full binary tree that consists of nodes.
The TreeNode class is defined above.



Example 1:
===============================
The list [1, 3, None] should return a tree like:

   1
  / \
 3  None

Example 2:
===============================
The list [9, 7, 12, None, None, 3, None] should return a tree like:

           9
        /     \
       7      12
     /  \    /  \
 None  None 3  None
"""

def build_tree(data):
    from collections import deque
    n = iter(data)
    tree = TreeNode(next(n))
    fringe = deque([tree])
    while True:
        head = fringe.popleft()
        try:
            head.left = TreeNode(next(n))
            fringe.append(head.left)
            head.right = TreeNode(next(n))
            fringe.append(head.right)
        except StopIteration:
            break
    return tree


"""
QUESTION 2
============================================================
Write tests for "build_tree" function in test_build_tree.py in directory tests.
"""

"""
QUESTION 3
============================================================
Write a binary class tree with name "BinaryClass" that 

- initializes the tree for a given "node" as an argument and assigns it
to an attribute of the class which is also called "node"; also creates new
attributes "left" and "right" which are "None" by default.

- has a method called "add_left" that takes a new node as an argument
and assigns it to the left node of the tree.

- has a method called "add_right" that takes a new node as an argument
and assigns it to the right node of the tree.

- has a method is_leaf that returns True if the tree does not have any
children.
"""
class BinaryClass(object):
    def __init__(self, node, left=None, right=None):
        self.node = node

        self.left = left
        self.right = right
    def __str__(self):
        return str(self.node)

    def add_left(self,new_node):
        self.left = BinaryClass(new_node)


    def add_right(self,new_node):
        self.right = BinaryClass(new_node)

    def is_leaf(self):
        if (self.left == None) &(self.right == None):
            return True
        return False

"""
QUESTION 4
============================================================
Write tests for "BinaryTree" class in test_binary_tree.py in directory tests.
"""


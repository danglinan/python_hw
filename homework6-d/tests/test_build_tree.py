import pytest
from mypkg.my_answers import TreeNode
from mypkg.my_answers import build_tree

import pytest
from mypkg.my_answers import build_tree

def test_example1():
    # implement this
    data = [1,2,3,4,5,6,7]
    tree = build_tree(data)
    assert(str(tree) == "1")
    assert(str(tree.left) == "2")
    assert(str(tree.right) == "3")
    assert(str(tree.left.left) == "4")
    assert(str(tree.left.right) == "5")
    assert(str(tree.right.left) == "6")
    assert(str(tree.right.right) == "7")
    assert(str(tree.right.right.right) == "None")

def test_example2():
    # implement this
    data = [1,2,None]
    tree = build_tree(data)
    assert(str(tree) == "1")
    assert(str(tree.left) == "2")
    assert(str(tree.right) == "None")

def test_example3():
    # implement this
    data = [9, 7, 12, None, None, 3, None]
    tree = build_tree(data)
    assert(str(tree) == "9")
    assert(str(tree.left) == "7")
    assert(str(tree.right) == "12")
    assert(str(tree.left.left) == "None")
    assert (str(tree.left.right) == "None")
    assert (str(tree.right.left) == "3")
    assert(str(tree.right.right) == "None")

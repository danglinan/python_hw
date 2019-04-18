import pytest
from mypkg.my_answers import TreeNode
from mypkg.my_answers import BinaryClass

def test_example1():
    # implement this
    t = BinaryClass(1)
    assert(t.is_leaf())

def test_example2():
    # implement this
    t = BinaryClass(1)
    assert(str(t) == "1")
    t.add_left(2)
    assert(str(t.left) == "2")
    t.add_right(3)
    assert(str(t.right) == "3")
    assert(not t.is_leaf())
def test_example3():
    # implement this
    t = BinaryClass(1)
    assert(str(t) == "1")
    t.add_left(2)
    assert(str(t.left) == "2")
    t.add_right(3)
    assert(str(t.right) == "3")
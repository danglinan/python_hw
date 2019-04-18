import pytest
from mypkg.my_answers import Node
from mypkg.my_answers import is_cycled

def test_example1():
    node1, node2, node3, node4 = Node(1), Node(2), Node(3), Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    assert (is_cycled(node1))

def test_example1():
    node1, node2, node3, node4 = Node(1), Node(2), Node(3), Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    assert (not is_cycled(node1))
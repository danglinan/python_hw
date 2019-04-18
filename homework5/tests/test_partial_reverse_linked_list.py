import pytest
from mypkg.my_answers import Node
from mypkg.my_answers import partial_reverse_linkedlist


def test_example1():
    node1, node2, node3, node4, node5, node6, node7 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    m = 3
    n = 6

    res = partial_reverse_linkedlist(node1, m, n)

    assert(res.data == 1)
    assert(res.next.data == 2)
    assert(res.next.next.data == 6)
    assert(res.next.next.next.data == 5)
    assert(res.next.next.next.next.data == 4)
    assert(res.next.next.next.next.next.data == 3)
    assert(res.next.next.next.next.next.next.data == 7)

def test_example2():
    node1, node2, node3, node4, node5, node6, node7 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    m = 1
    n = 7

    res = partial_reverse_linkedlist(node1, m, n)

    assert(res.data == 7)
    assert(res.next.data == 6)
    assert(res.next.next.data == 5)
    assert(res.next.next.next.data == 4)
    assert(res.next.next.next.next.data == 3)
    assert(res.next.next.next.next.next.data == 2)
    assert(res.next.next.next.next.next.next.data == 1)


def test_example3():
    node1, node2, node3, node4, node5, node6, node7 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    m = 3
    n = 3

    res = partial_reverse_linkedlist(node1, m, n)

    assert(res.data == 1)
    assert(res.next.data == 2)
    assert(res.next.next.data == 3)
    assert(res.next.next.next.data == 4)
    assert(res.next.next.next.next.data == 5)
    assert(res.next.next.next.next.next.data == 6)
    assert(res.next.next.next.next.next.next.data == 7)
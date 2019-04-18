"""
QUESTION 1:
=======================================================================

Write a function "partial_reverse_linkedlist" that reverses
a linked list between positions m and n. The arguments to the function
should be linked_list, m, n. The type of linked_list will be a linked
list where each node is created by Node class. The types of m and n
are integers such that 1<=m<=n<=length_of_linked_list.
You should implement this in one pass.

The class for Node is defined for you.

Example:
===========================================
Input: 1->2->3->4->5->6->7->None, m=3, n=6
Output: 1->2->6->5->4->3->2->7
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
def partial_reverse_linkedlist(head, m, n):
    if m == n:
        return head
    falseNode = Node(0)
    falseNode.next = head
    pre = falseNode
    for i in range(m - 1):
        pre = pre.next
    # reverse the [m, n] nodes
    reverse = None
    cur = pre.next
    for i in range(n - m + 1):
        next = cur.next
        cur.next = reverse
        reverse = cur
        cur = next
    pre.next.next = cur
    pre.next = reverse
    return falseNode.next








"""
QUESTION 2:
=======================================================================

Write a function is_cycled that determines if a linked list has a
cycle. The argument to the function is a linked list that contains
nodes which are instances of the Node class. The function returns True
is there is a cycle in the list.

Examples:
===========================================
Input: node1 -> node2 -> node3 -> node2 ...
Output: True

Input: node1 -> node2 -> node3 -> node4 -> None
Output: False
"""
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
def is_cycled(head):

    if head == None or head.next == None:
        return False

    slow = head
    fast = head.next
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if (slow == fast):
            return True

    return False






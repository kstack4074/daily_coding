'''
Given two singly linked lists that intersect at some point, find that point.
The lists are non-cyclical.

e.g.
A = 3 -> 7 -> 8 -> 10
B = 99 -> 1 -> 8 -> 10

value return should be 8.
Do this in O(M + N) and constant space.
'''

class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def intersection_val(head1, head2, listDiff):
    node = head1
    node2 = head2
    for _ in range(0, listDiff):
        node = node.next

    while node != None and node.data != node2.data:
        node = node.next
        node2 = node2.next

    return node.data

def list_intersection(head1, head2):
    c1, c2 = 0, 0
    node = head1
    while node != None:
        c1 += 1
        node = node.next

    node = head2
    while node!= None:
        c2 += 1
        node = node.next

    listDiff = abs(c1 - c2)
    if c1 > c2:
        return intersection_val(head1, head2, listDiff)
    else:
        return intersection_val(head2, head1, listDiff)

n10 = Node(10)
n8 = Node(8, n10)
n7 = Node(7, n8)
n3 = Node(3, n7)
nx = Node(2, n3)

n1 = Node(1, n8)
n99 = Node(99, n1)

node = n3

print(list_intersection(nx, n99))

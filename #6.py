'''
An XOR linked list is a more efficient doubly linked listself.
Instead of each node holding next and prev fields, it holds a
field named both, which is an XOR of the next and previous nodes.

Implement an XOR linked list.
It has:
    - add(element) which appends the element
    - get(index) which returns the node at index

If using a language with no pointers, assume you have access to functions
get_pointer and deference_pointers that convers between nodes and memory
addresses.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.both = None

    def set_pos(self, both):
        self.both = both

class Linked_List:
    def add(self, element):
        print("add function")

    def get(self, index):
        print(index)

list = Linked_List()
# a.get(1)
# n1 = Node("1", None)
n1 = Node("1")

list.add(n1)

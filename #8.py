'''
A unival tree (which stands for "universal value") is a tree where
all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

The trees in this case will be all leaf nodes, and the [1,1,1] tree.

We will have to do this recursively as we don't know the size
of the tree.

We will also have to start from the bottom, this way we can keep track
of what we've already seen.

If we keep a value for the left sub-tree and the right sub-tree to
indicate if all the values are the same, and if not set to Noneself.

e.g.
    1
   / \
  1   1

unitrees = [0], set to an array so we don't have to return the element.
Start at root.left, this has no children so uniTress[0] += 1.
We will return value of 1 to root node. (leftTreeVal)
Check the root.right, this has no children so uniTrees[0] += 1.
We will return value of 1 to root node. (rightTreeVal)

if leftTreeVal == rightTreeVal:
    uniTrees[0] += 1
'''

class Node:
    def __init__ (self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def unival_number(node):
    univalNum = [0]
    helper(node, univalNum)

    return univalNum[0]

def helper(node, univalNum):
    leftTreeVal = None
    rightTreeVal = None

    #Leaf Node
    if(not node.left and not node.right):
        univalNum[0] += 1
        return node.data

    #Recursion
    if(node.left):
        leftTreeVal = helper(node.left, univalNum)
    if(node.right):
        rightTreeVal = helper(node.right, univalNum)
    #Balanced children
    if leftTreeVal == rightTreeVal == node.data:
        univalNum[0] += 1
        return leftTreeVal

    #Unbalanced children
    if(node.left == None or node.right == None):
        if leftTreeVal == node.data:
            univalNum[0] += 1
            return leftTreeVal

        elif rightTreeVal == node.data:
            univalNum[0] += 1
            return rightTreeVal


RLL = Node(1, None, None)
RLR = Node(1, None, None)
RL = Node(1, RLL, RLR)
RR = Node(0, None, None)
L = Node(1, None, None)
R = Node(0,RL, RR)
root = Node(0, L, R)
univalNum = [None]

unival_number(root)

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

'''
Counts the number of unival subtrees O(n^2)
'''
def count_univals(root):
    if root == None:
        return 0

    total_count = count_univals(root.left) + count_univals(root.right)
    if is_unival(root):
        total_count += 1
    return total_count

'''
Returns whether or not a given root node is a unival tree
'''
def is_unival(root):
    if root == None:
        return True
    if root.left != None and root.left.data != root.data:
        return False
    if root.right != None and root.right.data != root.data:
        return False
    if is_unival(root.left) and is_unival(root.right):
        return True
    return False

'''
Wrapper for helper2
'''
def count_univals2(root):
    total_count, is_unival = helper2(root)
    return total_count

'''
Returns the number of unival sub trees from a root node, and whether the root
node forms a unival subtree
O(n)
'''
def helper2(root):
    is_unival = True
    if root == None:
        return (0, True)
    left_count, is_left_unival = helper2(root.left)
    right_count, is_right_unival = helper2(root.right)

    if not is_left_unival or not is_right_unival:
        is_unival = False

    if root.left != None and root.left.data != root.data:
        is_unival = False
    if root.right != None and root.right.data != root.data:
        is_unival = False

    if is_unival:
        return (left_count + right_count + 1, True)
    else:
        return (left_count + right_count, False)


RLL = Node(1, None, None)
RLR = Node(1, None, None)
RL = Node(1, RLL, RLR)
RR = Node(0, None, None)
L = Node(1, None, None)
R = Node(0,RL, RR)
root = Node(0, L, R)
univalNum = [None]

print(count_univals2(root))

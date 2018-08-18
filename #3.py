class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):
    nodeList = []
    serializeList(node, nodeList)
    return ",".join(nodeList)

def serializeList(node, nodeList):
    if(node):
        nodeList.append(node.val)
        serializeList(node.left, nodeList)
        serializeList(node.right, nodeList)
    else:
        nodeList.append('')
    return

def deserialize(nodeString):
    nodeList = nodeString.split(",")
    node = deserializeList(nodeList)
    return node

def deserializeList(nodeList):
    node = None
    firstEle = None
    if(nodeList):
        firstEle = nodeList.pop(0)
        if(firstEle == ''):
            return node
        else:
            node = Node(firstEle, deserializeList(nodeList), deserializeList(nodeList))
    return node

node = Node('root', Node('left', Node('left.left')), Node('right'))
nodeList = []
nodeString = serialize(node)
node = deserialize(nodeString)
serialize(node)
print(node.right.val)

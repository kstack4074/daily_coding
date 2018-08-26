'''
Given a singly linked list, delete the kth last element.
We want to accomplis this in only one pass of the list, assume that k is
always less than the length of the list.
'''

class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next

def remove_element(head, k):
    if head.next == None:
        return None

    prev_ele_k = head
    cur = head
    ele_k = head.next
    idx = 0

    while cur:
        if idx - k - 1 > 0:
            prev_ele_k = ele_k
            ele_k = ele_k.next
        cur = cur.next
        idx += 1

    #Removing the head
    if idx - 1 == k:
        prev_ele_k.next = None
        return ele_k
    #Removing some other element
    else:
        prev_ele_k.next = ele_k.next
        #print('removing' + str(prev_ele_k.data) + str(ele_k.data))
        return head

if __name__ == '__main__':
    rrr = Node(3, None)
    rr = Node(2, rrr)
    r = Node(1, rr)

    cur = remove_element(r, 2)
    while cur:
        print(cur.data)
        cur = cur.next

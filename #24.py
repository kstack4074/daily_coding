'''
Implement locking in a binary tree. A treen node can be locked or unlocked only if:
    - all descendants are not locked
    OR
    - all ancestors are not locked

Design a binary tree node class with the following methods:
    - is_locked, which returns whether the node is locked
    - lock, which attempts to lock the node. If it cannot be locked, return false, else return true
    - unlock, same as above but with unlocking.

You may augment nodes as you wish.
'''

class Node:
    def __init__(self, data, left = None, right = None, parent = None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = None
        self.locked = False
        self.descendants_locked_count = 0

    def _can_lock_unlock(self):
        #Check all descendants
        if self.descendants_locked_count > 0:
            return False

        #Check all ancestors
        cur = self.parent
        while cur:
            if cur.is_locked() == True:
                return False
            cur = cur.parent

        return True

    def is_locked(self):
        return self.locked

    def lock(self):
        #Check if already locked
        if self.is_locked() == True:
            return False

        if self._can_lock_unlock():
            self.locked = True
            cur = self.parent
            while cur:
                cur.descendants_locked_count += 1
                cur = cur.parent

            return True
        return False

    def unlock(self):
        #Check if already unlocked
        if self.is_locked() == False:
            return False

        if self._can_lock_unlock():
            self.locked = False
            cur = self.parent
            while cur:
                cur.descendants_locked_count -= 1
                cur = cur.parent

            return True
        return False

    def add_parent(self, parent):
        self.parent = parent

if __name__ == '__main__':
    LL = Node('LL')
    LR = Node('LR')
    L = Node('L', LL, LR)
    LL.add_parent(L)
    LR.add_parent(L)
    RL = Node('RL')
    RR = Node('RR')
    R = Node('R', RL, RR)
    RR.add_parent(R)
    RL.add_parent(R)
    root = Node('root', L, R)
    R.add_parent(root)
    L.add_parent(root)

    LL.lock()
    print(L._can_lock_unlock())

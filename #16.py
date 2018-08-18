'''
You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, with the following API:

- record(order_id): adds the order_id to the log
- get_last(i): gets the ith last element from the log. i is guaranteed to be
    less than the array size

You should be efficient as possible with time and space.

Dynamic array?
Lookup time is O(1) and average append time is O(1) with amortized cost.
However we only want to keep N elements, so we would to remove first element and shift
everything down.

OR

We can use a cyclic array where we keep track of our start and our append.
The array has a fixed size of N so this should be doable.
Lookups, and appends will be constant then with a space complexity of O(n)
'''

class Log():

    def __init__(self):
        self.N = 100
        self._appendIdx = 0
        self._log = []

    def record(self, order_id):
        if len(self._log) < 100:
            self._log.append(order_id)
        else:
            self._log[self._appendIdx] = order_id

        self._appendIdx = (self._appendIdx + 1) % self.N

    def get_last(self, i):
        log = self._log
        if i > self.N or i <= 0:
            raise ValueError('Please bound to 1 <= i <= ' + str(self.N))

        idx = self._appendIdx - i
        if idx < 0:
            idx = 100 + idx

        return log[idx]

    def get_all(self):
        return self._log

x = Log()
for i in range(0, 102):
    x.record(i)

print(x.get_all())
print(x.get_last(3))

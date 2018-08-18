ENDS_HERE = '__ENDS_HERE'

class Trie(object):
    def __init__(self):
        self._trie = {}

    def insert(self, text):
        trie = self._trie
        for char in text:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie[ENDS_HERE] = True

    def elements(self, prefix):
        d = self._trie
        for char in prefix:
            if char in d:
                d = d[char]
            else:
                return []
        return [prefix + a for a in self._readable_elements(d)]

    def _readable_elements(self, dict):
        result = []
        for k, v in dict.items():
            if k == ENDS_HERE:
                subResult = ['']
            else:
                subResult = [k + s for s in self._readable_elements(v)]
            result.extend(subResult)

        return result

def auto_complete(prefix):
    temp = trie.elements(prefix)
    print(temp)

words = ['ab', 'abc', 'bc', 'dog', 'ok']
trie = Trie()
for word in words:
    trie.insert(word)

auto_complete('a')

'''
Given a dictionary of words and a string made up of those words
(no spaces), return the original sentence in a list. If there is
more than one possible reconstruction, return any of them. If no
possible reconstruction, then return null.

For example, given the set of words:
'quick', 'brown', 'the', 'fox',
and the string:
'thequickbrownfox'
you should return:
['the', 'quick', 'brown', 'fox'].

Given the set of words:
'bed', 'bath', 'bedbath' 'and', 'beyond',
and the string:
'bedbathandbeyond'
you should return:
['bed', 'bath', 'and', 'beyond']
OR
['bedbath', 'and', 'beyond']

We can condsider a greedy approach initially. However duplicates
such as 'bed' and 'bedbath' will not work. So we should condsider
backtracking.

    - Iterate over string and split it into a prefix and suffix
    - If the prefix is valid, recursively call on suffix
    - If that's valid, return, else continue serach
    - At the end and haven't found anything, return empty

This run time is atrocious. If all the letters are the same,
and they're all in the dictionary, we get O(2^N)
s = 'aaaaab', dict = {'a', 'aa', 'aaa', 'aaaa', 'aaaaa'}
a:
    a:  aa: aaa: aaaa:
        a: aa: aaa:
            a: aa:
                a:
'''

def word_break(sentence, wordList):
    s, valid = helper(sentence, wordList)
    if valid:
        print(s)
        return s

def helper(sentence, wordList):
    size = len(sentence)
    if size == 0:
        return [], True

    result = []
    for i in range(size + 1):
        prefix, suffix = sentence[:i], sentence[i:]
        if prefix in wordList:
            rest, valid = helper(suffix, wordList)
            if valid:
                return [prefix] + rest, True

    return [], False



if __name__ == '__main__':
    wordList = {'the', 'thequick', 'brown', 'fox'}
    sentence = 'thequickfox'
    word_break(sentence, wordList)

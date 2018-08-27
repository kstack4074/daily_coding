'''
Given a string of round, curly, and square open and closing brackets,
return whether the brackets are well balanced.

e.g. '([])[]({})' -> True
     '([)]' -> False
     '((()' -> False
'''

def are_brackets_balanced(string):
    stack = []
    bracketList = {')': '(', ']': '[', '}':'{'}
    #Keys are closing brackets, values are opening

    for bracket in string:
        if bracket in bracketList.values():
            stack.append(bracket)
        elif bracket in bracketList.keys():
            if len(stack) <= 0:
                return False
            lastBracket = stack.pop()
            if lastBracket != bracketList[bracket]:
                return False

    if len(stack) != 0:
        return False
    else:
        return True


if __name__ == '__main__':
    tester = '([])[]({})'
    print(are_brackets_balanced(tester))

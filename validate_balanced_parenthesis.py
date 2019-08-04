"""
Hi, here's your problem today. This problem was recently asked by Uber:

Imagine you are building a compiler. Before running any code, the compiler
must check that the parentheses in the program are balanced. Every opening
bracket must have a corresponding closing bracket. We can approximate this
using strings.

Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.

Example:
Input: "((()))"
Output: True

Input: "[()]{}"
Output: True

Input: "({[)]"
Output: False
"""


class Solution:
    def __init__(self, s):
        self.chars = s

    def isvalid(self):
        opening = list(map(str, '[{('))
        closing = list(map(str, ']})'))
        items = []
        if len(self.chars) % 2 == 1:
            return False
        for c in self.chars:
            if c in opening:
                items.append(c)
            elif c in closing:
                try:
                    if items[-1] == opening[closing.index(c)]:
                        items.pop()
                except IndexError:
                    return False
        return len(items) == 0


if __name__ == '__main__':
    assert Solution('((()))').isvalid()
    assert Solution('[()]{}').isvalid()
    assert Solution('[( ) ]{}').isvalid()
    assert not Solution('[()]{(})').isvalid()
    assert not Solution('({[)]').isvalid()

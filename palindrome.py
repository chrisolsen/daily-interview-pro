#######################################################################################################################
# Hi, here's your problem today. This problem was recently asked by Twitter:
# A palindrome is a sequence of characters that reads the same backwards and forwards. Given a string, s, find the
# longest palindromic substring in s.

# Example:
# Input: "banana"
# Output: "anana"
# Input: "million"
# Output: "illi"
#######################################################################################################################


# This is the initial way I tried to solve this problem. Unfortunately, this way had a hard time
# dealing with both odd and even length words.
# def palindrome(word):
#     i, longest = 0, ''
#     while i < len(word):
#         for x in range(0, min(i+1, len(word)-i)):
#             a, b = word[i-x:i+1], word[i:i+x+1]
#             if a == b[::-1]:
#                 if len(a) * 2 > len(longest):
#                     longest = a + b[1:]
#             else:
#                 break
#         i += 1
#     return longest


# A better way of solving things is to identify all the combinations of substrings, starting from the largest size,
# and return the first palindrome found, which will thereby be the largest.
def palindrome(word):
    for i in range(len(word), 0, -1):
        contains, pal = contains_palindrome(word, i)
        if contains:
            print(pal)
            return pal
    raise 'not found'


# Identifies all the possible substrings for the length passed in
# |----- 1 -----|
#   |----- 2 -----|
# t r a c e c a r s
#
# |---- 1 ----|
#   |---- 2 ----|
#     |---- 3 ----|
# t r a c e c a r s
def contains_palindrome(word, length):
    if length > len(word):
        raise 'substring of word cannot be longer than word'
    gapsize = len(word) - length
    for i in range(gapsize):
        s = word[i:length+i+1]
        if is_palindrome(s):
            return (True, s)
    return (False, '')


# determine if word is an palindrome. If the strint being checked is an odd number
# of characters the middle letter must is ignored.
def is_palindrome(word):
    half = len(word) / 2
    if len(word) % 2 == 0:
        a, b = word[:half], word[half:]
    else:
        a, b = word[:half], word[half+1:]
    return a == b[::-1]


if __name__ == '__main__':
    assert palindrome('racecar') == 'racecar'
    assert palindrome('tracecars') == 'racecar'
    assert palindrome('banana') == 'anana'
    assert palindrome('million') == 'illi'
    assert palindrome('foobar') == 'oo'

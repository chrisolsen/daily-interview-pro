# Hi, here's your problem today. This problem was recently asked by Microsoft:
# Given a string, find the length of the longest substring without repeating characters.

# class Solution:
#   def lengthOfLongestSubstring(self, s):
#     # Fill this in.

# print Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx')
# > 10

# Can you find a solution in linear time?

def longest(input):
    chars, count, max_count = {}, 0, 0
    for c in input:
        if chars.has_key(c):
            max_count = count if count > max_count else max_count
            chars, count = {}, 0
        count += 1
        chars[c] = True

    return max_count

if __name__ == '__main__':
    count = longest('abrkaabcdefghijjxxx')
    assert 10 == count, '{} chars'.format(count)
    print('passed!')

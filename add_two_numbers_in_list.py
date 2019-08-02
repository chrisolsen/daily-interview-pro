# Hi, here's your problem today. This problem was recently asked by Microsoft:
# You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    @staticmethod
    def convert_number(num):
        factor = 1
        node = None
        root = None
        while True:
            if num <= 0:
                break
            val = num % (10**factor)
            num -= val
            factor += 1
            child = ListNode(val)
            if node is None:
                root = child
            else:
                node.next = child
            node = child
        return root

    def to_list(self):
        node = self
        ls = []
        f = 0
        while node is not None:
            ls.append(node.val / 10**f)
            node = node.next
            f += 1
        return ls

    def value(self):
        vals = reversed(self.to_list())
        sum = 0
        for i, v in enumerate(vals):
            sum += v * 10**i
        return sum

    def __len__(self):
        return len(self.to_list)

    def __repr__(self):
        return ' '.join(map(str, self.to_list()))

    def __add__(self, ln):
        return self.convert_number(self.value() + ln.value())

def add_two_numbers(n1, n2, c = 0):
    l1, l2 = ListNode.convert_number(n1), ListNode.convert_number(n2)
    print(l1 + l2)

if __name__ == '__main__':
    add_two_numbers(342, 465)
    add_two_numbers(3421, 465)

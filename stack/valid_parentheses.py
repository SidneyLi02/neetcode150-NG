class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        paren_dict = {
            '(' : ')',
            '{' : '}',
            '[' : ']',
        }

        for paren in s:
            if paren in paren_dict.keys():
                stack.append(paren)
            else:
                if not stack:
                    return False
                opening_paren = stack.pop()
                if paren_dict[opening_paren] != paren:
                    return False
        return not stack

        """
        NOTE: 
        solution:                     O(n) time, O(n) space
        """
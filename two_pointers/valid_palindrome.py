class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start, end = 0, len(s) - 1
        while (start < end):
            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue
            if s[start].lower() == s[end].lower():
                start, end = start + 1, end - 1
            else:
                return False
            
        return True

        """
        NOTE: 
        solution:                     O(n) time, O(1) space
        strip, reverse, compare:      O(n) time, O(n) space
        """
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        count_hm = {}
        for idx in range(len(s)):
            count_hm[s[idx]] = count_hm.get(s[idx], 0) + 1
            count_hm[t[idx]] = count_hm.get(t[idx], 0) - 1
        
        for count in count_hm.values():
            if count != 0: return False
        return True
    
        """
        NOTE: 
        solution:                     O(n) time, O(n) space
        two hashmaps:                 O(n) time, O(n) space (but two HMs)
        sorted strings:               O(n log n) time, O(1) space
        """
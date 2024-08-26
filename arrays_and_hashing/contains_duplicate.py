class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False
    
        """
        NOTE: 
        solution:                     O(n) time, O(n) space
        naive pairwise comparison:    O(n^2) time, O(1) space
        sorting one pass comparison:  O(n log n), O(1) space
        """
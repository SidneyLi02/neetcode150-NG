class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            mp = (start + end) // 2
            if nums[mp] == target:
                return mp
            elif nums[mp] < target:
                start = mp + 1
            else:
                end = mp - 1
        return -1
    
        """
        NOTE: 
        solution:                     O(log n) time, O(1) space
        """

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complements_hm = {}
        for idx in range(len(nums)):
            complement = target - nums[idx]
            complements_hm[complement] = idx
        
        for idx in range(len(nums)):
            if nums[idx] in complements_hm and idx != complements_hm[nums[idx]]:
                return [idx, complements_hm[nums[idx]]]
            
        """
        NOTE: 
        solution:                     O(n) time, O(n) space
        naive:                        O(n^2) time, O(1) space
        """
class Solution(object):
    def firstMissingPositive(self, nums):
        
        i = 0
        while i < len(nums):
            if nums[i] > 0 and nums[i] - 1 < len(nums) and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            else:
                i += 1
        
        for i, integer in enumerate(nums):
            if integer != i + 1:
                return i + 1
        return len(nums) + 1
        """
        :type nums: List[int]
        :rtype: int
        """
        

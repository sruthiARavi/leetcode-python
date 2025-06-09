"""
# 2016. Maximum Difference Between Increasing Elements
# Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].
# Return the maximum difference. If no such i and j exists, return -1.
"""
class lc2016(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        ans = -1
        pre_min = nums[0]

        for i in range(1, nums_len):
            if nums[i] > pre_min:
                ans = max(ans, nums[i] - pre_min)
            else:
                pre_min = nums[i]

        return ans 
        

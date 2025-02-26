"""
 # https://leetcode.com/problems/maximum-subarray/
 # 53. Maximum Subarray
 # Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""
class leetcode53(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Kadane's algorithm 
      
        maxSubArraySum = nums[0]
        currentSum = 0
        
        for n in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum += n
            maxSubArraySum = max(maxSubArraySum, currentSum)
        
        return maxSubArraySum
        

"""
 # https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/?envType=daily-question&envId=2025-02-26
 # 749. Maximum Absolute Sum of Any Subarray
 # You are given an integer array nums. 
 # The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).
 # Return the maximum absolute sum of any (possibly empty) subarray of nums.
 # Note that abs(x) is defined as follows:
   ## If x is a negative integer, then abs(x) = -x.
   ## If x is a non-negative integer, then abs(x) = x.
"""
class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Max absolute sum will be either the max sum or the min sum.
        # So, ust run kadane twice, once calculating the max sum and once calculating the min sum.
        # Kadane : https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/


        

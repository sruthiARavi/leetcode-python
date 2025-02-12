"""
# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/?envType=daily-question&envId=2025-02-01
# 1752. Check if Array Is Sorted and Rotated
# Given an array nums, return true if the array was originally sorted in non-decreasing order, 
# then rotated some number of positions (including zero). 
# Otherwise, return false.
# There may be duplicates in the original array.
# Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], 
# where % is the modulo operation.
"""
class leetcode1752(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n<=1:
            return True

        inversion_count = 0

        # For every pair, count the number of inversions.
        for index in range(1,n):
            if nums[index] < nums[index-1]:
                inversion_count += 1
                if inversion_count > 1:
                    return False
        
        # Also check between the last and the first element due to rotation
        if nums[0] < nums[n-1]:
            inversion_count += 1

        return inversion_count<=1


        

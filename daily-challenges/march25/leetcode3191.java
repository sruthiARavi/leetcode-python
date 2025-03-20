"""
 # 3191. Minimum Operations to Make Binary Array Elements Equal to One I
 # You are given a binary array nums.
 # You can do the following operation on the array any number of times (possibly zero):
   ## Choose any 3 consecutive elements from the array and flip all of them.
 # Flipping an element means changing its value from 0 to 1, and from 1 to 0.
 # Return the minimum number of operations required to make all elements in nums equal to 1. If it is impossible, return -1.
"""
class leetcode3191(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        if len(nums) < 2:
            return -1
        
        for i in range(2, len(nums)):
            if nums[i-2] == 0:
                nums[i-2] = 1
                nums[i-1] = nums[i-1] ^ 1
                nums[i] = nums[i] ^ 1
                count += 1

        if nums[len(nums)-2] == 0 or nums[len(nums)-1] == 0:
            return -1 

        return count
        

"""
# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/description/?envType=daily-question&envId=2025-02-13
# 3066. Minimum Operations to Exceed Threshold Value II
# You are given a 0-indexed integer array nums, and an integer k.
# In one operation, you will:
   ## Take the two smallest integers x and y in nums.
   ## Remove x and y from nums.
   ## Add min(x, y) * 2 + max(x, y) anywhere in the array.
 # Note that you can only apply the described operation if nums contains at least two elements.
 # Return the minimum number of operations needed so that all elements of the array are greater than or equal to k.
"""
class leetcode3066(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums) #nums becomes a heap 

        num_operations = 0; 
        while len(nums) >=2 and nums[0] < k: # The input is generated such that an answer always exists.
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            z = min(x,y) * 2 + max(x,y)
            num_operations += 1
            heapq.heappush(nums, z)

        return num_operations 

'''
3151. Special Array I
----------------------
An array is considered special if every pair of its adjacent elements contains two numbers with different parity.
You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.
'''
class leetcode3151(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(1, len(nums)):
            if nums[i]%2 == nums[i-1]%2:
                return False
        return True
        

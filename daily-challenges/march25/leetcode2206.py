"""
 # https://leetcode.com/problems/divide-array-into-equal-pairs/description/?envType=daily-question&envId=2025-03-17
 # 2206. Divide Array Into Equal Pairs
 # You are given an integer array nums consisting of 2 * n integers.
 # You need to divide nums into n pairs such that:
   ## Each element belongs to exactly one pair.
   ## The elements present in a pair are equal.
 # Return true if nums can be divided into n pairs, otherwise return false.
"""
class leetcode2206(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)%2!=0:
            return False
            
        unpaired = set()

        for num in nums:
            if num in unpaired:
                unpaired.remove(num)
            else:
                unpaired.add(num)

        return not unpaired
        

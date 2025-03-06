"""
 # https://leetcode.com/problems/find-missing-and-repeated-values/?envType=daily-question&envId=2025-03-06
 # 2965. Find Missing and Repeated Values
 # You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. 
 # Each integer appears exactly once except a which appears twice and b which is missing. 
 # The task is to find the repeating and missing numbers a and b.
 # Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.
"""
class leetcode2965:
    def __init__(self, name):
        self.name = name

    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        freq = {}

        for row in grid:
            for num in row:
                freq[num] = freq.get(num, 0) + 1

        for num in range(1, (n*n)+1):
            if num not in freq:
                missing = num
            elif freq[num] == 2:
                repeat = num

        return [repeat, missing]

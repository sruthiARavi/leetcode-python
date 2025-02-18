"""
 # https://leetcode.com/problems/find-the-punishment-number-of-an-integer/?envType=daily-question&envId=2025-02-15
 # 2698. Find the Punishment Number of an Integer
 # Given a positive integer n, return the punishment number of n.
 # The punishment number of n is defined as the sum of the squares of all integers i such that:
   ## 1 <= i <= n
   ## The decimal representation of i * i can be partitioned into contiguous substrings such that 
   ## the sum of the integer values of these substrings equals i.
"""
class leetcode2698(object):   
 
    def __init__(self):
        self.punishment_nums = self.find_top_1000_punishment_nums()

    def check_validity(self, num, target):
        if target < 0 or num < target:
            return False
        if num == target:
            return True 
        return (
            self.check_validity(num // 10, target - (num%10)) 
            or self.check_validity(num // 100, target - (num%100)) 
            or self.check_validity(num // 1000, target - (num%1000))
        )

    def find_top_1000_punishment_nums(self):
        p_nums = [1]
        for i in range(2, 1001):
            square_value = i*i
            if self.check_validity(square_value, i):
                p_nums.append(i)
        return p_nums
     
   def punishmentNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for i in range(1, n+1):
            if i in self.punishment_nums:
                ans += (i*i)
        return ans

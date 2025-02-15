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
  def punishmentNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

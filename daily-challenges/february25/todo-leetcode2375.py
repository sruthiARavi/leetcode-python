"""
 # https://leetcode.com/problems/construct-smallest-number-from-di-string/?envType=daily-question&envId=2025-02-18
 # 2375. Construct Smallest Number From DI String
 # You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.
 # A 0-indexed string num of length n + 1 is created using the following conditions:
 # num consists of the digits '1' to '9', where each digit is used at most once.
   ## If pattern[i] == 'I', then num[i] < num[i + 1].
   ## If pattern[i] == 'D', then num[i] > num[i + 1].
 # Return the lexicographically smallest possible string num that meets the conditions.
"""
class leetcode2375(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """

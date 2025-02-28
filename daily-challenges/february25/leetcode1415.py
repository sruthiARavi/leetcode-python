"""
 # https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/?envType=daily-question&envId=2025-02-19
 # 1415. The k-th Lexicographical String of All Happy Strings of Length n
 # A happy string is a string that:
   ## consists only of letters of the set ['a', 'b', 'c'].
   ## s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
 # For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.
 # Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.
 # Return the kth string of this list or return an empty string if there are less than k happy strings of length n.
"""
class leetcode1415(object):
    def __init__(self):
        self.happy_strings = []

    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.generateHappyStrings(n, k, "")
        if len(self.happy_strings) < k:
            return ""

        return self.happy_strings[k-1]

    
    def generateHappyStrings(self, n, k, current_string):
        if len(self.happy_strings) == k:
            return
        
        if len(current_string) == n:
            self.happy_strings.append(current_string)
            print(self.happy_strings)
            return 

        for current_char in ["a", "b", "c"]:
            if len(current_string) > 0 and current_string[-1] == current_char:
                continue
            
            self.generateHappyStrings(n, k, current_string + current_char)
        
        

'''
# 1768. Merge Strings Alternately
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.
'''
class leetcode1768(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ptr1 = 0
        ptr2 = 0
        ans = []
        while ptr1 < len(word1) or ptr2 < len(word2):
            if ptr1 < len(word1):
                ans.append(word1[ptr1])
                ptr1 += 1
            
            if ptr2 < len(word2):
                ans.append(word2[ptr2])
                ptr2 += 1

        return ''.join(ans)

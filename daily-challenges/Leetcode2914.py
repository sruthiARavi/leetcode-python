# https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/?envType=daily-question&envId=2024-11-05
# We can decompose the whole string into disjoint blocks of size 2 and find the minimum number of changes required to make those blocks beautiful
class Leetcode2914(object):
    def minChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        min_changes_required = 0         
        #step size 2 
        for i in range(0, len(s), 2):
            if s[i] != s[i+1]:
                min_changes_required += 1
        
        return min_changes_required
        

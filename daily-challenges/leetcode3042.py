# 3042. Count Prefix and Suffix Pairs I
# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/description/?envType=daily-question&envId=2025-01-08
class leetcode3042(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # Brute forcing it 
        n = len(words)
        count = 0

        for i in range(n):
            for j in range(i+1, n):
                str1 = words[i]
                str2 = words[j]

                if len(str1) > len(str2):
                    continue
                
                if str2.startswith(str1) and str2.endswith(str1):
                    # java has the same functionality 
                    count += 1

        return count 

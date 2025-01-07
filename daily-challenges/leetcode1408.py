# https://leetcode.com/problems/string-matching-in-an-array/?envType=daily-question&envId=2025-01-07
# Brute forcing it - checking against every other word in the array. Another alternative is KMP 
class leetcode1408(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        matching_words = []

        for current_word_index in range(len(words)):
            for other_word_index in range(len(words)):
                if current_word_index == other_word_index:
                    continue
                if words[current_word_index] in words[other_word_index]:
                    matching_words.append(words[current_word_index])
                    break 
                
        return matching_words 


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
            Approach: Calculate the frequency of letters in each string
            and use it as a key in hash map with the word as value.
        '''
        anagrams = {}
        for word in strs:
            counts = [0] * 26
            for char in word:
                counts[ord(char) - ord('a')] += 1

            key = tuple(counts)
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]

        return list(anagrams.values())
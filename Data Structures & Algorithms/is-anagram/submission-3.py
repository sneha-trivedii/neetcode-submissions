class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arrS = [0] * 26
        arrT = [0] * 26
        for char in s:
            arrS[ord(str.lower(char)) - ord('a')] += 1
        
        for char in t:
            arrT[ord(str.lower(char)) - ord('a')] += 1
        return arrS == arrT

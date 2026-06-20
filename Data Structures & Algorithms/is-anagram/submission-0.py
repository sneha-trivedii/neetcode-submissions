class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charStringS = {}
        for char in s:
            if char in charStringS:
                charStringS[char] += 1
            else:
                charStringS[char] = 1

        charStringT = {}
        for char in t:
            if char in charStringT:
                charStringT[char] += 1
            else:
                charStringT[char] = 1

        if charStringS == charStringT:
            return True
        else:
            return False


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Using 'sorted' function of string to sort and then compare
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
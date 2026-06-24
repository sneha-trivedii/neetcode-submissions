class Solution:
    '''
        Approach: We can use an encoding approach where we start with a number representing the length of the string, followed by a separator character (let's use # for simplicity), and then the string itself. To decode, we read the number until we reach a #, then use that number to read the specified number of characters as the string.
    '''
    def encode(self, strs: List[str]) -> str:
        encodedList = []
        for string in strs:
            encodedList.append(str(str(len(string))+'#'+string))
        return "".join(encodedList)

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            ans.append(word)
            i = j + len(word) + 1
        return ans
            

                
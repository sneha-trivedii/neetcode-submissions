class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
            Approach: Iterate over the input 'strs' and store them in a
            hash map by sorting them as {sorted_str: [strings]}. Then
            return the values as a list.
        '''

        stringMap = {}
        for string in strs:
            if "".join(sorted(string)) in stringMap:
                stringMap["".join(sorted(string))].append(string)
            else:
                stringMap["".join(sorted(string))] = [string]
            
        for value in stringMap.values():
            return list(stringMap.values())

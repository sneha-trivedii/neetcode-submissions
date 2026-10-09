class Solution:
    def isValid(self, s: str) -> bool:
        #Approach: Use stack
        stack = []
        for char in s:
            if char=='(' or char=='{' or char=='[':
                stack.append(char)
            else:
                if stack:
                    x=stack.pop()
                else:return False
                if x=='(' and char==')':
                    continue
                elif x=="{" and char=="}":
                     continue 
                elif x=="[" and char=="]":
                     continue 
                else:
                    return False
        
        if stack:
            return False
        else:
            return True
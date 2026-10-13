class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator=["+","-","*","/"]
        stack=[]
        for i in tokens:
            if i in operator:
                b=stack.pop()
                a=stack.pop()
                if i=="+":
                    stack.append(int(a)+int(b))
                elif i=="-":
                    stack.append(int(a)-int(b))
                elif i=="*":
                    stack.append(int(a)*int(b))
                else:
                    stack.append(int(a)/int(b))
            else:
                stack.append(i)
        if stack:
            return int(stack[-1])
class MinStack:

    def __init__(self):
        self.stack=[]
        self.mini=None
        self.prefMin=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mini==None:
            self.mini=val
            self.prefMin.append(val)
            return None
        self.prefMin.append(min(val,self.prefMin[-1]))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.prefMin.pop()
        if not self.prefMin:
            self.mini=None

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.prefMin:
            return self.prefMin[-1]

class MinStack:

    def __init__(self):
        self.stack=[]
        self.prefMin=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.prefMin:
            self.prefMin.append(min(val, self.prefMin[-1]))
        else:
            self.prefMin.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.prefMin.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.prefMin:
            return self.prefMin[-1]

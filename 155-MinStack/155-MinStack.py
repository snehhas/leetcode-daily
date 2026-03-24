# Last updated: 24/03/2026, 22:38:54
class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        self.result=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack)==0:
            self.min_stack.append(val)
        elif val<=self.min_stack[-1]:
            self.min_stack.append(val)

        self.result.append(None)
        return None

    def pop(self) -> None:
        p=self.stack.pop()
        if p==self.min_stack[-1]:
            self.min_stack.pop()
        self.result.append(None)
        
    def top(self) -> int:
        self.result.append(self.stack[-1])
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
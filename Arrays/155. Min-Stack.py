class MinStack:
    #initialize stack and minstack
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    #append to stack, append to minstack if val smaller than mintop
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or self.getMin() >= val:
            self.min_stack.append(val)
    #if top is min, pop top and mintop
    def pop(self) -> None:
        if self.top() == self.getMin():
            self.min_stack.pop()
        self.stack.pop()
    #return top of stack
    def top(self) -> int:
        return self.stack[-1]
    #top for minstack
    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float('inf')
        

    def push(self, x: int) -> None:
        if self.min >= x:
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)

    def pop(self) -> None:
        res = self.stack.pop()
        if self.min == res:
            self.min = self.stack.pop()
        return res

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min

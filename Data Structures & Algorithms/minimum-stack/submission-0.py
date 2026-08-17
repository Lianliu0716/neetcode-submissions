class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min == []:
            self.min.append(val)
        else:
            #temp = val < self.stack[-1]? val : self.stack[-1]
            temp = val if val < self.min[-1] else self.min[-1]
            self.min.append(temp)

    def pop(self) -> None:
        self.stack.pop(len(self.stack)-1)
        self.min.pop(len(self.min)-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]

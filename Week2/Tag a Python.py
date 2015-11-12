class Stack(object):

    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def peek(self):
        return self.stack[-1]

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()

with open('code.py') as f:
    for i in f:
        for j in i.strip():
            pass

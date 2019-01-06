'''
    Stack implementation
    Concept: FILO
'''

class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size


    def push(self, data):
        # TODO: Fix check length for non-list data
        if len(self.stack) >= self.size or len(data) > self.size:
            print('STACK OVERFLOW')
            return None

        if isinstance(data, list):
            self.stack.extend(data)
        else:
            self.stack.append(data)


    def _pop(self):
        temp = self.stack[-1]
        del self.stack[-1]

        yield temp


    def pop(self):
        last = next(self._pop())
        print(last)


    def pop_all(self):
        end = len(self.stack)
        for i in range(end):
            self.pop()


    def peek(self):
        print(self.stack[-1])
        return self.stack[-1]


    def all(self):
        print(self.stack)
        return self.stack


def main():
    s = Stack(3)
    s.push([1, 2, 3])
    s.all()
    s.pop()
    s.push(5)
    s.pop_all()
    s.all()


if __name__ == '__main__':
    main()
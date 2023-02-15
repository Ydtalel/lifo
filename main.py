class Stack:
    def __init__(self):
        self.left = ['(', '[', '{']
        self.right = [')', ']', '}']
        self.stack_list = []

    def is_empty(self):
        return bool(self.stack_list)

    def push(self, unit):
        self.stack_list.append(unit)

    def pop(self):
        return self.stack_list.pop()

    def peek(self):
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def check(self, str_):
        for symbol in str_:
            if symbol in self.left:
                self.push(symbol)
            elif symbol in self.right:
                if not self.is_empty():
                    return "Несбалансированно"
                if self.right.index(symbol) == self.left.index(self.pop()):
                    continue

                return "Несбалансированно"

        if not self.is_empty():
            return "Сбалансированно"


list_of_str = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]']
stack = Stack()
for st in list_of_str:
    res = stack.check(st)
    print(res)

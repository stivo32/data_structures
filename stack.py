class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.previous_node = None


class Stack:
    def __init__(self):
        self._top = None
        self._len = 0

    def push(self, value):
        new_node = Node(value)
        if self._top is None:
            self._top = new_node
        else:
            self._top.next_node = new_node
            new_node.previous_node = self._top
            self._top = new_node
        self._len += 1

    def pop(self):
        if self._top:
            value = self._top.value
            self._len -= 1
            if self._top.previous_node:
                self._top = self._top.previous_node
            else:
                self._top = None
            return value
        else:
            return None

    def peek(self):
        if self._top:
            return self._top.value
        else:
            return None

    def iter(self):
        current = self._top
        while current is not None:
            yield current.value
            current = current.previous_node

    def __len__(self):
        return self._len


def check_brackets(statement):
    stack = Stack()
    open_brackets = ['{', '[', '(']
    close_brackets = ['}', ']', ')']
    for symbol in statement:
        if symbol in open_brackets:
            stack.push(symbol)
        elif symbol in close_brackets:
            last = stack.pop()
            if last is None:
                return False
            if close_brackets.index(symbol) == open_brackets.index(last):
                continue
            return False
    if len(stack):
        return False
    return True


def main():
    st = '([])}{}{}'
    print(check_brackets(st))


if __name__ == '__main__':
    main()
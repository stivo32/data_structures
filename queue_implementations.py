class StackBasedQueue:
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []

    def enqueue(self, value):
        self.inbound_stack.append(value)

    def dequeue(self):
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
        return self.outbound_stack.pop()


class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.previous_node = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def __len__(self):
        return self.len

    def enqueue(self, value):
        new_node = Node(value)
        self.len += 1
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.previous_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node

    def dequeue(self):
        current = self.head
        if self.len == 1:
            self.head = None
            self.tail = None
            self.len -= 1
        elif self.len > 1:
            self.head = self.head.next_node
            self.head.previous_node = None
            self.len -= 1
        return current


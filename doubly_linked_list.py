from typing import Optional


class Node:
    def __init__(self, value, next_node=None, previous_node=None):
        self.value = value
        self.next_node = next_node
        self.previous_node = previous_node

    def __repr__(self):
        return f'{self.value}'


class LinkedListIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.current = iterable.head
        self.retval = None

    def __iter__(self):
        return self

    def __next__(self):
        while self.current is not None:
            self.retval, self.current = self.current, self.current.next_node
            return self.retval.value
        raise StopIteration()


class DoublyLinkedList:
    def __init__(self):
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None
        self._len: int = 0

    def append(self, value):
        new_node = Node(value=value)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.previous_node = self._tail
            self._tail.next_node = new_node
            self._tail = new_node
        self._len += 1

    @property
    def tail(self) -> Node:
        return self._tail

    @property
    def head(self) -> Node:
        return self._head

    def is_empty(self):
        return not self._len

    def __contains__(self, value):
        for node in self.__iter():
            if node.value == value:
                return True
        return False

    def __iter(self):
        current = self._head
        while current is not None:
            yield current
            current = current.next_node

    def __len__(self):
        return self._len

    def remove(self, value):
        if self.is_empty():
            return False
        if self._head.value == value:
            self._head = self._head.next_node
            self._head.previous_node = None
            self._len -= 1
            return True
        if self._tail.value == value:
            self._tail = self._tail.previous_node
            self._tail.next_node = None
            self._len -= 1
            return True
        current = self._head
        while current is not None:
            if current.value == value:
                previous_node = current.previous_node
                next_node = current.next_node
                previous_node.next_node = next_node
                next_node.previous_node = previous_node
                self._len -= 1
                return True
            current = current.next_node

    def __iter__(self):
        return LinkedListIterator(self)

    def __repr__(self):
        elements = []
        cur_node = self.head
        while cur_node is not None:
            elements.append(str(cur_node))
            cur_node = cur_node.next_node
        return f'[{", ".join(elements)}]'


def main():
    linked_list = DoublyLinkedList()
    linked_list.append(10)
    linked_list.append(8)
    linked_list.append(7)
    linked_list.push(11)
    print(linked_list)


if __name__ == '__main__':
    main()
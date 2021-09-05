from typing import Optional


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return f'{self.value}'


class LinkedListIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.current = iterable.head
        self.retval = None

    def __next__(self):
        while self.current is not None:
            self.retval, self.current = self.current, self.current.next_node
            return self.retval.value
        raise StopIteration()

    def __iter__(self):
        return self


class LinkedList:
    _head: Optional[Node] = None
    _tail: Optional[Node] = None
    _len: int = 0

    @property
    def tail(self) -> Node:
        return self._tail

    @property
    def head(self) -> Node:
        return self._head

    def __iter(self):
        current = self._head
        while current is not None:
            yield current
            current = current.next_node

    def __iter__(self) -> LinkedListIterator:
        return LinkedListIterator(self)

    def __contains__(self, value) -> bool:
        for node in self.__iter():
            if node.value == value:
                return True
        return False

    def append(self, value):
        new_node = Node(value=value)
        self._len += 1
        self._tail = new_node
        if self._head is None:
            self._head = new_node
            return
        cur_node = self._head
        while cur_node.next_node is not None:
            cur_node = cur_node.next_node
        cur_node.next_node = new_node

    def clear(self):
        self._head = None
        self._tail = None
        self._len = 0

    def remove(self, value) -> bool:
        """
        remove element by value
        :param value:
        :return:
        """
        cur_node = self._head
        prev_node = None

        while cur_node is not None:
            if cur_node.value == value:
                if prev_node is not None:
                    prev_node.next_node = cur_node.next_node
                    if cur_node.next_node is None:
                        self._tail = prev_node
                else:
                    self._head = cur_node.next_node
                    if self._head is None:
                        self._tail = None
                self._len -= 1
                return True
            prev_node, cur_node = cur_node, cur_node.next_node
        return False

    def __len__(self):
        return self._len

    def is_empty(self) -> bool:
        return not not self.__len__()

    def __repr__(self):
        elements = []
        cur_node = self.head
        while cur_node is not None:
            elements.append(str(cur_node))
            cur_node = cur_node.next_node
        return f'[{", ".join(elements)}]'


def main():
    linked_list = LinkedList()
    linked_list.append(5)
    linked_list.append(10)
    linked_list.append(5)
    linked_list.append(7)
    for el in linked_list:
        print(el)
    print(len(linked_list))
    print(linked_list)


if __name__ == '__main__':
    main()





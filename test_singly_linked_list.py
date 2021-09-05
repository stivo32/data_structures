from singly_linked_list import LinkedList


class TestSinglyLinkedList:
    def init(self):
        pass

    def test_add_value(self):
        linked_list = LinkedList()
        new_value = 10
        linked_list.append(new_value)
        assert len(linked_list) == 1
        assert linked_list.tail.value == new_value

    def test_add_first_element(self):
        linked_list = LinkedList()
        new_value = 10
        linked_list.append(new_value)
        assert linked_list.tail.value == linked_list.head.value == new_value

    def test_contain(self):
        linked_list = LinkedList()
        new_value = 10
        linked_list.append(new_value)
        assert new_value in linked_list

    def test_not_contain(self):
        linked_list = LinkedList()
        new_value = 10
        false_value = 11
        linked_list.append(new_value)
        assert false_value not in linked_list

    def test_clear(self):
        linked_list = LinkedList()
        new_value = 10
        linked_list.append(new_value)
        linked_list.clear()
        assert len(linked_list) == 0
        assert linked_list.head is None
        assert linked_list.tail is None


from doubly_linked_list import DoublyLinkedList


class TestSinglyLinkedList:
    def init(self):
        pass

    def test_add_value(self):
        linked_list = DoublyLinkedList()
        linked_list.append(1)
        linked_list.append(2)
        assert len(linked_list) == 2
        assert linked_list.tail.value == 2

    def test_add_first_element(self):
        linked_list = DoublyLinkedList()
        new_value = 10
        linked_list.append(new_value)
        assert linked_list.tail.value == linked_list.head.value == new_value

    def test_contain(self):
        linked_list = DoublyLinkedList()
        linked_list.append(10)
        assert 10 in linked_list
        assert 11 not in linked_list

    def test_not_contain(self):
        linked_list = DoublyLinkedList()
        new_value = 10
        false_value = 11
        linked_list.append(new_value)
        assert false_value not in linked_list

    def test_remove_element(self):
        linked_list = DoublyLinkedList()
        assert not linked_list.remove(1)
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)
        linked_list.append(5)
        assert linked_list.remove(1)
        assert linked_list.head.value == 2
        assert linked_list.remove(5)
        assert linked_list.tail.value == 4
        assert linked_list.remove(3)
        assert linked_list.head.next_node is linked_list.tail

    # def test_clear(self):
    #     linked_list = DoublyLinkedList()
    #     new_value = 10
    #     linked_list.append(new_value)
    #     linked_list.clear()
    #     assert len(linked_list) == 0
    #     assert linked_list.head is None
    #     assert linked_list.tail is None


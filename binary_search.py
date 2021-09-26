def binary_search_iterative(ordered_list: list, term: int) -> int:
    size = len(ordered_list) - 1
    first = 0
    last = size
    while first <= last:
        middle = (first + last) // 2
        if term == ordered_list[middle]:
            return middle
        if term > ordered_list[middle]:
            first = middle + 1
        else:
            last = middle - 1
    return -1


def binary_search_recursive(ordered_list: list, first_element_index: int, last_element_index: int, term: int) -> int:
    if last_element_index < first_element_index:
        return -1
    else:
        mid_point = first_element_index + ((last_element_index - first_element_index) // 2)

        if ordered_list[mid_point] > term:
            return binary_search_recursive(ordered_list, first_element_index, mid_point - 1, term)
        elif ordered_list[mid_point] < term:
            return binary_search_recursive(ordered_list, mid_point + 1, last_element_index, term)
        else:
            return mid_point


def main():
    array = [1, 3, 6, 8, 10, 12]
    print(binary_search_iterative(array, 12))
    print(binary_search_recursive(array, 0, len(array) - 1, 12))


if __name__ == '__main__':
    main()

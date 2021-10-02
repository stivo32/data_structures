def quick_select(array_list: list, left: int, right: int, k: int):
    split = partition(array_list, left, right)

    if split == k:
        return array_list[k]
    elif k > split:
        return quick_select(array_list, split + 1, right, k)
    else:
        return quick_select(array_list, left, split - 1, k)


def partition(array_list: list, first_index: int, last_index: int) -> int:
    if first_index == last_index:
        return first_index

    pivot = array_list[first_index]
    pivot_index = first_index
    index_of_last_element = last_index
    less_than_pivot_index = index_of_last_element
    bigger_than_pivot_index = first_index + 1

    while True:
        while bigger_than_pivot_index < last_index and array_list[bigger_than_pivot_index] < pivot:
            bigger_than_pivot_index += 1
        while less_than_pivot_index >= first_index + 1 and array_list[less_than_pivot_index] > pivot:
            less_than_pivot_index -= 1
        if less_than_pivot_index > bigger_than_pivot_index:
            (array_list[less_than_pivot_index],
             array_list[bigger_than_pivot_index]) = (array_list[bigger_than_pivot_index],
                                                     array_list[less_than_pivot_index])
        else:
            break
    (array_list[pivot_index],
     array_list[less_than_pivot_index]) = (array_list[less_than_pivot_index],
                                           array_list[pivot_index])
    return less_than_pivot_index


def main():
    array = [45, 23, 87, 12, 72, 4, 54, 32, 52]
    print(quick_select(array, 0, len(array) - 1, 3))


if __name__ == '__main__':
    main()
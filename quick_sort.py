from typing import Optional


def quick_sort_with_extra_memory(unsorted_list: list):
    if len(unsorted_list) < 2:
        return unsorted_list
    pivot = unsorted_list[0]
    less = [elem for elem in unsorted_list[1:] if elem <= pivot]
    greater = [elem for elem in unsorted_list[1:] if elem > pivot]
    return quick_sort_with_extra_memory(less) + [pivot] + quick_sort_with_extra_memory(greater)


def quick_sort_without_extra_memory(unsorted_list: list, first: int, last: int) -> Optional[int]:
    if last <= first:
        return
    partition_point = partition(unsorted_list, first, last)
    quick_sort_without_extra_memory(unsorted_list, first, partition_point - 1)
    quick_sort_without_extra_memory(unsorted_list, partition_point + 1, last)


def partition(unsorted_list: list, first_index: int, last_index: int):
    """
    Return pivot index in the list where all elements left to the pivot are less than pivot
    and all element right to the pivot are bigger
    :param unsorted_list: list
    :param first_index:  int
    :param last_index:  int
    :return pivot index: int
    """
    pivot = unsorted_list[first_index]
    pivot_index = first_index
    index_of_last_element = last_index

    less_than_pivot_index = index_of_last_element
    greater_than_pivot_index = first_index + 1

    while True:
        while unsorted_list[greater_than_pivot_index] < pivot and greater_than_pivot_index < last_index:
            greater_than_pivot_index += 1
        while unsorted_list[less_than_pivot_index] > pivot and less_than_pivot_index > first_index:
            less_than_pivot_index -= 1
        if greater_than_pivot_index < less_than_pivot_index:
            (unsorted_list[greater_than_pivot_index],
             unsorted_list[less_than_pivot_index]) = (unsorted_list[less_than_pivot_index],
                                                      unsorted_list[greater_than_pivot_index])
        else:
            break
    unsorted_list[pivot_index] = unsorted_list[less_than_pivot_index]
    unsorted_list[less_than_pivot_index] = pivot
    return less_than_pivot_index


def main():
    unsorted_list = [43, 3, 20, 4, 89, 77]
    sorted_array = quick_sort_with_extra_memory([*unsorted_list])
    quick_sort_without_extra_memory(unsorted_list, 0, len(unsorted_list) - 1)
    print(sorted_array)
    print(unsorted_list)


if __name__ == '__main__':
    main()

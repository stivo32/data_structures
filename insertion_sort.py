def insertion_sort(array: list) -> list:
    sorting_array = [*array]
    for i in range(1, len(sorting_array)):
        search_index = i
        insert_value = sorting_array[i]
        while search_index > 0 and sorting_array[search_index - 1] > insert_value:
            sorting_array[search_index] = sorting_array[search_index - 1]
            search_index -= 1
        sorting_array[search_index] = insert_value
    return sorting_array


def main():
    unsorted_list = [5, 1, 100, 2, 10]
    print(insertion_sort(unsorted_list))


if __name__ == '__main__':
    main()

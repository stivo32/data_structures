def selection_sort(unsorted_list: list) -> list:
    sorting_list = [*unsorted_list]
    size_of_list = len(sorting_list)

    for i in range(size_of_list):
        for j in range(i + 1, size_of_list):

            if sorting_list[j] < sorting_list[i]:
                sorting_list[i], sorting_list[j] = sorting_list[j], sorting_list[i]
    return sorting_list


def main():
    unsorted_list = [5, 1, 100, 2, 10]
    print(selection_sort(unsorted_list))


if __name__ == '__main__':
    main()

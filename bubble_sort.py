def bubble_sort(array: list) -> list:
    sorting_array = [*array]
    iterations = len(array) - 1
    for i in range(0, iterations):
        for j in range(0, iterations - i):
            if sorting_array[j] > sorting_array[j + 1]:
                sorting_array[j], sorting_array[j + 1] = sorting_array[j + 1], sorting_array[j]
    return sorting_array


def main():
    unsorted_array = [1, 8, 20, 6, 2]
    print(bubble_sort(unsorted_array))


if __name__ == '__main__':
    main()

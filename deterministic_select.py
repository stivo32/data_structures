def deterministic_select(array_list: list, left: int, right: int, k: int):
    split = partition(array_list, left, right)

    if split == k:
        return array_list[k]
    elif k > split:
        return deterministic_select(array_list, split + 1, right, k)
    else:
        return deterministic_select(array_list, left, split - 1, k)


def median_of_medians(elems: list) -> int:
    sublists = [elems[j:j+5] for j in range(0, len(elems), 5)]

    medians = []
    for sublist in sublists:
        medians.append(sorted(sublist)[len(sublist)//2])

    if len(medians) <= 5:
        return sorted(medians)[len(medians)//2]
    else:
        return median_of_medians(medians)


def get_index_of_nearest_median(array_list: list, first: int, second: int, median: int) -> int:
    if first == second:
        return first
    else:
        return first + array_list[first:second].index(median)


def partition(array_list: list, first_index: int, last_index: int) -> int:
    if first_index == last_index:
        return first_index
    nearest_median = median_of_medians(array_list[first_index: last_index])

    index_of_nearest_median = get_index_of_nearest_median(array_list, first_index, last_index, nearest_median)
    array_list[first_index], array_list[index_of_nearest_median] = array_list[index_of_nearest_median], array_list[first_index]
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
    print(deterministic_select(array, 0, len(array) - 1, 3))


if __name__ == '__main__':
    main()
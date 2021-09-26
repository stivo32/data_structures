def nearest_mid(input_list: list, lower_bound_index: int, upper_bound_index: int, search_value: int):
    return lower_bound_index + ((upper_bound_index - lower_bound_index) // (
            input_list[upper_bound_index] - input_list[lower_bound_index])) * (
                   search_value - input_list[lower_bound_index])


def interpolation_search(ordered_list: list, term: int):
    size = len(ordered_list) - 1
    first = 0
    last = size
    while first <= last:
        middle = nearest_mid(ordered_list, first, last, term)
        if middle < first or middle > last:
            return -1
        if term == ordered_list[middle]:
            return middle
        if term > ordered_list[middle]:
            first = middle + 1
        else:
            last = middle - 1
    return -1


def main():
    array = [44, 60, 75, 100, 120, 230, 250]
    print(interpolation_search(array, 230))


if __name__ == '__main__':
    main()

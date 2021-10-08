def merge_sort(unsorted_list: list) -> list:
    if len(unsorted_list) == 1:
        return unsorted_list
    mid_point = len(unsorted_list) // 2

    first_half = unsorted_list[:mid_point]
    second_half = unsorted_list[mid_point:]

    half_a = merge_sort(first_half)
    half_b = merge_sort(second_half)

    return merge(half_a, half_b)


def merge(first_sublist: list, second_sublist: list) -> list:
    i = j = 0
    first_len = len(first_sublist)
    second_len = len(second_sublist)
    merged_list = []

    while i < first_len and j < second_len:
        if (first := first_sublist[i]) < (second := second_sublist[j]):
            merged_list.append(first)
            i += 1
        else:
            merged_list.append(second)
            j += 1

    while i < first_len:
        merged_list.append(first_sublist[i])
        i += 1

    while j < second_len:
        merged_list.append(second_sublist[j])
        j += 1

    return merged_list


def main():
    print(merge_sort([6, 3, 8, 4, 2, 10, 15, 22, 1]))


if __name__ == '__main__':
    main()
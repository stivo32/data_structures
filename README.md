# Quickselect

The quickselect algorithm is used to obtain the kth smallest element in an unordered list of items, and is based on the
quicksort algorithm. in the case of the quickselect algorithm, we recursively call the function exclusively for the
sublist that has the kth smallest element. In the quickselect algorithm, we compare the index of the pivot point with
the k value to obtain the kth smallest element from the given unordered list.

# Deterministic select

The only different from quickselect is a way of choosing pivot index. Median_of_medians method used instead of just
getting first element of the list.
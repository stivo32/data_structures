# Searing algorithms

## Binary search

BS needs a sorted list to perform searching. It starts searching the item by dividing the given list by half. If the
search item is smaller than the middle value then it will look for the searched item only in the first half of the list,
and if the search item is greater than the middle value it will only look at the second half of the list. We repeat the
same process every time until we find the search item or we have checked the whole list.

## Interpolation search

The interpolation searching algorithm is an improved version of the binary search algorithm. In the interpolation search
algorithm, the starting search position is most likely to be the closest to the start or end of the list depending on
the search item. It is based on trying to make a good guess of the index position where a search item is likely to be
found in a sorted list of items.
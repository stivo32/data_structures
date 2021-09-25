from dataclasses import dataclass


@dataclass
class Heap:
    def __init__(self):
        self.heap: list[int] = [0]
        self.size: int = 0

    def insert(self, item: int):
        """
        3 steps:
         * Add new element to the end of the list
         * Increment size
         * Put element into right place
        """
        self.heap.append(item)
        self.size += 1
        self._arrange(self.size)

    def pop(self) -> int:
        """
        as heap root is min(max) element, pop it and put the last heap element as new root
        new root element sink to the right place of the heap
        """
        item = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self._sink(1)
        return item

    def _arrange(self, k: int):
        """
        chosen element move up till the right place
        """

    def _sink(self, k: int):
        """
        chosen element move down till the right place
        """


class MinHeap(Heap):
    def _arrange(self, k: int):
        """
        chosen element move up till the right place
        """
        while k // 2 > 0:
            if self.heap[k] < self.heap[k // 2]:
                self.heap[k], self.heap[k // 2] = self.heap[k // 2], self.heap[k]
            k //= 2

    def _minindex(self, k: int) -> int:
        if k * 2 + 1 > self.size:
            return k * 2
        if self.heap[k * 2] < self.heap[k * 2 + 1]:
            return k * 2
        return k * 2 + 1

    def _sink(self, k: int):
        """
        chosen element move down till the right place
        """
        while k * 2 <= self.size:
            mi = self._minindex(k)
            if self.heap[k] > self.heap[mi]:
                self.heap[k], self.heap[mi] = self.heap[mi], self.heap[k]
                k = mi


class MaxHeap(Heap):
    def _arrange(self, k: int):
        """
        chosen element move up till the right place
        """
        while k // 2 > 0:
            if self.heap[k] > self.heap[k // 2]:
                self.heap[k], self.heap[k // 2] = self.heap[k // 2], self.heap[k]
            k //= 2

    def _sink(self, k: int):
        """
        chosen element move down till the right place
        """
        while k * 2 < self.size:
            mi = self._maxindex(k)
            if self.heap[k] <= self.heap[mi]:
                self.heap[k], self.heap[mi] = self.heap[mi], self.heap[k]
            k = mi

    def _maxindex(self, k: int):
        if k * 2 + 1 > self.size:
            return k * 2
        if self.heap[k * 2] > self.heap[k * 2 + 1]:
            return k * 2
        return k * 2 + 1


def main():
    heap = MaxHeap()
    items = [4, 8, 7, 2, 9, 10, 5, 1, 3, 6]
    [heap.insert(item) for item in items]
    print(heap.heap)
    for i in range(3):
        n = heap.pop()
        print(n)
        print(heap.heap)


if __name__ == '__main__':
    main()

from dataclasses import dataclass


@dataclass
class Heap:
    def __init__(self):
        self.heap: list[int] = [0]
        self.size: int = 0

    def from_list(self, list_: list):
        [self.insert(item) for item in list_]

    def insert(self, item: int):
        """
        3 steps:
         * Add new element to the end of the list
         * Increment size
         * Put element into right place
        """
        self.heap.append(item)
        self.size += 1
        self._float(self.size)

    def pop(self):
        item = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self._sink(1)
        return item

    def _float(self, k: int):
        """
        chosen element move up till the right place
        """

    def _sink(self, k: int):
        """
        chosen element move down till the right place
        """


class MinHeap(Heap):
    def sort(self) -> list:
        sorted_list = []
        for _ in range(self.size):
            n = self.pop()
            sorted_list.append(n)
        return sorted_list

    def _float(self, k: int):
        """
        chosen element move up till the right place
        """
        while k // 2 > 0:
            if self.heap[k] < self.heap[k // 2]:
                self.heap[k], self.heap[k // 2] = self.heap[k // 2], self.heap[k]
            k //= 2

    def minchild(self, k):
        if k * 2 + 1 > self.size:
            return k * 2
        elif self.heap[k*2] < self.heap[k*2+1]:
            return k * 2
        else:
            return k * 2 + 1

    def _sink(self, k: int):
        """
        chosen element move down till the right place
        """
        while k * 2 <= self.size:
            mi = self.minchild(k)
            if self.heap[k] > self.heap[mi]:
                self.heap[k], self.heap[mi] = self.heap[mi], self.heap[k]
            k = mi


def main():
    h = MinHeap()
    h.from_list([4, 8, 7, 2, 9, 10, 5, 1, 3, 6])
    print(h.heap)
    print(h.sort())


if __name__ == '__main__':
    main()
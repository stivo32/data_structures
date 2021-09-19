from typing import List, Optional


class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self):
        self.size = 20
        self.slots: List[Optional[HashItem]] = [None] * self.size
        self.count = 0

    def __setitem__(self, key, value):
        return self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def _hash(self, key):
        hv = 0
        for i, ch in enumerate(key, start=1):
            hv += ord(ch) * i
        return hv % self.size

    def put(self, key, value):
        # hash collision fixing method -> linear probing
        item = HashItem(key, value)
        h = self._hash(key)
        while self.slots[h] is not None:
            if self.slots[h].key == key:
                break
            h = (h + 1) % self.size
        if self.slots[h] is None:
            self.count += 1
        self.slots[h] = item

    def get(self, key):
        h = self._hash(key)
        while self._hash(key) is not None:
            if self.slots[h].key == key:
                return self.slots[h].value
            else:
                h = (h + 1) % self.size
        return None


def main():
    hash_table = HashTable()
    hash_table['good'] = 'eggs'
    hash_table['better'] = 'ham'
    hash_table['best'] = 'spam'
    hash_table['ad'] = 'do not'
    hash_table['ga'] = 'collide'
    for key in ["good", 'better','best', 'ad', 'ga']:
        print(hash_table[key])


if __name__ == '__main__':
    main()

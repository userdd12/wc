# Min head data structure
# with decrease key functionality - in O(log(n)) time


class Node:
    def __init__(self, val, name):
        self.val = val
        self.name = name

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.val < other.val


class MinHeap:
    """
    >>> r = Node(-1, "R")
    >>> b = Node(6, "B")
    >>> a = Node(3, "A")
    >>> x = Node(1, "X")
    >>> e = Node(4, "E")
    >>> myMinHeap = MinHeap([r, b, a, x, e])
    >>> myMinHeap.decrease_key(b, -17)
    """

    def __init__(self, array):
        self.idx_of_element = {}
        self.heap = self.build_heap(array)

    def get_parent_idx(self, idx):
        return (idx - 1) // 2

    def get_left_child_idx(self, idx):
        return idx * 2 + 1

    def get_right_child_idx(self, idx):
        return idx * 2 + 2

    def build_heap(self, array):
        lastIdx = len(array) - 1
        startFrom = self.get_parent_idx(lastIdx)

        for idx, i in enumerate(array):
            self.idx_of_element[i] = idx

        for i in range(startFrom, -1, -1):
            self.sift_down(i, array)
        return array

    # this is min-heapify method
    def sift_down(self, idx, array):
        while True:
            l = self.get_left_child_idx(idx)
            r = self.get_right_child_idx(idx)

            smallest = idx
            if l < len(array) and array[l] < array[idx]:
                smallest = l
            if r < len(array) and array[r] < array[smallest]:
                smallest = r

            if smallest != idx:
                array[idx], array[smallest] = array[smallest], array[idx]
                self.idx_of_element[array[idx]], self.idx_of_element[
                    array[smallest]
                ] = (
                    self.idx_of_element[array[smallest]],
                    self.idx_of_element[array[idx]],
                )
                idx = smallest
            else:
                break

    def sift_up(self, idx):
        p = self.get_parent_idx(idx)
        while p >= 0 and self.heap[p] > self.heap[idx]:
            self.heap[p], self.heap[idx] = self.heap[idx], self.heap[p]
            self.idx_of_element[self.heap[p]], self.idx_of_element[self.heap[idx]] = (
                self.idx_of_element[self.heap[idx]],
                self.idx_of_element[self.heap[p]],
            )
            idx = p
            p = self.get_parent_idx(idx)

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.idx_of_element[self.heap[0]], self.idx_of_element[self.heap[-1]] = (
            self.idx_of_element[self.heap[-1]],
            self.idx_of_element[self.heap[0]],
        )

        x = self.heap.pop()
        del self.idx_of_element[x]
        self.sift_down(0, self.heap)
        return x

    def insert(self, value):
        self.heap.append(value)
        self.idx_of_element[value] = len(self.heap) - 1
        self.sift_up(len(self.heap) - 1)

    def is_empty(self):
        return True if len(self.heap) == 0 else False

    def decrease_key(self, key, newValue):
        assert (
            self.heap[self.idx_of_element[key]].val > newValue
        ), "newValue must be less that current value"
        key.val = newValue
        self.sift_up(self.idx_of_element[key])


## USAGE

r = Node(-1, "R")
b = Node(6, "B")
a = Node(3, "A")
x = Node(1, "X")
e = Node(4, "E")

# Use one of these two ways to generate Min-Heap

# Generating Min-Heap from array
myMinHeap = MinHeap([r, b, a, x, e])

# Generating Min-Heap by Insert method
# myMinHeap.insert(a)
# myMinHeap.insert(b)
# myMinHeap.insert(x)
# myMinHeap.insert(r)
# myMinHeap.insert(e)

# Before
print("Min Heap - before decrease key")
for i in myMinHeap.heap:
    print(i, i.val)

print("Min Heap - After decrease key of node [B -> -17]")
myMinHeap.decrease_key(b, -17)

# After
for i in myMinHeap.heap:
    print(i, i.val)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

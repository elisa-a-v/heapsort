import unittest
from Heap import Heap


class TestHeap(unittest.TestCase):
    def setUp(self) -> None:
        self.heapq = Heap([[4, "hola"], [1, "chao"], [3, "qué tal"], [2, "ACAB"], [16, "Todd"], [9, "???"], [10, ":B"]])

    def test_HeapSize(self):
        self.assertEqual(self.heapq.size, 7)

    def test_BuildMaxHeap(self):
        self.heapq.buildmaxheap()
        for i in range(0, self.heapq.size, 1):
            if 2*i + 1 < self.heapq.size:
                self.assertGreaterEqual(self.heapq.array[i], self.heapq.get_left(i))
            if 2*i + 2 < self.heapq.size:
                self.assertGreaterEqual(self.heapq.array[i], self.heapq.get_right(i))

    def test_heapsort(self):
        self.heapq.heapsort()
        arr1 = [18, 123, 1, 21, -3, 7]
        arr2 = [-18, 13, 1, 21, -3, 7]
        heap1 = Heap(arr1)
        heap2 = Heap(arr2)
        heap1.heapsort()
        heap2.heapsort()
        self.assertEqual(heap1.array, sorted(arr1))
        self.assertEqual(heap2.array, sorted(arr2))
        lista = [[4, "hola"], [1, "chao"], [3, "qué tal"], [2, "ACAB"], [16, "Todd"], [9, "???"], [10, ":B"]]
        lista.sort()
        self.assertEqual(self.heapq.array, lista)


if __name__ == '__main__':
    unittest.main()

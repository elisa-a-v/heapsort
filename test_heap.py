import unittest
from Heap import Heap


class TestHeap(unittest.TestCase):
    def setUp(self) -> None:
        self.heap = Heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])

    def test_HeapSize(self):
        self.assertEqual(self.heap.size, 10)

    def test_BuildMaxHeap(self):
        self.heap.buildmaxheap()
        for i in range(0, self.heap.size, 1):
            if 2*i + 1 < self.heap.size:
                self.assertGreaterEqual(self.heap.array[i], self.heap.get_left(i))
            if 2*i + 2 < self.heap.size:
                self.assertGreaterEqual(self.heap.array[i], self.heap.get_right(i))

    def test_heapsort(self):
        self.heap.heapsort()
        arr1 = [18, 123, 1, 21, -3, 7]
        arr2 = [-18, 13, 1, 21, -3, 7]
        heap1 = Heap(arr1)
        heap2 = Heap(arr2)
        heap1.heapsort()
        heap2.heapsort()
        self.assertEqual(heap1.array, sorted(arr1))
        self.assertEqual(heap2.array, sorted(arr2))
        lista = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        lista.sort()
        self.assertEqual(self.heap.array, lista)


if __name__ == '__main__':
    unittest.main()

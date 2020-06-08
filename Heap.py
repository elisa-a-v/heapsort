class Heap:
    def __init__(self, array):
        self.array = array
        self.size = len(self.array)

    def get_size(self):
        return self.size

    def get_left(self, i):
        if 2*i + 1 < self.size:
            return self.array[2*i + 1]

    def get_right(self, i):
        if 2*i + 2 < self.size:
            return self.array[2*i + 2]

    def swap(self, a, b):
        self.array[a], self.array[b] = self.array[b], self.array[a]

    def maxheapify(self, i):
        left = 2*i + 1
        right = 2*i + 2
        if left < self.size and self.array[left] > self.array[i]:
            largest = left
        else:
            largest = i
        if right < self.size:
            if self.array[right] > self.array[largest]:
                largest = right
        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.maxheapify(largest)

    def get(self, param):
        return self.array[param]

    def buildmaxheap(self):
        for i in range(int(self.size/2)-1, -1, -1):
            self.maxheapify(i)

    def heapsort(self):
        aux = self.size-1
        self.buildmaxheap()
        for i in range(aux, 0, -1):
            self.swap(i, 0)
            self.size -= 1
            self.maxheapify(0)

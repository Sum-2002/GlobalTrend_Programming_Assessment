class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        """Insert a value into the max heap"""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def delete(self):
        """Delete the maximum value from the max heap"""
        if not self.heap:
            return None
        max_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return max_value

    def get_max(self):
        """Return the maximum value from the max heap"""
        if not self.heap:
            return None
        return self.heap[0]

    def _heapify_up(self, index):
        """Maintain the max heap property by bubbling up the value at the given index"""
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index] >= self.heap[index]:
                break
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            index = parent_index

    def _heapify_down(self, index):
        """Maintain the max heap property by bubbling down the value at the given index"""
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            largest = index
            if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
                largest = left_child_index
            if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
                largest = right_child_index
            if largest == index:
                break
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            index = largest
heap = MaxHeap()
heap.insert(5)
heap.insert(3)
heap.insert(8)
heap.insert(1)
print(heap.get_max())  
print(heap.delete())
print(heap.get_max())

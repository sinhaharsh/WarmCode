"""
Min Heap implementation in Python
"""
class MinHeap:
    def __int__(self):
        """
        heap_list : initialized with a value 0
        current_size : size of the heap
        :return:
        """
        self.heap_list = [0]
        self.current_size = 0

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.percolateUp(self.current_size)

    def percolateUp(self, i):
        """
        Percolates a new item as far up in the tree as it needs to go to maintain the heap property
        :param i: index of element inserted at the end of the heap list
        :return: None
        """
        # Find the parent, until reach the root
        while i//2 > 0:
            # If the child is smaller than the parent, swap it
            if self.heap_list[i] < self.heap_list[i//2]:
                self.heap_list[i//2], self.heap_list[i] = self.heap_list[i], self.heap_list[i//2]
            i = i//2

    def percolateDown(self, i):
        # While child exists
        while (i*2) <= self.current_size:
            min_child = self.minChild(i)
            # And if parent is greater than child, swap it
            if self.heap_list[i] > self.heap_list[min_child]:
                self.heap_list[i], self.heap_list[min_child] = self.heap_list[min_child], self.heap_list[i]
            i = min_child

    def minChild(self, i):
        """
        select minimum child among the two children
        :param i: parent index
        :return: child index with the minimum value
        """
        if i*2 + 1 > self.current_size:
            return i*2
        else:
            if self.heap_list[i*2] < self.heap_list[i*2 + 1]:
                return i*2
            else:
                return i*2 + 1

    def delMin(self):
        """
        Get minimum value, and delete it from heap
        :return:
        """
        root_value = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.percolateDown(1)
        return root_value

    def buildHeap(self, values):
        i = len(values)//2
        self.current_size = len(values)
        self.heap_list = [0]+values.copy()
        while (i>0):
            self.percolateDown(i)
            i = i-1
class MinHeap:
    """
    This Binary Minimum Heap function will use an array to represent itself.

    Instead of implementing a binary tree class, we devise an indexing system in an array
    where we can identify the parent/child based on the index of the elements. Watch video
    to get visual explanation:

    https://www.youtube.com/watch?v=t0Cq6tVNRBA
    """

    def __init__(self, input_list, comparison_index=None):
        # Typically, we'll have to specify the length of the array, and increase capacity
        # as needed. We won't be doing that since python list can dynamically change size.
        self.heap = []
        # If the user specified comparison_index, it means the elements we receive should be
        # iterable. We'll use that specific element to make our comparison to maintain
        # minimum heap variance...
        # Ex: [(1, 3), (2, 1)] list uses comparison_index=0 to maintain order
        self.comparison_index = comparison_index

        for item in input_list:
            self.add(item)

    # Helpers for getting selected element's parent/child index:
    @staticmethod
    def _getLeftChildIndex(parentIndex):
        return 2 * parentIndex + 1

    @staticmethod
    def _getRightChildIndex(parentIndex):
        return 2 * parentIndex + 2

    @staticmethod
    def _getParentIndex(childIndex):
        return (childIndex - 1) // 2

    # Helpers to determine whether we are reaching out of bounds
    # (does our current index/node have a parent/child?):
    def _hasLeftChild(self, index):
        return self._getLeftChildIndex(index) < len(self.heap)

    def _hasRightChild(self, index):
        return self._getRightChildIndex(index) < len(self.heap)

    def _hasParent(self, index):
        return self._getParentIndex(index) >= 0

    # Helpers to get the comparison value of parent/child:
    def _currentNode(self, index):
        if self.comparison_index:
            return self.heap[index][self.comparison_index]

        return self.heap[index]

    def _leftChild(self, index):
        if self.comparison_index:
            return self.heap[self._getLeftChildIndex(index)][self.comparison_index]

        return self.heap[self._getLeftChildIndex(index)]

    def _rightChild(self, index):
        if self.comparison_index:
            return self.heap[self._getRightChildIndex(index)][self.comparison_index]

        return self.heap[self._getRightChildIndex(index)]

    def _parent(self, index):
        if self.comparison_index:
            return self.heap[self._getParentIndex(index)][self.comparison_index]

        return self.heap[self._getParentIndex(index)]

    def _swap(self, firstIndex, secondIndex):
        """
        Swapping two array elements using Python's tuple:
        """
        self.heap[firstIndex], self.heap[secondIndex] = self.heap[secondIndex], self.heap[firstIndex]
        return None

    def peek(self):
        """
        Returns the first (root) element value.
        """
        if not self.heap:
            raise IndexError("Heap does not contain any elements!")

        return self.heap[0]

    def poll(self):
        """
        Pops the root, and re-organizes MinHeap using the last leaf node.
        Use heapify down to bubble down the current root node to correct position.
        """
        if not self.heap:
            raise IndexError("Heap does not contain any elements!")

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapifyDown()
        return root

    def add(self, item):
        """
        Appends new value at the end of the heap array, and re-organizes the MinHeap.
        Use heapify up to bubble up the newly added leaf node to correct position.
        """
        self.heap.append(item)
        self._heapifyUp()

    def _heapifyUp(self):
        """
        Bubbles up the newly appended leaf node to correct position. While loop will continue
        bubbling up until the parent node is no longer greater than leaf node (or until we
        can't bubble up anymore as per first condition)
        """
        index = len(self.heap) - 1
        while self._hasParent(index) and self._parent(index) > self._currentNode(index):
            self._swap(self._getParentIndex(index), index)
            index = self._getParentIndex(index)

        return None

    def _heapifyDown(self):
        """
        Bubbles down the root node to correct position.
        """
        index = 0

        while self._hasLeftChild(index):

            # Get the index of the smaller child:
            smallerChildIndex = self._getLeftChildIndex(index)
            smallerChild = self._leftChild(index)
            if self._hasRightChild(index) and self._rightChild(index) < self._leftChild(index):
                smallerChildIndex = self._getRightChildIndex(index)
                smallerChild = self._rightChild(index)

            # Check if MinHeap order is maintained. If yes, break out of while loop
            if self._currentNode(index) < smallerChild:
                break
            # Otherwise, swap current index element with smaller child:
            else:
                self._swap(index, smallerChildIndex)

            # Continue bubbling up...
            index = smallerChildIndex

        return None


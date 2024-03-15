

class MinHeap:
    """
    This Binary Minimum Heap function will use an array to represent itself.

    The implementation is clearly explained in this youtube video:
    https://www.youtube.com/watch?v=t0Cq6tVNRBA

    Instead of implementing a binary tree, we devise an indexing system in an array 
    where we can identify the parent/child based on
    """

    def __init__(self):
        
        # Typically, we'll have to specify the length of the array, and increase capacity
        # as needed. We won't be doing that since python list can dynamically change size.
        self.heap = []

    def _getLeftChildIndex(self, parentIndex):
        return 2 * parentIndex + 1

    def _getRightChildIndex(self, parentIndex):
        return 2 * parentIndex + 2

    def _getParentIndex(self, childIndex):
        return (childIndex - 1) // 2


    def _hasLeftChild(self, index):
        return self._getLeftChildIndex(index) < len(self.heap)

    def _hasRightChild(self, index):
        return self._getRightChildIndex(index) < len(self.heap)

    def _hasParent(self, index):
        return self._getParentIndex(index) >= 0


    def _leftChild(self, index):
        return self.heap[self._getLeftChildIndex(index)]

    def _rightChild(self, index):
        return self.heap[self._getRightChildIndex(index)]

    def _parent(self, index):
        return self.heap[self._getParentIndex(index)]
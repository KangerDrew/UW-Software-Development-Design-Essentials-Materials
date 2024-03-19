from MinHeap import MinHeap


def test_MinHeapCreation():

    testArr = [6, 2, 1]

    # Creating heap using the above array should go something like this:

    # First element gets added. No major updates.
    # Second element gets added. This will get heapified up to the root.
    # Third elements get added, this will get heapified up, where it swaps its position
    # from right child of the root to the root.

    # Expected MinHeap Structure:
    #          1
    #        /   \
    #       6     2

    test_heap = MinHeap(testArr)
    assert test_heap.heap == [1, 6, 2]


def test_MinHeapCreation2():

    testArr = [1, 2, 3, 4, 5, 6]

    # Since the input is already sorted, there shouldn't be any heapifying up/down occuring.

    # Expected MinHeap Structure:
    #          1
    #        /   \
    #       2     3
    #      / \   /
    #     4   5 6

    test_heap = MinHeap(testArr)
    assert test_heap.heap == [1, 2, 3, 4, 5, 6]


def test_MinHeapPeek():
    testArr = [1, 2, 3, 4, 5, 6]
    test_heap = MinHeap(testArr)

    assert test_heap.peek() == 1
    assert len(test_heap.heap) == 6


def test_MinHeapPoll():
    testArr = [1, 2, 3, 4, 5, 6]
    test_heap = MinHeap(testArr)

    assert test_heap.poll() == 1
    assert len(test_heap.heap) == 5
    assert test_heap.peek() == 2

    # After polling, 6 should get replaced in the root, then bubbled down using heapifyDown.

    # Expected MinHeap Structure:
    #          2
    #        /   \
    #       4     3
    #      / \
    #     6   5

    assert test_heap.heap == [2, 4, 3, 6, 5]

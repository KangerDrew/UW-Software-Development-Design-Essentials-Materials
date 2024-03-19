from collections import defaultdict
from MinHeap import MinHeap

# Assume undirected, but weighted graph.
# See assignment page for visual graph.
# (node1, node2, weight)


def adjacencyDictionaryCreator(edgeList):
    """
    Takes edge list and converts it to adjacency dictionary (I'll use dictionary, incase
    the user wants to use a specific name for a given node)
    """

    # We can use Python's defaultdict to set the default value as a list (easy to append
    # new values to a list without writing extra lines of code...)
    adjacencyDict = defaultdict(list)

    # Assume edgeList element are set such that - (node1, node2, weight)
    for node1, node2, weight in edgeList:

        adjacencyDict[node1].append((node2, weight))
        adjacencyDict[node2].append((node1, weight))

    return adjacencyDict


def shortestPath(adjacencyList, source, target):
    """
    This is an implementation of Dijkstra's Shortest Path Algorithm. This function will use BFS,
    combined with minimum heap to perform the traversal. BFS scans the neighboring nodes, and minimum
    heap allows us to keep track of the shortest path (regardless of the target). This allows us to
    traverse the path of least resistance first, which in turn will give us the shortest path to all
    the nodes that can be reached by the source.
    """
    # Initialize a dictionary (hash map) that will keep track of all the nodes
    # reached, as well as the shortest path to that node from source:
    shortest_path = {}

    # Create a priority queue (minimum heap) that contains a single element - (original_node, distance)
    # original_node is our starting point, A.K.A our source. Since this is the starting point, the distance
    # should be zero:

    # comparison_index should be 1, as we're using the 2nd input of each element "distance" to weigh our
    # minimum heap variance:
    heap = MinHeap([(source, 0)], comparison_index=1)

    while heap:

        # Pop the path to the node with the shortest travel distance:
        current_node, distance = heap.poll()

        # Check to see if current_node has already been recorded by "shortest" dictionary.
        if current_node in shortest_path:
            # If yes, the shortest path to next_node should already be recorded. Skip and
            # move onto the next node in the MinHeap!
            continue

        # If current_node is target, that means we've found the shortest path:
        if current_node == target:
            return distance

        # Otherwise, this is the first time we've discovered current_node. Because of the
        # minimum heap variance, this should be the shortest path possible from the source
        # to the current node:
        shortest_path[current_node] = distance

        # Then, add the neighboring nodes, along with the distance it would take to travel
        # from current_node to the minimum heap:
        for next_node, next_distance in adjacencyList[current_node]:

            # Only add onto the heap if it doesn't exist in shortest path:
            if next_node not in shortest_path:
                heap.add((next_node, next_distance + distance))

    # If the above while loop exits without returning, it means the node is un-reachable.
    # Return null element to let the user know that shortest path doesn't exist between
    # source and target!
    return None

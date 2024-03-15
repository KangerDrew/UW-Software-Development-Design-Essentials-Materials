
# Assume undirected, but weighted graph.
# See assignment page for visual graph.
# (node1, node2, weight)

data = [
    (1, 2, 7),
    (1, 3, 9),
    (1, 6, 14),
    (2, 3, 10),
    (2, 4, 15),
    (3, 6, 2),
    (3, 4, 11),
    (4, 5, 6),
    (5, 6, 9)
    ]


class ShortestPath:


    def __init__(self):
        
        self.minHeap = []
        pass
from ShortestPath import adjacencyDictionaryCreator, shortestPath

# Data below is the edge list representation of the .gif file in the class assignment page
# (also on wikipedia entry for Dijkstra's algorithm):
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


def test_adjacencyDictionaryCreator():

    adjDic = adjacencyDictionaryCreator(data)
    assert adjDic == {1: [(2, 7), (3, 9), (6, 14)],
                      2: [(1, 7), (3, 10), (4, 15)],
                      3: [(1, 9), (2, 10), (6, 2), (4, 11)],
                      4: [(2, 15), (3, 11), (5, 6)],
                      5: [(4, 6), (6, 9)],
                      6: [(1, 14), (3, 2), (5, 9)]
                      }


def test_shortest_paths():

    adjDic = adjacencyDictionaryCreator(data)

    assert shortestPath(adjDic, 1, 3) == 9  # The obvious path, go directly to node 3.
    assert shortestPath(adjDic, 1, 6) == 11  # Not so obvious path, go to node 3 then 6!
    assert shortestPath(adjDic, 1, 2) == 7  # Another obvious path, go directly to node 2.

    assert shortestPath(adjDic, 2, 5) == 21  # Go to node 4, then 5.
    assert shortestPath(adjDic, 2, 6) == 12  # Go to node 3 then 6.

    assert shortestPath(adjDic, 1, 5) == 20
    assert shortestPath(adjDic, 1, 5) == shortestPath(adjDic, 5, 1)

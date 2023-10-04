from collections import defaultdict


def is_bipartite(gph: defaultdict[int, list[int]]) -> bool:
    """
    Check whether a graph is Bipartite or not using Depth-First Search (DFS).

    A Bipartite Graph is a graph whose vertices can be divided into two independent
    sets, U and V such that every edge (u, v) either connects a vertex from
    U to V or a vertex from V to U. In other words, for every edge (u, v),
    either u belongs to U and v to V, or u belongs to V and v to U. There is
    no edge that connects vertices of the same set.

    Args:
        graph: An adjacency list representing the graph.

    Returns:
        True if there's no edge that connects vertices of the same set, False otherwise.

    Examples:
        >>> gph1 = defaultdict(list, {0: [1, 2], 1: [0, 3], 2: [0, 4], 3: [1], 4: [2]})
        >>> is_bipartite(gph1)
        True

        >>> gph2 = defaultdict(list, {0: [1, 2], 1: [0, 2], 2: [0, 1]})
        >>> is_bipartite(gph2)
        False
    """

    def dpth(node, col):
        vis[node] = col
        return any(
            vis[nbor] == col or (vis[nbor] == -1 and not dpth(nbor, 1 - col))
            for nbor in gph[node]
        )

    vis: defaultdict[int, int] = defaultdict(lambda: -1)

    return all(not (vis[node] == -1 and not dpth(node, 0)) for node in gph)


if __name__ == "__main__":
    import doctest

    result = doctest.testmod()

    if result.failed == 0:
        print("All tests passed!")
    else:
        print(f"{result.failed} test(s) failed.")

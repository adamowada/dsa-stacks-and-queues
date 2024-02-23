class Vertex:
    """A Vertex in a graph."""

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.value}"


class Edge:
    """An Edge connecting two vertices in a graph, with an optional weight."""

    def __init__(self, vertex, weight=None):
        self.vertex = vertex
        self.weight = weight

    def __repr__(self):
        return f"Edge to {self.vertex}{f' with weight {self.weight}' if self.weight else '' }"


class Graph:
    """A graph implemented using an adjacency list."""

    def __init__(self):
        self.adjacency_list = {}

    def __str__(self):
        return f"Graph {self.adjacency_list}"

    def add_node(self, value):
        """Add a new vertex to the graph."""
        vertex = Vertex(value)
        self.adjacency_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=1):
        """Add a directed edge from start_vertex to end_vertex."""
        if start_vertex not in self.adjacency_list or end_vertex not in self.adjacency_list:
            raise KeyError("Both vertices must exist in the graph.")
        edge = Edge(end_vertex, weight)
        self.adjacency_list[start_vertex].append(edge)

    def get_nodes(self):
        """Return a collection of all vertices in the graph."""
        return list(self.adjacency_list.keys())

    def get_neighbors(self, vertex):
        """Return a collection of edges connected to the given vertex."""
        return self.adjacency_list[vertex]

    def size(self):
        """Return the number of vertices in the graph."""
        return len(self.adjacency_list)


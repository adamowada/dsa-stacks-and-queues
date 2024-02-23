class Vertex:
    """A Vertex in a graph."""

    def __init__(self, value: object) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"Vertex(\"{self.value}\")"


class Edge:
    """An Edge connecting two vertices in a graph, with an optional weight."""

    def __init__(self, vertex: Vertex, weight: int = None) -> None:
        self.vertex = vertex
        self.weight = weight

    def __repr__(self) -> str:
        return f"Edge({self.vertex}, {self.weight})"


class Graph:
    """A graph implemented using an adjacency list."""

    def __init__(self) -> None:
        # Each key is a Vertex(), each value is a list of Edge() instances representing neighbors
        self.adjacency_list = {}

    def __repr__(self):
        return f"Graph({self.adjacency_list})"

    def add_node(self, value):
        """
        Add a new vertex to the graph.

        :param value: Value of new Vertex.
        :return: Instance of created Vertex.
        """

        # Create a new vertex
        vertex = Vertex(value)

        # Add the vertex to the dictionary, empty list because new vertices don't have neighbors
        self.adjacency_list[vertex] = []

        # Return a reference to the vertex instance
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=None):
        """
        Add a directed edge from start_vertex to end_vertex.

        :param start_vertex: Vertex in graph.
        :param end_vertex: Vertex in graph.
        :param weight: Optional weight.
        :return: None.
        """

        # Error handling if the start or end vertex aren't in the graph
        if start_vertex not in self.adjacency_list or end_vertex not in self.adjacency_list:
            raise KeyError("Both vertices must exist in the graph.")

        # Create new edge instance
        edge = Edge(end_vertex, weight)

        # Add the edge to the vertex's neighbors list
        self.adjacency_list[start_vertex].append(edge)

    def get_nodes(self) -> list[Vertex]:
        """
        Return a collection of all vertices in the graph.

        :return: List of Vertex instances.
        """

        return list(self.adjacency_list.keys())

    def get_neighbors(self, vertex) -> list[Edge]:
        """
        Return a collection of edges connected to the given vertex.

        :param vertex: Target Vertex.
        :return: List of Edge instances, representing the Vertex's neighbors.
        """

        return self.adjacency_list[vertex]

    def size(self) -> int:
        """
        Return the number of vertices in the graph.

        :return: Number of Vertex instances in the graph.
        """

        return len(self.adjacency_list)


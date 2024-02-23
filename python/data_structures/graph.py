class Graph:
    def __init__(self):
        # Each key is a Vertex(), each value is a list of Edge() instances representing neighbors that vertex
        # can visit
        self.adjacency_list = {}

    def add_node(self, value):
        """
        Add a new vertex to the graph.

        :param value: Value of new Vertex.
        :return: Instance of created Vertex.
        """

        # create a new vertex
        vertex = Vertex(value)

        # add vertex to dictionary
        self.adjacency_list[vertex] = []

        # return a reference to the newly created vertex
        return vertex

    def size(self):
        """
        Return the number of vertices in the graph by getting the length of the Graph's adjacency_list.

        :return: Int representing the number of Vertex instances in the graph.
        """

        return len(self.adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight=None):
        """
        Add a directed edge from start_vertex to end_vertex.

        :param start_vertex: Vertex in graph.
        :param end_vertex: Vertex in graph.
        :param weight: Optional weight.
        :return: None.
        """

        # error handling if either vertex is not in the graph
        if start_vertex not in self.adjacency_list or end_vertex not in self.adjacency_list:
            raise KeyError("Both vertices must be in the graph.")

        # create a new edge
        edge = Edge(end_vertex, weight)

        # add the edge to starting vertex's neighbors list inside the adjacency_list
        self.adjacency_list[start_vertex].append(edge)

    def __repr__(self):
        return f"Graph({self.adjacency_list})"

    def get_neighbors(self, vertex):
        """
        Return a collection of edges connected to the given vertex.

        :param vertex: Target Vertex.
        :return: List of Edge instances, representing the Vertex's neighbors.
        """
        pass

    def get_nodes(self):
        """
        Return a collection of all vertices in the graph.

        :return: List of Vertex instances.
        """
        pass


class Vertex:
    """An Edge connecting two vertices in a graph, with an optional weight."""

    def __init__(self, value):
        self.value = value

    def __repr__(self) -> str:
        return f"Vertex(\"{self.value}\")"


class Edge:
    """An Edge connecting two vertices in a graph, with an optional weight."""

    def __init__(self, vertex, weight=None):
        self.vertex = vertex
        self.weight = weight

    def __repr__(self) -> str:
        return f"Edge({self.vertex}, {self.weight})"

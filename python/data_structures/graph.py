class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        # create a new vertex
        vertex = Vertex(value)

        # add vertex to dictionary
        self.adjacency_list[vertex] = []

        # return a reference to the newly created vertex
        return vertex

    def size(self):
        return len(self.adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight=None):
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
        pass

    def get_nodes(self):
        pass


class Vertex:
    def __init__(self, value):
        self.value = value

    def __repr__(self) -> str:
        return f"Vertex(\"{self.value}\")"


class Edge:
    def __init__(self, vertex, weight=None):
        self.vertex = vertex
        self.weight = weight

    def __repr__(self) -> str:
        return f"Edge({self.vertex}, {self.weight})"

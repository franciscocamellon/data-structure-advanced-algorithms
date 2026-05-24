


class GraphAdjList:
    def __init__(self):
        self.adj = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj:
            self.adj[vertex] = []

    def add_edge(self, u, v, directed=False):
        self.add_vertex(u)
        self.add_vertex(v)

        if v not in self.adj[u]:
            self.adj[u].append(v)

        if not directed:
            if u not in self.adj[v]:
                self.adj[v].append(u)

    def has_edge(self, u, v):
        if u not in self.adj:
            return False
        return v in self.adj[u]

    def print_adj_list(self):
        for vertex in sorted(self.adj):
            print(vertex, "->", sorted(self.adj[vertex]))

    def vertices(self):
        return list(self.adj.keys())

    def to_mermaid(self, directed=False):
        if directed:
            connector = "-->"
        else:
            connector = "---"

        lines = ["graph TD"]
        used_edges = set()

        for u in sorted(self.adj):
            if len(self.adj[u]) == 0:
                lines.append("    " + u)

            for v in sorted(self.adj[u]):
                if directed:
                    lines.append("    " + u + " " + connector + " " + v)
                else:
                    edge = tuple(sorted([u, v]))
                    if edge not in used_edges:
                        used_edges.add(edge)
                        lines.append("    " + u + " " + connector + " " + v)

        return "\n".join(lines)


class GraphAdjMatrix:
    def __init__(self):
        self.index = {}
        self.vertices_names = []
        self.mat = []

    def add_vertex(self, vertex):
        if vertex in self.index:
            return

        self.index[vertex] = len(self.vertices_names)
        self.vertices_names.append(vertex)

        for row in self.mat:
            row.append(0)

        new_row = [0] * len(self.vertices_names)
        self.mat.append(new_row)

    def add_edge(self, u, v, directed=False):
        self.add_vertex(u)
        self.add_vertex(v)

        i = self.index[u]
        j = self.index[v]
        self.mat[i][j] = 1

        if not directed:
            self.mat[j][i] = 1

    def has_edge(self, u, v):
        if u not in self.index or v not in self.index:
            return False

        i = self.index[u]
        j = self.index[v]
        return self.mat[i][j] == 1

    def print_matrix(self):
        print("vertices:", self.vertices_names)
        for row in self.mat:
            print(row)


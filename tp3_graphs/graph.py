from collections import deque


class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj:
            self.adj[vertex] = []

    def add_edge(self, origin, destination):
        self.add_vertex(origin)
        self.add_vertex(destination)

        if destination not in self.adj[origin]:
            self.adj[origin].append(destination)

        if not self.directed:
            if origin not in self.adj[destination]:
                self.adj[destination].append(origin)

    def print_adj_list(self):
        for vertex in sorted(self.adj):
            print(vertex, ":", sorted(self.adj[vertex]))

    def vertices(self):
        return list(self.adj.keys())

    def dfs(self, start):
        visited = set()
        order = []

        def visit(vertex):
            visited.add(vertex)
            order.append(vertex)

            for neighbor in sorted(self.adj.get(vertex, [])):
                if neighbor not in visited:
                    visit(neighbor)

        visit(start)
        return order

    def bfs(self, start):
        visited = set()
        queue = deque()

        order = []
        visited.add(start)
        queue.append(start)

        while queue:
            vertex = queue.popleft()
            order.append(vertex)

            for neighbor in sorted(self.adj.get(vertex, [])):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order

    def has_path(self, start, end):
        if start == end:
            return True

        visited = set()
        queue = deque()

        visited.add(start)
        queue.append(start)

        while queue:
            vertex = queue.popleft()

            for neighbor in self.adj.get(vertex, []):
                if neighbor == end:
                    return True

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False

    def shortest_path_bfs(self, start, end):
        if start == end:
            return [start]

        visited = set()
        queue = deque()

        visited.add(start)
        queue.append((start, [start]))

        while queue:
            vertex, path = queue.popleft()

            for neighbor in sorted(self.adj.get(vertex, [])):
                if neighbor not in visited:
                    new_path = path + [neighbor]

                    if neighbor == end:
                        return new_path

                    visited.add(neighbor)
                    queue.append((neighbor, new_path))

        return []


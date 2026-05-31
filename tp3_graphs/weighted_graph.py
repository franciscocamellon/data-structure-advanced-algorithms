from collections import deque
import heapq


class WeightedGraph:
    def __init__(self):
        self.adj = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj:
            self.adj[vertex] = []

    def add_edge(self, origin, destination, weight):
        self.add_vertex(origin)
        self.add_vertex(destination)

        self.adj[origin].append((destination, weight))
        self.adj[destination].append((origin, weight))

    def neighbors(self, vertex):
        return self.adj.get(vertex, [])

    def reachable_bfs(self, start):
        visited = set()
        queue = deque()
        order = []

        visited.add(start)
        queue.append(start)

        while queue:
            vertex = queue.popleft()
            order.append(vertex)

            neighbor_names = []
            for neighbor, weight in self.neighbors(vertex):
                neighbor_names.append(neighbor)

            for neighbor in sorted(neighbor_names):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order

    def dfs(self, start):
        visited = set()
        order = []

        def visit(vertex):
            visited.add(vertex)
            order.append(vertex)

            neighbor_names = []
            for neighbor, weight in self.neighbors(vertex):
                neighbor_names.append(neighbor)

            for neighbor in sorted(neighbor_names):
                if neighbor not in visited:
                    visit(neighbor)

        visit(start)
        return order

    def shortest_path_bfs(self, start, end):
        visited = set()
        queue = deque()

        visited.add(start)
        queue.append((start, [start]))

        while queue:
            vertex, path = queue.popleft()

            neighbor_names = []
            for neighbor, weight in self.neighbors(vertex):
                neighbor_names.append(neighbor)

            for neighbor in sorted(neighbor_names):
                if neighbor not in visited:
                    new_path = path + [neighbor]

                    if neighbor == end:
                        return new_path

                    visited.add(neighbor)
                    queue.append((neighbor, new_path))

        return []

    def cost_of_path(self, path):
        total = 0

        for i in range(len(path) - 1):
            origin = path[i]
            destination = path[i + 1]
            found = False

            for neighbor, weight in self.neighbors(origin):
                if neighbor == destination:
                    total += weight
                    found = True
                    break

            if not found:
                return None

        return total

    def dijkstra(self, start):
        distances = {}
        previous = {}

        for vertex in self.adj:
            distances[vertex] = float("inf")
            previous[vertex] = None

        distances[start] = 0
        queue = [(0, start)]

        while queue:
            current_distance, vertex = heapq.heappop(queue)

            if current_distance > distances[vertex]:
                continue

            for neighbor, weight in self.neighbors(vertex):
                new_distance = current_distance + weight

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = vertex
                    heapq.heappush(queue, (new_distance, neighbor))

        return distances, previous


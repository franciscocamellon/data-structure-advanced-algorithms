from collections import deque
import heapq

from graph import Graph
from weighted_graph import WeightedGraph


def count_teams(number_of_students, friendships):
    graph = Graph()

    for student in range(1, number_of_students + 1):
        graph.add_vertex(student)

    for a, b in friendships:
        graph.add_edge(a, b)

    visited = set()
    groups = 0

    for student in range(1, number_of_students + 1):
        if student not in visited:
            groups += 1
            stack = [student]
            visited.add(student)

            while stack:
                current = stack.pop()

                for neighbor in graph.adj[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

    return groups


def count_valid_tours(number_of_rooms, tunnels, tours):
    graph = Graph()

    for room in range(1, number_of_rooms + 1):
        graph.add_vertex(room)

    for a, b in tunnels:
        graph.add_edge(a, b)

    valid_count = 0

    for tour in tours:
        is_valid = True

        for i in range(len(tour) - 1):
            origin = tour[i]
            destination = tour[i + 1]

            if not graph.has_path(origin, destination):
                is_valid = False
                break

        if is_valid:
            valid_count += 1

    return valid_count


def process_island_operations(number_of_islands, operations):
    graph = Graph()
    answers = []

    for island in range(1, number_of_islands + 1):
        graph.add_vertex(island)

    for operation, a, b in operations:
        if operation == 1:
            graph.add_edge(a, b)
        else:
            if graph.has_path(a, b):
                answers.append(1)
            else:
                answers.append(0)

    return answers


def build_product_graph():
    graph = Graph()
    edges = [
        ("brush", "nail_polish"),
        ("nail_polish", "eye_shadow"),
        ("eye_shadow", "eye_glasses"),
        ("nail_polish", "nails"),
        ("nails", "pins"),
        ("nails", "needles"),
        ("pins", "needles"),
        ("nails", "hammer"),
        ("hammer", "drill"),
        ("hammer", "saw"),
        ("saw", "knife"),
        ("knife", "fork"),
        ("knife", "spoon"),
    ]

    for origin, destination in edges:
        graph.add_edge(origin, destination)

    return graph


def build_social_graph():
    graph = Graph()
    edges = [
        ("Idris", "Kamil"),
        ("Idris", "Talia"),
        ("Kamil", "Lina"),
        ("Lina", "Sasha"),
        ("Sasha", "Marco"),
        ("Marco", "Ken"),
        ("Ken", "Talia"),
    ]

    for origin, destination in edges:
        graph.add_edge(origin, destination)

    return graph


def build_dependency_graph():
    graph = Graph(directed=True)
    edges = [
        ("Inicio", "A"),
        ("Inicio", "B"),
        ("A", "C"),
        ("B", "C"),
        ("C", "D"),
        ("D", "E"),
        ("B", "F"),
        ("F", "E"),
    ]

    for origin, destination in edges:
        graph.add_edge(origin, destination)

    return graph


def build_port_graph():
    graph = WeightedGraph()
    edges = [
        ("Berco_A", "Patio_1", 4),
        ("Berco_A", "Patio_2", 7),
        ("Berco_B", "Patio_2", 3),
        ("Berco_B", "Patio_3", 6),
        ("Patio_1", "Patio_2", 2),
        ("Patio_2", "Patio_3", 2),
        ("Patio_1", "Alfandega", 8),
        ("Patio_2", "Alfandega", 5),
        ("Patio_3", "Centro_Logistico", 4),
        ("Alfandega", "Centro_Logistico", 3),
    ]

    for origin, destination, weight in edges:
        graph.add_edge(origin, destination, weight)

    return graph


def rebuild_path(previous, start, end):
    path = []
    current = end

    while current is not None:
        path.append(current)

        if current == start:
            break

        current = previous[current]

    path.reverse()

    if not path or path[0] != start:
        return []

    return path


def print_distances(distances):
    for vertex in sorted(distances):
        print(vertex, ":", distances[vertex])


def run_basic_tests():
    print("Exercício 1 - Formação de times")
    friendships = [(1, 2), (2, 3), (4, 5)]
    print("Quantidade de grupos:", count_teams(6, friendships), "esperado: 3")

    print("\nExercício 2 - Passeios válidos")
    tunnels = [(1, 2), (2, 3), (4, 5)]
    tours = [
        [1, 3],
        [1, 2, 3],
        [1, 4],
        [4, 5],
    ]
    print("Passeios válidos:", count_valid_tours(5, tunnels, tours), "esperado: 3")

    print("\nExercício 3 - Conectividade dinâmica entre ilhas")
    operations = [
        (0, 1, 2),
        (1, 1, 2),
        (0, 1, 2),
        (1, 2, 3),
        (0, 1, 3),
        (0, 4, 5),
    ]
    print("Respostas:", process_island_operations(5, operations), "esperado: [0, 1, 1, 0]")

    print("\nExercício 4 - DFS em recomendações")
    product_graph = build_product_graph()
    dfs_result = product_graph.dfs("nails")
    print("Ordem DFS:", dfs_result)

    print("\nExercício 5 - BFS em recomendações")
    bfs_result = product_graph.bfs("nails")
    print("Ordem BFS:", bfs_result)

    print("\nExercício 6 - Menor caminho em rede social")
    social_graph = build_social_graph()
    path = social_graph.shortest_path_bfs("Idris", "Lina")
    print("Caminho:", path)
    print("Distância:", len(path) - 1)

    print("\nExercício 7 - Grafo direcionado")
    dependency_graph = build_dependency_graph()
    print("DFS:", dependency_graph.dfs("Inicio"))
    print("BFS:", dependency_graph.bfs("Inicio"))

    print("\nExercício 8 - BFS ignorando pesos na rede logística")
    port_graph = build_port_graph()
    reachable = port_graph.reachable_bfs("Berco_A")
    bfs_path = port_graph.shortest_path_bfs("Berco_A", "Centro_Logistico")
    print("Áreas alcançáveis:", reachable)
    print("Caminho com menor número de etapas:", bfs_path)
    print("Custo desse caminho:", port_graph.cost_of_path(bfs_path))

    print("\nExercício 9 - Dijkstra")
    distances, previous = port_graph.dijkstra("Berco_A")
    print("Menores distâncias a partir de Berco_A:")
    print_distances(distances)

    print("\nExercício 10 - Reconstrução da rota ótima")
    dijkstra_path = rebuild_path(previous, "Berco_A", "Centro_Logistico")
    print("Caminho mínimo:", dijkstra_path)
    print("Custo:", port_graph.cost_of_path(dijkstra_path))

    print("\nExercício 11 - Comparação BFS x Dijkstra")
    print("Caminho BFS:", bfs_path)
    print("Custo BFS:", port_graph.cost_of_path(bfs_path))
    print("Caminho Dijkstra:", dijkstra_path)
    print("Custo Dijkstra:", port_graph.cost_of_path(dijkstra_path))

    print("\nExercício 12 - Análise geral da rede logística")
    print("Ordem DFS:", port_graph.dfs("Berco_A"))
    print("Ordem BFS:", port_graph.reachable_bfs("Berco_A"))
    print("Distâncias Dijkstra:")
    print_distances(distances)


if __name__ == "__main__":
    run_basic_tests()

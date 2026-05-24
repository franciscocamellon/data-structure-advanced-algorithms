from graph import GraphAdjList, GraphAdjMatrix
from trie import Trie

EDGE = [
    ("auth", "user"),
    ("auth", "payment"),
    ("user", "profile"),
    ("user", "email"),
    ("profile", "report"),
    ("order", "product"),
    ("order", "payment"),
    ("product", "stock"),
    ("product", "search"),
    ("stock", "report"),
    ("search", "report"),
    ("email", "report"),
]


def create_graph(choice):
    if choice == "list":
        return GraphAdjList()
    elif choice == "matrix":
        return GraphAdjMatrix()
    else:
        raise ValueError("Opção inválida. Escolha 'list' ou 'matrix'.")


def build_sample_graph(choice):
    graph = create_graph(choice)
    edges = EDGE

    for u, v in edges:
        graph.add_edge(u, v)

    return graph


def find_vertices_by_prefix(prefix, k, trie, graph):
    candidates = trie.autocomplete(prefix, k)
    graph_vertices = graph.vertices()

    result = []
    for name in candidates:
        if name in graph_vertices:
            result.append(name)

    return result


def run_basic_tests():
    trie = Trie()

    print("Exercício 1")
    print("inserir 'car':", trie.insert("car"), "esperado: True")
    print("inserir 'car' novamente:", trie.insert("car"), "esperado: False")
    print("inserir 'cart':", trie.insert("cart"), "esperado: True")
    print("inserir 'carro':", trie.insert("carro"), "esperado: True")

    print("\nExercício 2")
    print("buscar 'car':", trie.search("car"), "esperado: True")
    print("buscar 'cart':", trie.search("cart"), "esperado: True")
    print("buscar 'ca':", trie.search("ca"), "esperado: False")
    print("buscar 'casa':", trie.search("casa"), "esperado: False")
    print("buscar palavra vazia:", trie.search(""), "esperado: False")

    words = ["car", "cart", "carro", "cat", "cab", "cable", "dog", "door", "dove"]
    trie = Trie()

    for word in words:
        trie.insert(word)

    print("\nExercício 3")
    prefixes = ["ca", "car", "do", "z", "cab"]

    for prefix in prefixes:
        print("prefixo", prefix, "->", trie.starts_with(prefix))

    print("\nExercício 4")
    print("todas as palavras:", trie.all_words())
    print("palavras a partir do prefixo 'ca':", trie.words_from_prefix("ca"))

    print("\nExercício 5")
    print("autocomplete para 'ca', limite 3:", trie.autocomplete("ca", 3))
    print("autocomplete para 'dog', limite 5:", trie.autocomplete("dog", 5))
    print("autocomplete para 'x', limite 5:", trie.autocomplete("x", 5))

    print("\nExercício 6")
    tests = ["car", "carx", "cot", "dzz", "xyz", "ca"]

    for word in tests:
        print("autocorreção de", word, "->", trie.autocorrect(word))

    print("\nExercício 7")
    graph_list = build_sample_graph("list")
    print("Lista de adjacência do grafo:")
    graph_list.print_adj_list()

    print("\nExercício 8")
    graph_matrix = build_sample_graph("matrix")
    print("Matriz de adjacência do grafo:")
    graph_matrix.print_matrix()

    print("\nExercício 9")
    print("lista possui aresta auth-user:", graph_list.has_edge("auth", "user"))
    print("matriz possui aresta auth-user:", graph_matrix.has_edge("auth", "user"))
    print("lista possui aresta auth-report:", graph_list.has_edge("auth", "report"))
    print("matriz possui aresta auth-report:", graph_matrix.has_edge("auth", "report"))

    print("\nExercício 10")
    print("Representação Mermaid do grafo:")
    print(graph_list.to_mermaid())

    print("\nExercício 11")
    vertex_trie = Trie()

    for vertex in graph_list.vertices():
        vertex_trie.insert(vertex)

    print("vértices com prefixo 'p':", find_vertices_by_prefix("p", 5, vertex_trie, graph_list))
    print("vértices com prefixo 'pro':", find_vertices_by_prefix("pro", 5, vertex_trie, graph_list))
    print("vértices com prefixo 'x':", find_vertices_by_prefix("x", 5, vertex_trie, graph_list))


if __name__ == "__main__":
    run_basic_tests()

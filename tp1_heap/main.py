from binary_heap import BinaryHeap


def is_valid_heap(array):
    for child in range(1, len(array)):
        parent = (child - 1) // 2
        if array[child] > array[parent]:
            return False
    return True


def k_largest(array, k):
    heap = BinaryHeap()
    heap.build_heap(array)

    result = []
    count = min(k, len(array))

    for i in range(count):
        value, changes = heap.extract_max()
        result.append(value)

    return result


def build_by_insert(array):
    heap = BinaryHeap()
    heap.reset_counters()

    for value in array:
        heap.insert(value)

    return heap


def compare_build_methods(array):
    heap_insert = build_by_insert(array)

    heap_build = BinaryHeap()
    heap_build.build_heap(array)

    return {
        "insert_heap": heap_insert.heap,
        "insert_comparisons": heap_insert.comparisons,
        "insert_swaps": heap_insert.swaps,
        "build_heap": heap_build.heap,
        "build_comparisons": heap_build.comparisons,
        "build_swaps": heap_build.swaps,
    }


def print_build_comparison(array):
    result = compare_build_methods(array)

    print("Array original:", array)

    print("\nConstrução por inserção:")
    print("Heap gerada:", result["insert_heap"])
    print("Comparações:", result["insert_comparisons"])
    print("Trocas:", result["insert_swaps"])

    print("\nConstrução com build_heap:")
    print("Heap gerada:", result["build_heap"])
    print("Comparações:", result["build_comparisons"])
    print("Trocas:", result["build_swaps"])


def empirical_test():
    sizes = [10, 50, 100, 500]
    results = []

    for size in sizes:
        data = list(range(size, 0, -1))
        heap = BinaryHeap()
        heap.build_heap(data)

        results.append({
            "size": size,
            "comparisons": heap.comparisons,
            "swaps": heap.swaps,
            "valid_heap": is_valid_heap(heap.heap),
        })

    return results


def run_basic_tests():
    print("Exercício 1 - Exemplo de problema")
    print("Usei como exemplo uma fila de tarefas por prioridade. A maior prioridade sai primeiro.")

    print("\nExercício 2 - Estrutura da heap")
    heap = BinaryHeap()
    print("heap inicial:", heap.heap)
    print("índice pai de 3:", heap.get_parent_index(3))
    print("filho esquerdo de 1:", heap.get_left_child_index(1))
    print("filho direito de 1:", heap.get_right_child_index(1))

    print("\nExercício 3 - Inserção")
    values = [33, 32, 28, 31, 29, 26, 25, 30, 27]
    for value in values:
        changes = heap.insert(value)
        print("inserindo", value, "->", heap.heap, "trocas:", len(changes))

    print("\nTeste com valores em ordem crescente")
    heap2 = BinaryHeap()
    for value in [10, 20, 30, 40, 50]:
        changes = heap2.insert(value)
        print("inserindo", value, "->", heap2.heap, "trocas:", len(changes))

    print("\nExercício 4 - Extração do maior")
    heap3 = BinaryHeap()
    heap3.build_heap([60, 20, 40, 70, 30, 10])
    print("heap antes das extrações:", heap3.heap)
    while not heap3.is_empty():
        value, changes = heap3.extract_max()
        print("extraído:", value, "heap:", heap3.heap, "trocas:", len(changes))

    print("\nExercício 5 - Busca linear")
    heap4 = BinaryHeap()
    heap4.build_heap([60, 20, 40, 70, 30, 10])
    print("contém 40:", heap4.contains(40))
    print("contém 99:", heap4.contains(99))

    print("\nExercício 6 - Remoção de valor qualquer")
    print("heap antes:", heap4.heap)
    print("remover 40:", heap4.delete(40))
    print("heap depois:", heap4.heap)
    print("remover 99:", heap4.delete(99))

    print("\nExercício 7 - Validação")
    print("[33, 32, 28, 31, 29, 26, 25, 30, 27]:", is_valid_heap([33, 32, 28, 31, 29, 26, 25, 30, 27]))
    print("[33, 32, 28, 31, 26, 29, 25, 30, 27]:", is_valid_heap([33, 32, 28, 31, 26, 29, 25, 30, 27]))

    print("\nExercício 8 - Build heap")
    heap5 = BinaryHeap()
    heap5.build_heap([4, 10, 3, 5, 1, 8, 2])
    print("heap construída:", heap5.heap)

    print("\nExercício 9 - Comparação")
    print_build_comparison([4, 10, 3, 5, 1, 8, 2])

    print("\nExercício 10 - k maiores")
    print("3 maiores:", k_largest([60, 20, 40, 70, 30, 10], 3))
    print("2 maiores:", k_largest([5, 1, 9, 3, 7], 2))

    print("\nExercício 11 - Teste empírico simples")
    for row in empirical_test():
        print(row)


if __name__ == "__main__":
    run_basic_tests()

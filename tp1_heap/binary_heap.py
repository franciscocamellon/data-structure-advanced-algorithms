

class BinaryHeap:
    def __init__(self):
        self.heap = []
        self.swaps = 0
        self.comparisons = 0

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    @staticmethod
    def get_parent_index(index):
        return (index - 1) // 2

    @staticmethod
    def get_left_child_index(index):
        return 2 * index + 1

    @staticmethod
    def get_right_child_index(index):
        return 2 * index + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.swaps += 1

    def reset_counters(self):
        self.swaps = 0
        self.comparisons = 0

    def sift_up(self, index):
        changes = []

        while index > 0:
            parent = self.get_parent_index(index)
            self.comparisons += 1

            if self.heap[index] > self.heap[parent]:
                before = self.heap.copy()
                self.swap(index, parent)
                changes.append((before, self.heap.copy()))
                index = parent
            else:
                break

        return changes

    def sift_down(self, index):
        changes = []
        last_index = len(self.heap) - 1

        while True:
            left = self.get_left_child_index(index)
            right = self.get_right_child_index(index)
            largest = index

            if left <= last_index:
                self.comparisons += 1
                if self.heap[left] > self.heap[largest]:
                    largest = left

            if right <= last_index:
                self.comparisons += 1
                if self.heap[right] > self.heap[largest]:
                    largest = right

            if largest != index:
                before = self.heap.copy()
                self.swap(index, largest)
                changes.append((before, self.heap.copy()))
                index = largest
            else:
                break

        return changes

    def insert(self, value):
        self.heap.append(value)
        return self.sift_up(len(self.heap) - 1)

    def peek_max(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def extract_max(self):
        if self.is_empty():
            return None, []

        max_value = self.heap[0]

        if len(self.heap) == 1:
            self.heap.pop()
            return max_value, []

        self.heap[0] = self.heap.pop()
        changes = self.sift_down(0)
        return max_value, changes

    def contains(self, value):
        for item in self.heap:
            self.comparisons += 1
            if item == value:
                return True
        return False

    def delete(self, value):
        index = -1

        for i in range(len(self.heap)):
            self.comparisons += 1
            if self.heap[i] == value:
                index = i
                break

        if index == -1:
            return False, []

        if index == len(self.heap) - 1:
            self.heap.pop()
            return True, []

        self.heap[index] = self.heap.pop()

        changes = []
        if index > 0:
            parent = self.get_parent_index(index)
            self.comparisons += 1
            if self.heap[index] > self.heap[parent]:
                changes = self.sift_up(index)
            else:
                changes = self.sift_down(index)
        else:
            changes = self.sift_down(index)

        return True, changes

    def build_heap(self, array):
        self.heap = array.copy()
        self.reset_counters()

        last_parent = (len(self.heap) // 2) - 1
        all_changes = []

        for index in range(last_parent, -1, -1):
            changes = self.sift_down(index)
            all_changes.extend(changes)

        return all_changes

    def print_heap(self):
        print(self.heap)


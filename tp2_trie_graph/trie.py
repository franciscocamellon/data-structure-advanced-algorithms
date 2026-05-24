


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if word == "":
            return False

        current = self.root
        created_new = False

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
                created_new = True
            current = current.children[char]

        if current.is_end:
            return False

        current.is_end = True
        return True

    def search(self, word):
        if word == "":
            return False

        current = self.root

        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]

        return current.is_end

    def starts_with(self, prefix):
        current = self.root

        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]

        return True

    def find_node(self, prefix):
        current = self.root

        for char in prefix:
            if char not in current.children:
                return None
            current = current.children[char]

        return current

    def collect_words(self, node, prefix):
        words = []

        if node is None:
            return words

        if node.is_end:
            words.append(prefix)

        for char in node.children:
            child = node.children[char]
            words += self.collect_words(child, prefix + char)

        return words

    def all_words(self):
        return sorted(self.collect_words(self.root, ""))

    def words_from_prefix(self, prefix):
        node = self.find_node(prefix)
        return sorted(self.collect_words(node, prefix))

    def autocomplete(self, prefix, k):
        if k <= 0:
            return []

        suggestions = self.words_from_prefix(prefix)
        return suggestions[:k]

    def autocorrect(self, word):
        if self.search(word):
            return word

        current = self.root
        prefix = ""

        for char in word:
            if char not in current.children:
                break
            current = current.children[char]
            prefix += char

        candidates = sorted(self.collect_words(current, prefix))

        if len(candidates) == 0:
            return None

        return candidates[0]
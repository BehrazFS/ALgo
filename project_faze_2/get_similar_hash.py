class TrieNode:
    def __init__(self):
        self.children = {}
        self.strings = []


def levenshtein_distance(s1, s2, threshold):
    if abs(len(s1) - len(s2)) > threshold:
        return threshold + 1

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        if min(current_row) > threshold:
            return threshold + 1
        previous_row = current_row

    return previous_row[-1]


def insert_into_trie(root, string):
    node = root
    for char in string:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.strings.append(string)


def collect_similar_strings(root, string, threshold):
    node = root
    for char in string:
        if char in node.children:
            node = node.children[char]
        else:
            break
    similar_strings = node.strings[:]
    return [s for s in similar_strings if levenshtein_distance(s, string, threshold) <= threshold]


def update_clusters(strings, clusters, threshold):
    root = TrieNode()
    for cluster in clusters:
        for string in cluster:
            insert_into_trie(root, string)

    new_clusters = []
    for string in strings:
        similar_strings = collect_similar_strings(root, string, threshold)
        added_to_cluster = False
        for cluster in new_clusters:
            if any(levenshtein_distance(string, member, threshold) <= threshold for member in cluster):
                cluster.append(string)
                added_to_cluster = True
                break
        if not added_to_cluster:
            new_clusters.append([string])

        insert_into_trie(root, string)

    return new_clusters


def map_strings_to_numbers(strings, threshold=3):
    clusters = update_clusters(strings, [], threshold)
    mapping = {}
    for number, cluster in enumerate(clusters):
        for string in cluster:
            mapping[string] = number
    return mapping


if __name__ == '__main__':
    initial_strings = ["apple", "appl", "apples", "banana", "bananas", "banan"]
    threshold = 3

    mapping = map_strings_to_numbers(initial_strings, threshold)

    print("Initial Clusters:")
    for string, number in mapping.items():
        print(f"{string}: {number}")

    new_strings = ["application", "apply", "orange", "apple"]

    updated_mapping = map_strings_to_numbers(new_strings + initial_strings, threshold)

    print("\nUpdated Clusters:")
    for string, number in updated_mapping.items():
        print(f"{string}: {number}")

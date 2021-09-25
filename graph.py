from collections import deque


def breadth_first_search(root: str, graph: dict) -> list:
    visited = list()
    queue = deque()
    queue.append(root)
    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.append(current)
        queue += sorted(graph[current])
    return visited


def depth_first_search(root: str, graph: dict) -> list:
    visited_vertices = list()
    graph_stack = deque()
    graph_stack.append(root)
    node = root
    while graph_stack:
        if node not in visited_vertices:
            visited_vertices.append(node)
        adj_nodes = graph[node]
        # if all neighbors already visited
        if set(adj_nodes).issubset(set(visited_vertices)):
            graph_stack.pop()
            if graph_stack:
                node = graph_stack[-1]
            continue
        else:
            # select only not visited neighbors
            remaining_elements = set(adj_nodes) - set(visited_vertices)
            first_adj_node = sorted(remaining_elements)[0]
            graph_stack.append(first_adj_node)
            node = first_adj_node
    return visited_vertices


def make_adjacency_matrix_from_dict(graph: dict) -> list[list]:
    matrix_elements = sorted(graph.keys())
    cols = rows = len(matrix_elements)
    adjacency_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    edges_list = []
    for key in matrix_elements:
        for neighbor in graph[key]:
            edges_list.append((key, neighbor))
    for vertex, neighbor in edges_list:
        adjacency_matrix[matrix_elements.index(vertex)][matrix_elements.index(neighbor)] = 1
    return adjacency_matrix


def main():
    graph = dict()
    graph['A'] = ['B', 'S']
    graph['B'] = ['A']
    graph['S'] = ['A', 'G', 'C']
    graph['D'] = ['C']
    graph['G'] = ['S', 'F', 'H']
    graph['H'] = ['G', 'E']
    graph['E'] = ['C', 'H']
    graph['F'] = ['C', 'G']
    graph['C'] = ['D', 'S', 'E', 'F']

    matrix = make_adjacency_matrix_from_dict(graph)
    from pprint import pprint
    pprint(matrix)
    result = breadth_first_search('A', graph)
    print(result)
    # depth_first_traversal('A', graph)
    print(depth_first_search('A', graph))


if __name__ == '__main__':
    main()

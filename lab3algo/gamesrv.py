import heapq


# створюється граф
class Graph(object):
    def __init__(self, vertices=None, client_vertices=None):
        self.vertices = vertices or []
        self.client_vertices = client_vertices or set()


# зчитування
def read_graph(fl):
    vertex_count, edge_count = [int(tok) for tok in fl.readline().split()]
    vertices = [set() for i in range(vertex_count)]
    client_vertices = {int(tok) - 1 for tok in fl.readline().split()}
    graph = Graph(vertices=vertices, client_vertices=client_vertices)

    for line in fl.readlines():
        _from, to, weight = [int(tok) for tok in line.rstrip().split()]
        _from -= 1
        to -= 1
        graph.vertices[_from].add((to, weight))
        graph.vertices[to].add((_from, weight))
    return graph


def shortest_paths(graph, start_v):
    # алгоритм дейкстра для одної вершини
    distances = [float('inf')] * len(graph.vertices)
    distances[start_v] = 0
    pq = [(0, start_v)]
    while pq:
        distance, vertex = heapq.heappop(pq)
        for neighbor, nweight in graph.vertices[vertex]:
            new_distance = distance + nweight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))
    return distances


def max_shortest_paths(graph):
    # загальний виклик алгоритмку дейкстра для тих вершин, які ще не пройдені були
    for vertex in range(len(graph.vertices)):
        if vertex in graph.client_vertices:
            continue
        distances = shortest_paths(graph, vertex)
        yield max(dst for v, dst in enumerate(distances) if v in graph.client_vertices)


def main():
    with open('gamsrv.in', 'r') as fl:
        graph = read_graph(fl)
        result = min(max_shortest_paths(graph))

    print(str(result))


if __name__ == '__main__':
    main()

import collections
class Graph:
    def __init__(self,graph=None):
        if graph is None:
            graph = {}
        self.graph = graph

def bfs(graph, startnode):
# Отслеживание посещенных и не посещенных вершин с использованием очереди
        seen, queue = set([startnode]), collections.deque([startnode])
        while queue:
            vertex = queue.popleft()
            marked(vertex)
            for node in graph[vertex]:
                if node not in seen:
                    seen.add(node)
                    queue.append(node)

def marked(n):
    print(n)

# The graph dictionary
graph =        {"1" : set(["2","3","4"]),
                "2" : set(["1", "8"]),
                "3" : set(["1"]),
                "4" : set(["1"]),
                "5" : set(["7","8","9"]),
                "6" : set(["8"]),
                "7" : set(["5"]),
                "8" : set(["2","5","6"]),
                "9" : set(["5"])}

bfs(graph, "1")
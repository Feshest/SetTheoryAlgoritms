class Graph:

    def __init__(self,graph=None):
        if graph is None:
            graph = {}
        self.graph = graph
#Проверка на посещенные и не посещенные вершины
def depthFirstSearch(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        depthFirstSearch(graph, next, visited)
    return visited

graph =        {"1" : set(["2","3","4"]),
                "2" : set(["1", "8"]),
                "3" : set(["1"]),
                "4" : set(["1"]),
                "5" : set(["7","8","9"]),
                "6" : set(["8"]),
                "7" : set(["5"]),
                "8" : set(["2","5","6"]),
                "9" : set(["5"])}


depthFirstSearch(graph, '1')
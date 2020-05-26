# матрица смежности
graph = [[0,0,1,1,0,0,0,0,0],
         [1,0,0,0,0,0,0,1,0],
         [1,0,0,0,0,0,0,0,0],
         [1,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,1,1,1],
         [0,0,0,0,0,0,0,1,0],
         [0,0,0,0,1,0,0,0,0],
         [0,1,0,0,1,1,0,0,0],
         [0,0,0,0,1,0,0,0,0]]

# main function

def checkCycle(graph):
    count = 0
    line_lenght = len(graph)
    column_lenght = len(graph[0])

    for i in range(line_lenght):
        for j in range(column_lenght):
            if graph[i][j] == 0:
                graph[i][j] = 0

    for i in range(line_lenght):
        for j in range(column_lenght):
            if graph[i][j] == 0:
                graph[j][i] = 0

    for i in range(line_lenght):
        for j in range(column_lenght):
            if graph[i][j] != 0:
                count = count + 1

    if count > 0:
        print("Граф циклический")
    else:
        print("Граф ациклический")

print(checkCycle(graph))



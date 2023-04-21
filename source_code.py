import heapq
import time
start_time = time.time()

def dijkstra_algorithm(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    pq = [(0, start)]
    while pq:
        curr_distance, curr_node = heapq.heappop(pq)

        if curr_node == end:
            return curr_distance

        for neighbor, weight in graph[curr_node].items():
            distance = curr_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

def shortest_path(matrix):
    m = len(matrix)
    n = len(matrix[0])
    graph = {}
    for i in range(m):
        for j in range(n):
            node = (i, j)
            neighbors = {}
            if i > 0:
                neighbors[(i-1, j)] = matrix[i-1][j]
            if j > 0:
                neighbors[(i, j-1)] = matrix[i][j-1]
            if i < m-1:
                neighbors[(i+1, j)] = matrix[i+1][j]
            if j < n-1:
                neighbors[(i, j+1)] = matrix[i][j+1]
            graph[node] = neighbors

    start = (0, 0)
    end = (m-1, n-1)
    shortest_distance = dijkstra_algorithm(graph, start, end)
    return shortest_distance + matrix[0][0]

def read_file(filename):
    graph = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                w = line.split()
                w_num = [int(x) for x in w]
                graph.append(w_num)
    # print(graph)
    return graph

matrix = read_file("in-5.txt")
print(shortest_path(matrix))
print("Process finished --- %s seconds ---" % (time.time() - start_time))
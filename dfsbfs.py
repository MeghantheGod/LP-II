import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

def main():
    graph = {}
    n = int(input("Enter the number of nodes: "))
    for i in range(n):
        node = input(f"Enter node {i + 1}: ")
        neighbors = input(f"Enter neighbors of {node} separated by space: ").split()
        graph[node] = neighbors

    start_node = input("Enter the start node: ")

    print('DFS = ', end=' ')
    dfs(graph, start_node)

    print('\nBFS = ', end=' ')
    bfs(graph, start_node)

    # Drawing the graph
    G = nx.Graph(graph)
    node_colors = ['red' if node == start_node else 'skyblue' for node in G.nodes()]
    nx.draw(G, with_labels=True, node_color=node_colors, node_size=1500, font_size=12, font_weight='bold')
    plt.title("Input Graph")
    plt.show()


main()


# Inputs to be given
#Enter the number of nodes: 5
#Enter node 1: A
#Enter neighbors of A separated by space: B C
#Enter node 2: B
#Enter neighbors of B separated by space: A D
#Enter node 3: C
#Enter neighbors of C separated by space: A D
#Enter node 4: D
#Enter neighbors of D separated by space: B C E
#Enter node 5: E
#Enter neighbors of E separated by space: D
#Enter the start node: A 


# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }

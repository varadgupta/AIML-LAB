# Graph Representation and BFS/DFS

graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input(f"Enter node {i+1} value: ")
    m = int(input(f"Enter number of nodes connected to {node}: "))

    child_nodes = []

    for j in range(m):
        neighbor = input(f"Enter connected node {j+1}: ")
        child_nodes.append(neighbor)

    graph[node] = child_nodes

print("\nGraph:", graph)

start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

# ---------- BFS ----------

def bfs(graph, start, goal):

    queue = [start]
    visited = []

    print("\n--- BFS ---")

    while queue:

        print("Queue:", queue)

        node = queue.pop(0)

        if node not in visited:

            visited.append(node)
            print("Visited:", visited)

            if node == goal:
                print("\nGoal Found!")
                print("Final Visited Nodes:", visited)
                return

            for neighbor in graph[node]:

                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

    print("\nGoal Not Found!")
    print("BFS - Visited Nodes:", visited)

# ---------- DFS ----------

def dfs(graph, start, goal):

    stack = [start]
    visited = []

    print("\n--- DFS ---")

    while stack:

        print("Stack:", stack)

        node = stack.pop()

        if node not in visited:

            visited.append(node)
            print("Visited:", visited)

            if node == goal:
                print("\nGoal Found!")
                print("Final Visited Nodes:", visited)
                return

            for neighbor in reversed(graph[node]):

                if neighbor not in visited and neighbor not in stack:
                    stack.append(neighbor)

    print("\nGoal Not Found!")
    print("DFS - Visited Nodes:", visited)

# ---------- Menu ----------

while True:

    print("\n===== Menu =====")
    print("1. BFS")
    print("2. DFS")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        bfs(graph, start, goal)

    elif choice == 2:
        dfs(graph, start, goal)

    elif choice == 3:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
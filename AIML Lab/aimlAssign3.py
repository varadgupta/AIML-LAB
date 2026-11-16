# Greedy Best First Search 

graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = str(input(f"Enter node {i+1} value: "))
    m = int(input(f"Enter number of nodes connected to {node}: "))
    child_nodes = []

    for j in range(m):
        neighbour = str(input(f"Enter connected node {j+1}: "))
        child_nodes.append(neighbour)

    graph[node] = child_nodes

print("\nGraph:", graph)

heuristic = {}
print("\n----- Heuristic values -----")

for node in graph:
    heuristic[node] = int(input(f"Enter heuristic value for {node} ="))

start = str(input("\nEnter start node: "))
goal = str(input("Enter goal node: "))

def GBFS(graph, heuristic, start, goal):
        open_list = [start]
        closed_list = []
        parent = {}
        previous = None
        
        while open_list:
            current = open_list[0]
            for node in open_list:
                if heuristic[node] < heuristic[current]:
                    current = node
            print("\nOpen List: ",open_list)
            open_list.remove(current)
            
            if current in closed_list:
                continue
                
            if previous is not None:
                parent[current] = previous
            
            closed_list.append(current)
            print("Closed List: ",closed_list)
            
            if current == goal:
                print("Parent nodes: ",parent)
                break
                
            previous = current

            for neighbour in graph[current]:
                if neighbour not in closed_list and neighbour not in open_list:
                        open_list.append(neighbour)
                        
                        parent[neighbour] = current
            
            print("Parent nodes: ",parent)

        if goal not in closed_list:
            print("\nNo path found.")
            return


        # Path Construction
        path = []
        current = goal

        while current != start:
            path.append(current)
            current = parent[current]

        path.append(start)
        path.reverse()

        print("\n------Greedy Best First Search------")
        print("\nVisited nodes:", closed_list)
        print("Path:",path)

GBFS(graph, heuristic, start, goal)
                



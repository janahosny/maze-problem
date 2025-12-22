import heapq, time
import matplotlib.pyplot as plt
from main import maze, start_state as start, goal_state as goal
import numpy as np

rows, cols = maze.shape
moves = [(1,0), (-1,0), (0,1), (0,-1)]

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])  

def astar(maze, start, goal):
    open_list = [(0, start)]
    g_cost = {start: 0}
    parent = {start: None}
    explored = set()

    start_time = time.time()

    while open_list:
        _, current = heapq.heappop(open_list)
        explored.add(current)

        if current == goal:
            return build_path(parent, goal), explored, time.time() - start_time

        for dr, dc in moves:
            nr, nc = current[0] + dr, current[1] + dc
            neighbor = (nr, nc)

            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                new_g = g_cost[current] + 1
                if neighbor not in g_cost or new_g < g_cost[neighbor]:
                    g_cost[neighbor] = new_g
                    f = new_g + heuristic(neighbor, goal)
                    parent[neighbor] = current
                    heapq.heappush(open_list, (f, neighbor))

    return None, explored, time.time() - start_time

def build_path(parent, node):
    path = []
    while node:
        path.append(node)
        node = parent[node]
    return path[::-1]

def draw(maze, path, explored):
    maze_img = maze.copy().astype(float)
    for r, c in explored:
        maze_img[r, c] = 0.5

    plt.imshow(maze_img, cmap="Blues")

    if path:
        plt.plot([p[1] for p in path], [p[0] for p in path], 'r', linewidth=2)

    plt.scatter(start[1], start[0], c='green', s=100)
    plt.scatter(goal[1], goal[0], c='red', s=100)
    plt.xticks([]); plt.yticks([])
    plt.title("A* Algorithm Solving Maze Pathfinding Problem")
    plt.show()

path, explored_nodes, time_taken = astar(maze, start, goal)

print("Path length:", len(path))
print("Explored nodes:", len(explored_nodes))
print("Time:", time_taken)

draw(maze, path, explored_nodes)
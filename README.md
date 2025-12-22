-- Maze pathfinding problem --

Overview:

Our AI project focuses on solving a 20 × 20 maze using A* , BFS and DFS search algorithms. The maze is represented as a 2D grid, and the goal is to find the shortest path from a start cell to a goal cell while avoiding walls.

Maze Description:

The maze size is 20 × 20.
Each cell can be:
0 → free cell
1 → wall (blocked cell)

→ Start position: (0, 0)
→ Goal position: (19, 19)

Movement is allowed in four directions only:
up,down,left, and right ( so we used Manhattan Distance as a heuristic function )

Implemented Algorithms:

A* (Informed Search)
Breadth-First Search (BFS) 
Depth-First Search (DFS) 

Each algorithm finds a path and records:
1- Path length
2- Number of explored nodes
3- Execution time

A* Algorithm Details:

Combines:
g(n) → actual cost from start
h(n) → estimated cost to goal

Total cost:
f(n)=g(n)+h(n)

Characteristics of A*: 

-Informed search: Uses heuristic h(n) to estimate distance to goal. 
-Optimal: Finds shortest path if heuristic is admissible. 
-Complete: Will find a solution if one exists. 
-Admissible heuristic: Never overestimates actual cost → guarantees optimal solution. 
-Heuristic used: Manhattan distance for our maze  |x₁ – x₂| + |y₁ – y₂|

Performance Evaluation:

The algorithms are compared based on:
-Path length
-Number of explored nodes
-Execution time
This comparison helps demonstrate the efficiency of heuristic-based search (A*) compared to uninformed searches (BFS and DFS).

Notes
All moves have equal cost (cost = 1).
Walls are not assigned costs because they are simply blocked.

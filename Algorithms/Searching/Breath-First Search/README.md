# Breadth First Search (BFS)

- **Last Updated:** 2024-07-25
- **Programming Languages:** Python
- **Complexity:** O(V + E) (time), O(V) (space)
- **Requires:** A graph representation

## Description

Breadth First Search (BFS) is a graph traversal algorithm that starts at a root node and explores all neighbors at the present depth prior to moving on to nodes at the next depth level. It is useful for finding the shortest path on unweighted graphs and for traversing or searching tree or graph data structures.

## Algorithm

The Breadth First Search algorithm works as follows:

1. **Initialize:**
    - Create a queue and enqueue the initial node (starting point).
    - Create a set to keep track of visited nodes.
2. **Traversal:**
    - While the queue is not empty:
        - Dequeue a node from the front of the queue.
        - If the node has not been visited:
            - Mark it as visited.
            - Process the node (e.g., print it, check for a condition).
            - Enqueue all adjacent unvisited nodes.
3. **Termination:**
    - The algorithm ends when all nodes reachable from the initial node have been visited.

| **Aspect**                | **DFS (Depth First Search)**                                    | **BFS (Breadth First Search)**                                      |
|---------------------------|------------------------------------------------------------------|---------------------------------------------------------------------|
| **Traversal Strategy**    | Explores as far as possible along each branch before backtracking | Explores all neighbors at the present depth level before moving on to nodes at the next depth level |
| **Data Structure**        | Stack (either implicitly via recursion or explicitly)            | Queue                                                               |
| **Traversal**             | Prioritizes visiting child nodes of the current node before siblings | Prioritizes visiting all neighbors of the current node before moving on to their children            |
| **Use Cases**             | Detecting cycles, solving puzzles with a single solution, topological sorting, pathfinding in trees | Finding the shortest path in unweighted graphs, level-order traversal in trees, peer-to-peer networks |
| **Characteristics**       | Can be implemented using recursion, uses less memory in dense graphs | Guarantees shortest path in an unweighted graph, may use more memory in wide or dense graphs          |
| **Time Complexity**       | O(V + E)                                                         | O(V + E)                                                            |
| **Space Complexity**      | O(V)                                                             | O(V)                                                                |

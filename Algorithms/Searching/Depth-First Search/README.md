# Depth First Search (DFS)

- **Last Updated:** 2024-05-29
- **Programming Languages:** Python
- **Complexity:** O(V + E) (time), O(V) (space)
- **Requires:** A graph representation

## Description

Depth First Search (DFS) is a graph traversal algorithm that starts at a root node and explores as far as possible along each branch before backtracking. It is useful for searching and traversing through data structures like graphs and trees.

## Algorithm

The Depth First Search algorithm works as follows:

1. **Initialize:**
    - Create a stack and push the initial node (starting point).
    - Create a set to keep track of visited nodes.
2. **Traversal:**
    - While the stack is not empty:
        - Pop a node from the stack.
        - If the node has not been visited:
            - Mark it as visited.
            - Process the node (e.g., print it, check for a condition).
            - Push all adjacent unvisited nodes onto the stack.
3. **Backtracking:**
    - If a node has no unvisited adjacent nodes, backtrack to the previous node.

4. **Termination:**
    - The algorithm ends when all nodes reachable from the initial node have been visited.

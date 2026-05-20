# Weekly Coding #9: Midnight Monster Delivery

## Summary

This program finds the cheapest delivery routes through a haunted city using Dijkstra’s algorithm. Each location in the city is represented as a node, and each road between locations has a positive travel cost. The program uses a heap-based priority queue with Python’s `heapq` module to efficiently process the next cheapest location.

The program can calculate the minimum delivery cost from one starting point to every other location. It can also find the shortest path between two locations and reconstruct the final route using a previous-node dictionary.

---

## Approach

- I represented the haunted city as a weighted graph using a dictionary of dictionaries.
- Each key in the graph is a location, and each value is another dictionary containing neighboring locations and travel costs.
- I used `heapq` as a priority queue to always process the location with the currently cheapest known cost.
- During Dijkstra’s algorithm, I used relaxation:
  - calculate a possible new cost
  - compare it with the current stored cost
  - update the cost if the new path is cheaper
- I stored previous nodes in a dictionary to reconstruct the final shortest path.
- To rebuild the path, I started from the target and followed previous nodes backward until reaching the start node.
- I validated the graph before running the algorithm to ensure:
  - all edge weights are positive
  - every neighbor exists in the graph
  - neighbor lists are dictionaries

---

## Complexity

### `monster_delivery_costs`

- **Time:** `O((V + E) log V)`
- **Space:** `O(V)`
- **Why:**  
  The algorithm may process every vertex and edge while using heap operations that take `O(log V)` time. Extra space is used for the cost dictionary and priority queue.

### `shortest_monster_delivery`

- **Time:** `O((V + E) log V)`
- **Space:** `O(V)`
- **Why:**  
  This function also uses Dijkstra’s algorithm with a heap-based priority queue. Additional space is used for the previous-node dictionary to reconstruct the final path.

---

## Edge-Case Checklist

- [x] start equals target
- [x] target is unreachable
- [x] start node is missing
- [x] target node is missing
- [x] node has no outgoing edges
- [x] graph contains cycles
- [x] tied shortest paths
- [x] negative edge weight
- [x] zero edge weight
- [x] neighbor not listed as a graph node

---

## Tests I Added

- Added a test where the start and target are the same node.
- Added a test for unreachable target nodes.
- Added a test for invalid graphs with negative edge weights.

---

## Assistance & Sources

### AI used?  
Y

### If yes, what did it help with?

- Understanding Dijkstra’s algorithm
- Heap queue syntax using `heapq`
- Debugging path reconstruction
- Complexity explanations
- Edge-case handling

### Other sources used

- Python documentation
- Class lecture notes
- Course examples

---

## Notes for Instructor

- The stretch function `best_next_monster_stop` was completed.
- The project uses only the Python standard library.
- All functions were tested with `pytest`.

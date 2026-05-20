"""Week 11: Midnight Monster Delivery.

Implement Dijkstra's algorithm using a heap-based priority queue.

Rules:
- Use Python 3.11+.
- Use the standard library only.
- Use heapq for the priority queue.
- Edge weights must be positive.
"""

from math import inf
import heapq


HAUNTED_CITY = {
    "Crypt Kitchen": {
        "Fog Alley": 2,
        "Bone Bridge": 5,
    },
    "Fog Alley": {
        "Moon Bridge": 1,
        "Goblin Market": 6,
    },
    "Bone Bridge": {
        "Goblin Market": 2,
    },
    "Moon Bridge": {
        "Werewolf Den": 5,
        "Goblin Market": 3,
    },
    "Goblin Market": {
        "Vampire Tower": 5,
    },
    "Werewolf Den": {
        "Vampire Tower": 2,
    },
    "Vampire Tower": {},
}


def validate_haunted_map(graph: dict[str, dict[str, int]]) -> None:
    """Raise ValueError if the haunted map is invalid."""

    if not isinstance(graph, dict):
        raise ValueError("Graph must be a dictionary.")

    for node, neighbors in graph.items():

        if not isinstance(neighbors, dict):
            raise ValueError("Neighbors must be stored in a dictionary.")

        for neighbor, weight in neighbors.items():

            if neighbor not in graph:
                raise ValueError("Neighbor does not exist in graph.")

            if weight <= 0:
                raise ValueError("Edge weights must be positive.")


def monster_delivery_costs(
    graph: dict[str, dict[str, int]],
    start: str,
) -> dict[str, float]:
    """Return the cheapest delivery cost from start to every location."""

    validate_haunted_map(graph)

    if start not in graph:
        raise ValueError("Start location is missing.")

    # Initial costs
    costs = {node: inf for node in graph}
    costs[start] = 0

    # Priority queue
    heap = [(0, start)]

    while heap:
        current_cost, current_node = heapq.heappop(heap)

        # Skip outdated heap entries
        if current_cost > costs[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():

            new_cost = current_cost + weight

            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))

    return costs


def shortest_monster_delivery(
    graph: dict[str, dict[str, int]],
    start: str,
    target: str,
) -> tuple[float, list[str]]:
    """Return the cheapest cost and path from start to target."""

    if start not in graph or target not in graph:
        return (inf, [])

    if start == target:
        return (0, [start])

    validate_haunted_map(graph)

    costs = {node: inf for node in graph}
    previous = {}

    costs[start] = 0

    heap = [(0, start)]

    while heap:
        current_cost, current_node = heapq.heappop(heap)

        if current_node == target:
            break

        if current_cost > costs[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():

            new_cost = current_cost + weight

            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                previous[neighbor] = current_node

                heapq.heappush(heap, (new_cost, neighbor))

    # Unreachable target
    if costs[target] == inf:
        return (inf, [])

    # Reconstruct path
    path = []
    current = target

    while current != start:
        path.append(current)
        current = previous[current]

    path.append(start)
    path.reverse()

    return (costs[target], path)


def best_next_monster_stop(
    graph: dict[str, dict[str, int]],
    start: str,
    targets: list[str],
) -> tuple[str, float]:
    """Return the reachable target with the cheapest delivery cost."""

    if start not in graph:
        return ("", inf)

    costs = monster_delivery_costs(graph, start)

    best_target = ""
    best_cost = inf

    for target in targets:

        if target in costs and costs[target] < best_cost:
            best_target = target
            best_cost = costs[target]

    return (best_target, best_cost)


if __name__ == "__main__":

    print("Monster delivery costs:")
    print(monster_delivery_costs(HAUNTED_CITY, "Crypt Kitchen"))

    print()

    print("Shortest monster delivery:")
    cost, path = shortest_monster_delivery(
        HAUNTED_CITY,
        "Crypt Kitchen",
        "Vampire Tower",
    )

    print("Cost:", cost)
    print("Path:", path)

    print()

    print("Best next monster stop:")
    print(
        best_next_monster_stop(
            HAUNTED_CITY,
            "Crypt Kitchen",
            ["Werewolf Den", "Vampire Tower", "Ghost Harbor"],
        )
    )
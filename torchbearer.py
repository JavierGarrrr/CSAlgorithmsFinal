"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Javier Garcia Ramirez
Student ID:   828165956

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    TODO
    """
    return (
        "Why a single shortest-path run from S is not enough:\n"
        "The problem type requires shortest-path to visit a set of required nodes, not shortest paths from S to other nodes. A single shortest-path run would give you the most efficient ways to connect to other nodes from Start but not how to reach required nodes.\n"
        "What decision remains after all inter-location costs are known:\n"
        "Deciding the optimal order in which to visit locations.\n"
        "Why this requires a search over orders (one sentence):\n"
        "To find the best order you must compare all different order combinations because different orders of locations visited may yield different costs.\n"
    )


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    """
    sources_list = []
    sources_list.append(spawn)
    sources_list.extend(relics)
    #keeps unique sources only through set
    unique_sources = list(set(sources_list))
    return unique_sources


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    """
    #init
    pq = []
    dist = {key: float('inf') for key in graph}
    dist[source] = 0
    heapq.heappush(pq, (0, source))
    while(pq):
        cost, node = heapq.heappop(pq)
        if(cost > dist[node]):
            continue
        for neighbor, weight in graph[node]:
            total_dist = cost + weight
            if total_dist < dist[neighbor]:
                dist[neighbor] = total_dist
                heapq.heappush(pq, (total_dist, neighbor))
    return dist



def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.
    """
    sources = select_sources(spawn, relics, exit_node)
    sources_table = {}
    #find shortest path using all relics as sources
    for source in sources:
        sources_table[source] = run_dijkstra(graph, source)
    return sources_table

    


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    return (
    "For nodes already finalized (in S):\n"
    "The shortest distance possible to reach those nodes has been confirmed.\n"
    "For nodes not yet finalized (not in S):\n"
    "Shortest distance possible has not been found to reach that node, only the current known shortest distance.\n"
    "Initialization : why the invariant holds before iteration 1:\n"
    "Before the first iteration, the only node in S is the source with distance 0, and the rest of the node's known distances are set to INF. The invariant holds because the shortest distance to source can only be 0, and all the other nodes have not been explored so their distance is unknown (INF).\n"
    "Maintenance : why finalizing the min-dist node is always correct:\n"
    "Every discovered node's distance is calculated using the weight from previous node, and then pushed to a priority queue that sorts by lowest weight first. This means that for a graph with nonnegative edge weights, only the closest node with the guaranteed shortest distance is used leading to shortest path, since adding other node paths can only add more distance.\n"
    "Termination : what the invariant guarantees when the algorithm ends:\n"
    "The algorithm ends when the priority queue is empty, meaning all nodes have been finalized. The invariant guarantees the absolute shortest path to all finalized nodes.\n"
    "A correct route is built using multiple found shortest distances, so if the distances are incorrect the routing will also be incorrect.\n"
    )

# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    return (
        "The failure mode: Greedy only knows the optimal distances from current node to the next, not overall best path.\n"
        "Counter-example setup: say we have Source S and edges S-C (1), S-D(2), C-D(100), D-C (1), C-T (1) and D-T (1).\n"
        "What greedy picks: Greedy elects node C as next node to visit.\n"
        "What optimal picks: Optimal elects node D as the next node to visit.\n"
        "Why greedy loses: Starting at C forces greedy to take route S->C->D->T which is a total cost of (102) versus optimal route S->D->C->T (4), greedy doesn't consider how it's node order decisions affect the path later.\n"
        "The algorithm must consider all orders of required nodes visited, to yield the optimal path.\n"
    )

# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.
    """
    #init
    relics_remaining = set(relics)
    relics_visited_order =[]
    cost_so_far = 0
    best = [float('inf'), []]
    #run
    _explore(dist_table, spawn, relics_remaining, relics_visited_order, cost_so_far, exit_node, best)
    return best



def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    #base case
    if not relics_remaining:
        #include distance to last node
        total_cost = cost_so_far + dist_table[current_loc][exit_node]
        #update
        if(total_cost < best[0]):
            best[0] = total_cost
            best[1] = relics_visited_order
        return
    #If a solution has not reached the end and its current cost and the cheapest next move are greater than or equal to the best cost found, 
    # it by definition cannot beat the optimal solution, 
    lower_bound = cost_so_far + min(dist_table[current_loc][i] for i in relics_remaining)
    if(lower_bound >= best[0]):
        return 
    #go down list of relics
    for relic in list(relics_remaining):
        relics_remaining.remove(relic)
        relics_visited_order.append(relic)
        #recursive call to continue down path
        _explore(dist_table, relic, relics_remaining, relics_visited_order, cost_so_far + dist_table[current_loc][relic], exit_node, best)
        #backtrack
        relics_visited_order.pop()
        relics_remaining.add(relic)


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    #run algorithms
    dist_table = precompute_distances(graph, spawn, relics, exit_node)
    return find_optimal_route(dist_table, spawn, relics, exit_node)


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()

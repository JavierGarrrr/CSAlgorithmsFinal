# The Torchbearer

**Student Name:** Javier Garcia Ramirez
**Student ID:** 828165956
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
  _The problem type requires shortest-path to visit a set of required nodes, not shortest paths from S to other nodes. A single shortest-path run would give you the most efficient ways to connect to other nodes from Start but not how to reach required nodes._

- **What decision remains after all inter-location costs are known:**
  _Deciding the optimal order in which to visit locations._

- **Why this requires a search over orders (one sentence):**
  _To find the best order you must compare all different order combinations because different orders of locations visited may yield different costs._

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source |
|---|---|
| _S_ | _Required start node_ |
| _Rk_ | _Find optimal distances to to other required nodes_ |

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer |
|---|---|
| Data structure name | _dictionaries_ |
| What the keys represent | _source/destination nodes_ |
| What the values represent | _shortest distances to other nodes_ |
| Lookup time complexity | _O(1)_ |
| Why O(1) lookup is possible | _use unique keys to lookup single value for desired destination_ |

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** _Rk + 1_
- **Cost per run:** _O(m log n)_
- **Total complexity:** _O(m log n + k (m log n) )_
- **Justification (one line):** _Djikstra's runs once from source node and then runs once for each required node_

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  _The shortest distance possible to reach those nodes has been confirmed._

- **For nodes not yet finalized (not in S):**
  _Shortest distance possible has not been found to reach that node, only the current known shortest distance._

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  _Before the first iteration, the only node in S is the source with distance 0, and the rest of the node's known distances are set to INF. The invariant holds because the shortest distance to source can only be 0, and all the other nodes have not been explored so their distance is unknown (INF)._

- **Maintenance : why finalizing the min-dist node is always correct:**
  _Every discovered node's distance is calculated using the weight from previous node, and then pushed to a priority queue that sorts by lowest weight first. This means that for a graph with nonnegative edge weights, only the closest node with the guaranteed shortest distance is used leading to shortest path, since adding other node paths can only add more distance._

- **Termination : what the invariant guarantees when the algorithm ends:**
  _The algorithm ends when the priority queue is empty, meaning all nodes have been finalized. The invariant guarantees the absolute shortest path to all finalized nodes._

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

_A correct route is built using multiple found shortest distances, so if the distances are incorrect the routing will also be incorrect._

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** _Greedy only knows the optimal distances from current node to the next, not overall best path._
- **Counter-example setup:** _say we have Source S and edges S-C (1), S-D(2), C-D(100), D-C (1), C-T (1) and D-T (1)._
- **What greedy picks:** _Greedy elects node C as next node to visit._
- **What optimal picks:** _Optimal elects node D as the next node to visit._
- **Why greedy loses:** _Starting at C forces greedy to take route S->C->D->T which is a total cost of (102) versus optimal route S->D->C->T (4), greedy doesn't consider how it's node order decisions affect the path later._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _The algorithm must consider all orders of required nodes visited, to yield the optimal path._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._

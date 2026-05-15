# Development Log – The Torchbearer

**Student Name:** Javier Garcia Ramirez
**Student ID:** 828165956

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – [5/12/26]: Initial Plan

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

_I will work on the precomputation first, such as distance storage, the djikstra's algorithm and the source node list. These are the core mechanisms of the program so it is important that they function correctly before anything else. I plan to test them on a simple sample weighted graph. The parts I expect to be most difficult are 5 and 6, with keeping state and actually searching._

---

## Entry 2 – [5/12/26]: [precompute_distances bug]

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

_When testing code for Part 2 a-c, the program would throw a traceback error. It turns out in the precompute distances function, when calling run dijkstra for each source, I accidentally left the parameter field empty. After the fix, I verified that my code was working properly by running it on some test graphs._

---

## Entry 3 – [5/14/26]: [explore troubleshooting and pruning implentation]

_When working on explore, my first test full cost was off by 1. Reviewing my code, I realized that in my base case, I was leaving out the exit node distance in the total cost. After adding exit node distance all tests passed._

---

## Entry 4 – [5/14/26]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_I think I would create more strict test cases and edge cases to be more thorough. I think I would also maybe make pruning more explicit, checking all relic distances instead of just the shortest next one, although that implentation is correct._

---

## Final Entry – [5/14/26]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 30 mins |
| Part 2: Precomputation Design | 1 hr 15 min |
| Part 3: Algorithm Correctness | 30 min |
| Part 4: Search Design | 30 mins|
| Part 5: State and Search Space | 30 mins |
| Part 6: Pruning | 40 mins |
| Part 7: Implementation | 5 hr |
| README and DEVLOG writing | 2 hr |
| **Total** |9 hr 15 min|

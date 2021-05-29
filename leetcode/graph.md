# Graph

+ [Course Schedule II](#course-schedule-ii)
+ [Course Schedule](#course-schedule)
+ [Number of Islands](#number-of-islands)
+ [Is Graph Bipartite?](#is-graph-bipartite?)
+ [Cheapest Flights Within K Stops](#cheapest-flights-within-k-stops)
+ [Shortest Path in Binary Matrix](#shortest-path-in-binary-matrix)
+ [Maximum Depth of N-ary Tree](#maximum-depth-of-n-ary-tree)

## Course Schedule II

<https://leetcode.com/problems/course-schedule-ii/>

```python
from enum import Enum

class State(Enum):
  INIT = 0
  VISITING = 1
  VISITED = 2

class Solution:
  def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    ans = []
    graph = [[] for _ in range(numCourses)]
    state = [State.INIT] * numCourses

    for a, b in prerequisites:
      graph[b].append(a)

    def hasCycle(node: int) -> bool:
      if state[node] == State.VISITING:
        return True
      if state[node] == State.VISITED:
        return False

      state[node] = State.VISITING
      if any(hasCycle(child) for child in graph[node]):
        return True
      state[node] = State.VISITED
      ans.append(node)

      return False

    if any(hasCycle(i) for i in range(numCourses)):
      return []

    return ans[::-1]
```

## Course Schedule

<https://leetcode.com/problems/course-schedule/>

```python
from enum import Enum

class State(Enum):
  INIT = 0
  VISITING = 1
  VISITED = 2

class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = [[] for _ in range(numCourses)]
    state = [State.INIT] * numCourses

    for a, b in prerequisites:
      graph[b].append(a)

    def hasCycle(node: int) -> bool:
      if state[node] == State.VISITING:
        return True
      if state[node] == State.VISITED:
        return False

      state[node] = State.VISITING
      if any(hasCycle(child) for child in graph[node]):
        return True
      state[node] = State.VISITED

      return False

    return not any(hasCycle(i) for i in range(numCourses))
```

## Number of Islands

<https://leetcode.com/problems/number-of-islands/>

```python
def numIslands(self, grid: List[List[str]]) -> int:
  if not grid:
    return 0

  m = len(grid)
  n = len(grid[0])

  def dfs(i, j):
    if i < 0 or i == m or j < 0 or j == n:
      return
    if grid[i][j] != '1':
      return

    grid[i][j] = '2'  # mark '2' as visited
    dfs(i + 1, j)
    dfs(i - 1, j)
    dfs(i, j + 1)
    dfs(i, j - 1)

  ans = 0

  for i in range(m):
    for j in range(n):
      if grid[i][j] == '1':
        dfs(i, j)
        ans += 1

  return ans
```

## Is Graph Bipartite?

<https://leetcode.com/problems/is-graph-bipartite/>

```python
def isBipartite(self, graph):
  blank = 0
  red = 1
  green = 2
  n = len(graph)
  visited = [blank]*n
  print(visited)
  for i in range(n):
      if not visited[i]:
          que = deque([i])
          visited[i] = red
          while que:
              i = que.popleft()
              for j in graph[i]:
                  if visited[i] == visited[j]:
                      return False
                  if not visited[j]:
                      visited[j] = 3 - visited[i]
                      que.append(j)
  return True
```

## Cheapest Flights Within K Stops

<https://leetcode.com/problems/cheapest-flights-within-k-stops/>

```python
def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
  g = defaultdict(list)
  print(g)
  for f, t, p in flights:
      g[f].append((t, p))
  print(g)
  M = defaultdict(int)
  q = [(src, 0, 0)]
  r = float('inf')
  while q:
      t, w, p = q.pop(0)
      if p >= r or w > k+1:
          continue
      if t == dst:
          r = min(r, p)
      for n, np in g[t]:
          if M[n] == 0 or M[n] > p + np:
              M[n] = p + np
              q.append((n, w + 1, p + np))
  return r if r != float('inf') else -1
```

## Shortest Path in Binary Matrix

<https://leetcode.com/problems/shortest-path-in-binary-matrix/>

```python
def can_visit(self, i, j, grid, seen, n):
  if i >= 0 and i < n and j >= 0 and j < n and not grid[i][j] and (i,j) not in seen:
    return True
  return False
    
def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
  seen = set()
  n = len(grid)
  if grid[0][0] or grid[n-1][n-1]:
    return -1
  q = deque()
  q.append((0, 0, 1))
  seen.add((0, 0))
  directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
  while q:
    i, j, d = q.popleft()
    if i == n - 1 and j == n - 1:
      return d    
    for direc in directions:
      x = i + direc[0]
      y = j + direc[1]
      if self.can_visit(x, y, grid, seen, n):
        seen.add((x, y))
        q.append((x, y, d+1))
  return -1
```

## Maximum Depth of N-ary Tree

<https://leetcode.com/problems/maximum-depth-of-n-ary-tree/>

```python
def maxDepth(self, root: 'Node') -> int:
  if not root:
    return 0
  if not root.children:
    return 1

  return 1 + max(self.maxDepth(child) for child in root.children)
```

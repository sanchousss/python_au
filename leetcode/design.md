# Design

+ [Min Stack](#min-stack)
+ [Implement Queue using Stacks](#implement-queue-using-stacks)
+ [Implement Stack using Queues](#implement-stack-using-queues)
+ [Design Twitter](#design-twitter)

## Min Stack

<https://leetcode.com/problems/min-stack/>

```python
def __init__(self):
  self.stack = []

  def push(self, x: int) -> None:
    mini = x if not self.stack else min(self.stack[-1][1], x)
    self.stack.append([x, mini])

  def pop(self) -> None:
    self.stack.pop()

  def top(self) -> int:
    return self.stack[-1][0]

  def getMin(self) -> int:
    return self.stack[-1][1]
```

## Implement Queue using Stacks

<https://leetcode.com/problems/implement-queue-using-stacks/>

```python
def __init__(self):
    self.queue = []
        
 def push(self, x: int) -> None:
    self.queue.append(x)
def pop(self) -> int:
    if len(self.queue) < 1:
        return None
    return self.queue.pop(0) 
def peek(self) -> int:
    if len(self.queue) < 1:
        return None
    return self.queue[0] 
def empty(self) -> bool:
    if len(self.queue) == 0:
        return True
    return False
```

## Implement Stack using Queues

<https://leetcode.com/problems/implement-stack-using-queues/>

```python
def __init__(self):
    self.container=deque()
def push(self, x: int) -> None:
    self.container.append(x)
        
def pop(self) -> int:
    return self.container.pop()   
def top(self) -> int:
    return self.container[-1]     
def empty(self) -> bool:
    return len(self.container)==0
```

## Design Twitter

<https://leetcode.com/problems/design-twitter/>

```python
def __init__(self):
  self.timer = itertools.count(step=-1)
  self.tweets = defaultdict(deque)
  self.followees = defaultdict(set)

def postTweet(self, userId: int, tweetId: int) -> None:
  self.tweets[userId].appendleft((next(self.timer), tweetId))
  if len(self.tweets[userId]) > 10:
    self.tweets[userId].pop()

def getNewsFeed(self, userId: int) -> List[int]:
  tweets = list(heapq.merge(
      *(self.tweets[followee] for followee in self.followees[userId] | {userId})))
  return [tweetId for _, tweetId in tweets[:10]]

def follow(self, followerId: int, followeeId: int) -> None:
  self.followees[followerId].add(followeeId)

def unfollow(self, followerId: int, followeeId: int) -> None:
  self.followees[followerId].discard(followeeId)
```
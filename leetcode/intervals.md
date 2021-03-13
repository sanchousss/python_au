# Intervals

+ [Non-overlapping Intervals](#non-overlapping-intervals)
+ [Merge Intervals](#merge-intervals)
+ [Insert Intervals](#insert-interval)

## Non-overlapping Intervals

<https://leetcode.com/problems/non-overlapping-intervals/>

```python
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    if not intervals or len(intervals) == 1:
        return 0
    count = 0
    intervals.sort(key=lambda x:x[1])
    f = 0
    for s in range(1, len(intervals)):
        if intervals[f][1]>intervals[s][0]:
            count = count + 1
            s = s + 1
        else:
            f, s = s, s + 1
    return count
```

## Merge Intervals

<https://leetcode.com/problems/merge-intervals/>

```python
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    if not intervals or len(intervals) == 1:
        return intervals
    intervals.sort(key=lambda x:x[0])
    i = 0
    while i < len(intervals) - 1:
        if intervals[i][1]>=intervals[i+1][0]:
            intervals[i][1] = max(intervals[i+1][1], intervals[i][1])
            intervals.pop(i+1)
        else:
            i = i + 1
    return intervals
```

## Insert Intervals

<https://leetcode.com/problems/insert-interval/>

```python
def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    intervals.append(newInterval)
    if not intervals or len(intervals) == 1:
        return intervals
    intervals.sort(key=lambda x:x[0])
    i = 0
    while i < len(intervals) - 1:
        if intervals[i][1]>=intervals[i+1][0]:
            intervals[i][1] = max(intervals[i+1][1], intervals[i][1])
            intervals.pop(i+1)
        else:
            i = i + 1
    return intervals

```

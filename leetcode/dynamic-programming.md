# Dynamic Programming

+ [House Robber](#house-robber)
+ [House Robber II](#house-robber-ii)

## House Robber

<https://leetcode.com/problems/house-robber/>

```python
def rob(self, nums: List[int]) -> int:
  prev1 = 0  # dp[i - 1]
  prev2 = 0  # dp[i - 2]

  for num in nums:
    dp = max(prev1, prev2 + num)
    prev2 = prev1
    prev1 = dp

  return prev1
```

## House Robber II

<https://leetcode.com/problems/house-robber-ii/>

```python
def rob(self, nums: List[int]) -> int:
  def rob(l: int, r: int) -> int:
    dp1 = 0
    dp2 = 0

    for i in range(l, r + 1):
      temp = dp1
      dp1 = max(dp1, dp2 + nums[i])
      dp2 = temp

    return dp1

  if not nums:
    return 0
  if len(nums) < 2:
    return nums[0]

  return max(rob(0, len(nums) - 2), rob(1, len(nums) - 1))
```
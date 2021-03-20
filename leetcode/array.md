# Array

+ [Max Consecutive Ones](#max-consecutive-ones)
+ [Reshape the Matrix](#reshape-the-matrix)
+ [Image Smoother](#image-smoother)
+ [Flipping an Image](#flipping-an-image)
+ [Transpose Matrix](#transpose-matrix)
+ [Move Zeroes](#move-zeroes)
+ [Squares of a Sorted Array](#squares-of-a-sorted-array)

## Max Consecutive Ones

<https://leetcode.com/problems/max-consecutive-ones/>

``` python
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    ans = 0
    sum = 0

    for num in nums:
      if num == 0:
        sum = 0
      else:
        sum += num
        ans = max(ans, sum)

    return ans
```

## Reshape the Matrix

<https://leetcode.com/problems/reshape-the-matrix/>

``` python
def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
    if nums == [] or r * c != len(nums) * len(nums[0]):
      return nums

    ans = [[0 for j in range(c)] for i in range(r)]
    k = 0

    for row in nums:
      for num in row:
        ans[k // c][k % c] = num
        k += 1

    return ans
```

## Image Smoother

<https://leetcode.com/problems/image-smoother>

``` python
def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
    m = len(M)
    n = len(M[0])

    ans = [[0 for j in range(n)] for i in range(m)]

    for i in range(m):
      for j in range(n):
        ones = 0
        count = 0
        for y in range(max(0, i - 1), min(m, i + 2)):
          for x in range(max(0, j - 1), min(n, j + 2)):
            ones += M[y][x]
            count += 1
        ans[i][j] = ones // count

    return ans
```

## Flipping an Image

<https://leetcode.com/problems/flipping-an-image/>

``` python
def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    for row in A:
      for i in range((len(row) + 1) // 2):
        row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1

    return A
```

## Transpose Matrix

<https://leetcode.com/problems/transpose-matrix/>

``` python
def transpose(self, A: List[List[int]]) -> List[List[int]]:
    ans = [[0] * len(A) for _ in range(len(A[0]))]

    for i in range(len(A)):
      for j in range(len(A[0])):
        ans[j][i] = A[i][j]

    return ans
```

## Move Zeroes

<https://leetcode.com/problems/move-zeroes/>

``` python
def moveZeroes(self, nums: List[int]) -> None:
    j = 0
    for num in nums:
      if num != 0:
        nums[j] = num
        j += 1

    for i in range(j, len(nums)):
      nums[i] = 0
```

## Squares of a Sorted Array

<https://leetcode.com/problems/squares-of-a-sorted-array/>

``` python
def sortedSquares(self, A: List[int]) -> List[int]:
    n = len(A)
    l = 0
    r = n - 1
    ans = [0] * n

    while n:
      n -= 1
      if abs(A[l]) > abs(A[r]):
        ans[n] = A[l] * A[l]
        l += 1
      else:
        ans[n] = A[r] * A[r]
        r -= 1

    return ans
```

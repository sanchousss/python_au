# Math

+ [Reverse Integer](#reverse-integer)
+ [Palindrome Number](#palindrome-number)
+ [Fizz Buzz](#fizz-buzz)
+ [Base 7](#base-7)
+ [Fibonacci Number](#fibonacci-number)
+ [Largest Perimeter Triangle](#largest-perimeter-triangle)
+ [Sqrt(x)](#sqrtx)

## Reverse Integer

<https://leetcode.com/problems/reverse-integer/>

```python
def reverse(self, x: int) -> int:
    a = 0
    t = x
    if x < 0:
        x = x*(-1)
    while x > 0:
        a = a*10 + x%10
        x = x // 10
    if t < 0:
        a = a*(-1)
    if (a > 2147483647) or (a < -2147483648):
        return 0
    return a
```

## Palindrome Number

<https://leetcode.com/problems/palindrome-number/>

``` python
def isPalindrome(self, x: int) -> bool:
    if x < 0:
        return False
    rev = 0
    y = x
    while y:
        rev = rev * 10 + y % 10
        y //= 10
    return rev == x
```

## Fizz Buzz

<https://leetcode.com/problems/fizz-buzz/>

``` python
def fizzBuzz(self, n):
    ans = []

    for num in range(1,n+1):

        divisible_by_3 = (num % 3 == 0)
        divisible_by_5 = (num % 5 == 0)

        if divisible_by_3 and divisible_by_5:
            ans.append("FizzBuzz")
        elif divisible_by_3:
            ans.append("Fizz")
        elif divisible_by_5:
            ans.append("Buzz")
        else:
            ans.append(str(num))

        return ans
```

## Base 7

<https://leetcode.com/problems/base-7/>

``` python
def convertToBase7(self, num: int) -> str:
    new_int = ''
    k = 1
    if num < 0:
        num = num * -1
        k = -1
    if num == 0:
        return '0'
    else:
        while num != 0:
            new_int = new_int + str(num % 7)
            num = num // 7
        new_int = new_int[::-1]
        return(str(int(new_int)*k))
```

## Fibonacci Number

<https://leetcode.com/problems/fibonacci-number/>

``` python
def fib(self, N: int) -> int:
    if N <= 1:
        return N
    return self.fib(N-1) + self.fib(N-2)
```

## Largest Perimeter Triangle

<https://leetcode.com/problems/largest-perimeter-triangle/>

``` python
def largestPerimeter(self, A: List[int]) -> int:
    A = sorted(A)

    for i in range(len(A) - 1, 1, -1):
      if A[i - 2] + A[i - 1] > A[i]:
        return A[i - 2] + A[i - 1] + A[i]

    return 0
```

## Sqrt(x)

<https://leetcode.com/problems/sqrtx/>

``` python
def mySqrt(self, x: int) -> int:
    return int(math.sqrt(x))
```

# String

+ [Valid Anagram](#valid-anagram)
+ [Reverse String](#reverse-string)
+ [Reverse Vowels of a String](#reverse-vowels-of-a-string)
+ [Reverse Words in a String III](#reverse-words-in-a-string-iii)
+ [To Lower Case](#to-lower-case)

## Valid Anagram

<https://leetcode.com/problems/valid-anagram>

``` python
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False

    dict = Counter(s)

    for c in t:
      dict[c] -= 1
      if dict[c] < 0:
        return False

    return True
```

## Reverse String

<https://leetcode.com/problems/reverse-string/>

``` python
def reverseString(self, s: List[str]) -> None:
    l = 0
    r = len(s) - 1

    while l < r:
      s[l], s[r] = s[r], s[l]
      l += 1
      r -= 1
```

## Reverse Vowels of a String

<https://leetcode.com/problems/reverse-vowels-of-a-string/>

``` python
def reverseVowels(self, s: str) -> str:
    charList = list(s)
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    l = 0
    r = len(s) - 1

    while l < r:
      while l < r and charList[l] not in vowels:
        l += 1
      while l < r and charList[r] not in vowels:
        r -= 1
      charList[l], charList[r] = charList[r], charList[l]
      l += 1
      r -= 1

    return ''.join(charList)
```

## Reverse Words in a String III

<https://leetcode.com/problems/reverse-words-in-a-string-iii/>

``` python
def reverseWords(self, s: str) -> str:
    d = s.split()
    new_str = ''
    
    if s == '':
        return ''
    else:
        for i in range(len(d)-1):
            d[i] = d[i][::-1]
            new_str = new_str + str(d[i]) + ' '
        d[len(d)-1] = d[len(d)-1][::-1]
        new_str = new_str + str(d[len(d)-1])
        return new_str
```

## To Lower Case

<https://leetcode.com/problems/to-lower-case/>

``` python
def toLowerCase(self, str):
    return(str.lower())
```

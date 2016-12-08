# Scrabble - Week 1 - @washt

Given a set of 7 letters and a word, determine if you can make the given word using the tiles, i.e.:

```python
scrabble('sckreah', 'hackers') # true
scrabble('dudesuh', 'suhdude') # true
scrabble('corsmom', 'carboat') # false
scrabble('abcdefg', 'lolrofl') # false
```


Test cases will be read in from a challenge.txt, arranged as an N by 2 matrix with
the scrambled letters in the left column and the target word on the right, i.e.:

| Scrambled | Target |
|-----------|:------:|
| rehsack   | hackers|
| ...       | ...    |
| corsmom   |carboat |

Please have your program write to STDOUT or solution.txt file in your root directory.

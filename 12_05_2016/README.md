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

| Scrambled | Target | Truth |
|-----------|:------:|:-----:|
| rehsack   | hackers| True  |
|   ...     |  ...   |  ...  |
| corsmom   |carboat | False |

You can build a local challenge set from the provided challenge.txt, or build your own
by piping a list of random words:

```bash
$ cat /usr/share/dict/words | grep -o -w '\w\{3,7\}' | sort -R | head -n 100 | python buildchallenge.py >> challenge.txt
```

Please have your program write to STDOUT or solution.txt file in your root directory.

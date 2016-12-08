import sys
import random
import string

def buildUnmatchedWord(word):
    tail = word[-1]
    unmatched = []

    while len(unmatched) < 7:
        letter = random.choice(string.ascii_letters.lower())
        if letter != tail:
            unmatched.append(letter)

    return ''.join(unmatched)

def pipeOut(testCases):
    for i in testCases:
        sys.stdout.write(i[0] + " " + i[1] + " " + str(i[2]) + "\n")

def main():
    '''
     Run by piping a random list of words with a specfied length:
     `$ cat /usr/share/dict/words | grep -o -w '\w\{3,7\}' | sort -R | head -n 100 | python buildchallenge.py >> challenge.txt`
     If you're on osx, you may need to install `coreutils` in order to use sort.
     Make sure your path is exported, i.e.:
       PATH="/usr/local/opt/coreutils/libexec/gnubin:$PATH"
       Otherwise you will need to replace the above command with `gsort`
    '''
    count=0
    testPairs = []
    # build scrambled words in testPairs, with the format (scrambledWord, targetWord)
    for line in sys.stdin:
        word = line.strip('\n').lower()
        # scrambledWord that can form the target
        if count % 3 == 0:

            # We add random letters to scrambledWord if target < 7
            if len(word) < 7:
                extraLetters = []
                diff = 7 - len(word)

                for i in range(diff):
                    extraLetters.append(random.choice(string.ascii_letters).lower())

                scrambled = ''.join(random.sample(word, len(word)) + extraLetters)
                testPairs.append((scrambled, word, True))

            else:
                scrambled = ''.join(random.sample(word, len(word)))
                testPairs.append((scrambled, word, True))

        # scrambledWord that cannot be made from scrambled words
        else:
            noWord = buildUnmatchedWord(word)
            testPairs.append((noWord, word, False))

        count +=1

    pipeOut(testPairs)

if __name__ == "__main__":
    main()

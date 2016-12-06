import sys
import random
import string

# λ →  cat /usr/share/dict/words | grep -o -w '\w\{3,7\}' | python buildchallenge.py
if __name__ == "__main__":
        count=0
        testPairs = []
        for line in sys.stdin:
                # build scrambled word, adding random letters if target < 7
                if count % 100 == 0:
                        word = line.strip('\n').lower()
                        if len(line) < 7:
                                extraLetters = []
                                diff = 7 - len(line)
                                for i in xrange(0,diff):
                                        extraLetters.append(random.choice(string.ascii_letters).lower())
                                scrambled = ''.join(random.sample(word, len(word)) + extraLetters)
                                print True, str(len(scrambled)), scrambled, ' ' + word
                        else:
                                scrambled = ''.join(random.sample(word, len(word)))
                                testPairs.append((scrambled, word))
                                print True, str(len(scrambled)), ' ' + scrambled, ' ' + word
                        #sys.stdout.write(scrambled + " " + line)
                count+=1

#        print testPairs

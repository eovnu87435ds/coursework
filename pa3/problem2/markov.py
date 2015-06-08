import sys
import collections
import random

# initialization
NPREF = 2
NONWORD = "\n"
MAXGEN = 10000
statetab = {}  # dictionary for mapping prefixes to suffixes
testset = set()  # set for testing
prefix = collections.deque([NONWORD] * NPREF)  # deque

# build
for line in sys.stdin:
    for word in line.split():
        # append word to suffix list or create list if not yet created; 'tuple' for "hashability" for dictionary
        statetab.setdefault(tuple(prefix), []).append(word)
        testset.add(tuple(prefix))  # add prefix to test set so that its occurence can be tested later
        prefix.rotate(-1)  # rotate one left
        prefix[-1] = word  # overwrite last entry
statetab.setdefault(tuple(prefix), []).append(NONWORD)

# generate
prefix = collections.deque([NONWORD] * NPREF)
for i in range(MAXGEN):
    suf = statetab[tuple(prefix)]
    w = suf[random.randrange(0, len(suf))]
    if w == NONWORD:
        break
    if not tuple(prefix) in testset:
        print("Internal error: generated prefix not found in original data!")
        break
    print(w)
    prefix.rotate(-1)
    prefix[-1] = w

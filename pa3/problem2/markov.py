import sys
import collections
import random

# initialization
NPREF = 2
NONWORD = "\n"
MAXGEN = 10000
statetab = {}  # dictionary
prefix = collections.deque([NONWORD] * NPREF)  # deque

# build
for line in sys.stdin:
    for word in line.split():
        # append word to suffix list or create list if not yet created; 'tuple' for "hashability" for dictionary
        statetab.setdefault(tuple(prefix), []).append(word)
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
    print(w, end=' ')
    prefix.rotate(-1)
    prefix[-1] = w

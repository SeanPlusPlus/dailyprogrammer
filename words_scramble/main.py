#!/usr/bin/env python

import itertools
from collections import defaultdict

def main():

    with open('words.txt') as f:
        words_set = set(line.strip() for line in f)

    words = defaultdict(lambda:None)
    li = [
      'mkeart',
      'sleewa',
      'edcudls',
      'iragoge',
      'usrlsle',
      'nalraoci',
      'nsdeuto',
      'amrhat',
      'inknsy',
      'iferkna'
    ]

    for word in li:
        perms = (''.join(i) for i in itertools.permutations(word, len(word)))
        try:
            words[word] = itertools.dropwhile(lambda x: not x in words_set, perms).next()
        except StopIteration:
            print("Didn't find `%s' in words.txt" % word)

    print words

if __name__ == '__main__':
    main()

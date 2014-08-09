#!/usr/bin/env python

import itertools
from collections import defaultdict

def main():

    words_set = set()
    with open('words.txt') as f:
        words_set = set(line.strip() for line in f)

    words = defaultdict(lambda:None)
    li = [
      'keart',
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
        for i in itertools.permutations(word, r=len(word)):
            s = ''.join(i)
            if s in words_set:
                words[word] = s
                break

    print words

if __name__ == '__main__':
    main()

#!/usr/bin/env python

import itertools

def main():

    with open('words.txt') as f:
        words_set = set(line.strip() for line in f)

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

    def descramble(w):
        perms = (''.join(i) for i in itertools.permutations(w, len(w)))
        try:
            return itertools.dropwhile(lambda x: not x in words_set, perms).next()
        except StopIteration:
            return None

    words = dict([(word, descramble(word)) for word in li])
    print(words)

if __name__ == '__main__':
    main()

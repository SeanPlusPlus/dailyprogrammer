#!/usr/bin/env python

import itertools
from collections import defaultdict

def main():

    words_set = set()
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

    def is_not_in_words_set(tu):
        print ''.join(tu)
        return not ''.join(tu) in words_set

    for word in li:
        perms = itertools.permutations(word, len(word))
        try:
            it = itertools.dropwhile(is_not_in_words_set, perms)
            words[word] = it.next()
        except StopIteration:
            raise

        # for i in itertools.permutations(word, r=len(word)):
        #     s = ''.join(i)
        #     if s in words_set:
        #         words[word] = s
        #         break

    print words

if __name__ == '__main__':
    main()

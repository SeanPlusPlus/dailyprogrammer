#!/usr/bin/env python

import itertools

def main():

    words_set = set()
    with open('words.txt') as f:
        words_set = set(line.strip() for line in f)

    words = {
      'keart': None,
      'sleewa': None,
      'edcudls': None,
      'iragoge': None,
      'usrlsle': None,
      'nalraoci': None,
      'nsdeuto': None,
      'amrhat': None,
      'inknsy': None,
      'iferkna': None
    }

    for word in words:
        for i in itertools.permutations(word, r=len(word)):
            s = ''.join(i)
            if s in words_set:
                words[word] = s
                break

    print words

if __name__ == '__main__':
    main()

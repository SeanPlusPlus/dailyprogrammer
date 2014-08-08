#!/usr/bin/env python

from random import randint

def bisect(start, end):
   return int((start + end) / 2)

def calc(lower, mid, upper):
    question = 'Is the num [h]igher, [l]ower, or [e]xactly ' + str(mid) + ': '
    direction = str(raw_input(question))

    if direction == 'h':
      calc(mid, bisect(mid, upper), upper)

    elif direction == 'l':
      calc(lower, bisect(lower, mid) ,mid)

    elif direction == 'e':
      print 'got it!'

    else:
      print 'no dice'


def main():
    lower = 1
    upper = 100
    randNumber = randint(lower, upper)
    print 'The Random Number Is: ' + str(randNumber) + '\n'
    calc(lower, 50, upper)


if __name__ == '__main__':
    main()

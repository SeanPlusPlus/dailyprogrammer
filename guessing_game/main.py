#!/usr/bin/env python

from random import randint

def bisect(start, end):
   return int((start + end) / 2)

def calcRecur(lower, upper):
    question = 'Is the num [h]igher, [l]ower, or [e]xactly ' + str(bisect(lower, upper)) + ': '
    direction = str(raw_input(question))

    if direction == 'h':
      calcRecur(bisect(lower, upper), upper)

    elif direction == 'l':
      calcRecur(lower, bisect(lower, upper))

    elif direction == 'e':
      print 'got it!'

    else:
      print 'no dice'

def calcIter(lower, upper):
    mid = bisect(upper, lower)

    while(True):
        question = 'Is the num [h]igher, [l]ower, or [e]xactly ' + str(mid) + ': '
        direction = str(raw_input(question))

        if direction == 'h':
            lower = mid
            mid = bisect(mid, upper)

        elif direction == 'l':
            upper = mid
            mid = bisect(lower, mid)

        elif direction == 'e':
            print 'got it!'
            break

        else:
            print 'no dice'

def main():
    lower = 1
    upper = 100
    randNumber = randint(lower, upper)
    print 'The Random Number Is: ' + str(randNumber) + '\n'
    calcRecur(lower, upper)
    calcIter(lower, upper)


if __name__ == '__main__':
    main()

#!/usr/bin/env python

from random import randint
import timeit
from math import factorial

def bisect(start, end):
    return int((start + end) / 2)

def calcRecur(lower, upper, ans=None):

    mid = bisect(lower, upper)
    if mid == ans:
        print 'got it'
        return

    if mid < ans:
        print mid
        calcRecur(mid, upper, ans=ans)

    else:
        print mid
        calcRecur(lower, mid, ans=ans)

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
    upper = factorial(100)
    randNumber = randint(lower, upper)
    print 'The Random Number Is: ' + str(randNumber) + '\n'

    calcRecur(lower, upper, ans=randNumber)
    #calcIter(lower, upper)


if __name__ == '__main__':
    main()

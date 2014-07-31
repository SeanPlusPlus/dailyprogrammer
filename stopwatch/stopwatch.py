#!/usr/bin/env python

# http://www.reddit.com/r/dailyprogrammer/comments/pjsdx/difficult_challenge_2/

# Your mission is to create a stopwatch program.

# This program should have start, stop, and lap options,
# and it should write out to a file to be viewed later.

import time

def procedure():
    time.sleep(1.0)

def stopwatch():
    start = time.clock()
    for i in range(1,10):
      print i
      procedure()


def main():
    stopwatch()

if __name__ == '__main__':
    main()

#!/usr/bin/env python

# http://www.reddit.com/r/dailyprogrammer/comments/pjsdx/difficult_challenge_2/

# Your mission is to create a stopwatch program.

# This program should have start, stop, and lap options,
# and it should write out to a file to be viewed later.

import time
import signal
import sys

def kill_stopwatch(signal, frame):
    print 'Stopwatch Stopped'
    sys.exit(0)

def stopwatch():
    signal.signal(signal.SIGINT, kill_stopwatch)
    count = 0
    while(True):
        time.sleep(1.0)
        count += 1
        print count

def main():
    stopwatch()

if __name__ == '__main__':
    main()

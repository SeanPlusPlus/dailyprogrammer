#!/usr/bin/env python

from __future__ import print_function
import time
import signal
import select
import tty
import termios
import time
import sys
from datetime import datetime
from curses import ascii

def main():

    # Found this helpful for capturing user input at arbitrary times in python
    # http://stackoverflow.com/questions/3731681/capturing-user-input-at-arbitrary-times-in-python

    def isData():
        return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

    old_settings = termios.tcgetattr(sys.stdin)
    try:
        tty.setcbreak(sys.stdin.fileno())

        # open file
        now = datetime.now().strftime('%Y-%m-%d-%M-%s')
        f = open('stopwatch-' + now,'w')
        f.write('hi there\n')
        f.close()

        # main loop
        # pressing the key "l" will make a new lap
        # pressing the excape key stops the stopwatch
        i = 1
        while 1:
            time.sleep(1.0)
            print(i)
            i += 1

            if isData():
                c = sys.stdin.read(1)
                if c == 'l':
                  print('lap')
                  i = 1
                if c == chr(ascii.ESC):
                    break

    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

if __name__ == '__main__':
    main()

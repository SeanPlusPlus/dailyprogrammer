#!/usr/bin/env python
import datetime as dt

def main():
    today   = dt.datetime.today()
    nyeStr  = str(dt.datetime.today().year + 1) + '-1-1-0-0-0'
    nyeDate = dt.datetime.strptime(nyeStr, '%Y-%m-%d-%H-%M-%S')

    print(nyeDate - today)

if __name__ == '__main__':
    main()

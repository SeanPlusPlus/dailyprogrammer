#!/usr/bin/env python
# find perfect numbers

import math

def is_prime(n):
    rooted = int(math.sqrt(n))
    for i in range(2, rooted):
        if n % i == 0:
            return False
    return True

def main():

    primes = []
    with open('primes.txt','r') as f:
        output = f.read().split('\n')
        for o in output:
            numList = o.split(' ')
            for n in numList:
                try:
                    prime = int(n)
                    primes.append(prime)
                except(ValueError):
                    continue

    for p in primes:
        if p < 59:
            x = (pow(2,p) - 1)
            if is_prime(x):
                print 'exponent: ' + str(p)
                y = (pow(2,(p-1)))
                print 'perfect:  ' + str(x * y)  + '\n'
            else:
                print '*** NOT PRIME  *** '
                print 'exponent: ' + str(p)
                print 'x: ' + str(x) + '\n'

if __name__ == '__main__':
    main()

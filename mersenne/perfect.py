#!/usr/bin/env python

# find perfect numbers

def is_prime(n):
    for i in range(2, n):
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

    primes = [2,3,5,7]

    for p in primes:
      x = (pow(2,p) - 1)
      if is_prime(x):

          print 'exponent: ' + str(p)

          y = (pow(2,(p-1)))
          print 'perfect:  ' + str(x * y)  + '\n'


if __name__ == '__main__':
    main()

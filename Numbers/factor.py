"""
Find prime factors of a number, a bit of a naive implementation.
Author: Jimmy Zuber
"""
import math

# returns list containing prime factors of a number in ascending order
# returns [n] if n is prime
def prime_factors(n):
    factors = []
    n = float(n)
    m = int(math.ceil(n / 2)) + 1
    isPrime = [True for x in range(0, m)]

    isPrime[0] = isPrime[1] = False
    for i in xrange(2, m):
        v = i
        while v + i < m:
            v += i
            isPrime[v] = False

    primes = []
    for i, p in enumerate(isPrime):
        if p:
            primes.append(i)

    for i in primes:
        temp = n
        while True:
            temp = temp / i
            if temp == int(math.ceil(temp)):
                factors.append(int(i))
            else:
                break

    if len(factors) == 0:
        return [int(n)]

    return factors

def main():
    while True:
        try:
            n = int(raw_input("Enter a number to be factored: "))
            if n > 0:
                break
        except:
            "Not an integer"

        print "Please enter a number greater than 1"

    print prime_factors(n)

main()


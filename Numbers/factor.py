"""
Find prime factors of a number.
Author: Jimmy Zuber
"""
import math

# returns list containing prime factors of a number in ascending order
# returns [n] if n is prime
def prime_factors(n):
    factors = []
    sqrt = math.sqrt(n)

    # only need to go until n = 1
    i = 2
    while n > 1:
        while n % i == 0:
            n = n / i
            factors.append(i)
        i += 1
        if i > sqrt:
            break

    if len(factors) == 0:
        factors.append(n)
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


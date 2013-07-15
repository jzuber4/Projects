"""
Find prime numbers until the user stops asking for the next one.
Verified correct for first 10,000 primes: primes.utm.edu/lists/small/10000.txt
Author: Jimmy Zuber
"""

# Expands an (ordered) list of primes in [2, last_max]
# to contain primes up to last_max * 2.
# Uses prime sieving technique.
def expand_list(prime_list, last_max):
    # start small and double
    if last_max < 2:
        last_max = 2
        prime_list = [2]

    sieve = [True] * last_max

    newstart = last_max + 1
    for i in prime_list:

        # start at beginning of sieve
        t = (newstart / i) * i # earliest multiple of i
        t -= newstart # convert indices (sieve[0] is primality of newstart)
        # no negative indices
        if t < 0:
            t += i

        while t < len(sieve):
            sieve[t] = False
            t += i

    # add new primes to list
    for i, p in enumerate(sieve):
        if p:
            prime_list.append(i + last_max + 1)

    # list and last checked number
    return prime_list, len(sieve) + last_max

def main():
    primes = []
    last_max = 0
    curr = 0
    # print prime numbers until user stops asking for more
    while True:
        choice = raw_input("Print next prime number (y/n)?: ")
        if choice == "y":
            if len(primes) == curr:
                primes, last_max = expand_list(primes, last_max)
            print primes[curr]
            curr += 1
        elif choice == "n":
            break
        else:
            print "Enter 'y' or 'n' to choose."

main()




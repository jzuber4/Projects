"""
Validates credit card numbers (Visa, MasterCard, American Express, and Discover) by looking at their checksums.
Author: Jimmy Zuber
"""
import sys

# Applies Luhn formula
def main():
    if len(sys.argv) != 2:
        print "usage: python credit_card.py number"
        return

    # parse to int list
    num = [int(k) for k in sys.argv[1]]

    # Go through string in reverse order starting from second to last
    for i in range (len(num) - 2, -1, -2):
        num[i] *= 2
        if num[i] > 9:
            num[i] -= 9

    print not sum(num) % 10

main()

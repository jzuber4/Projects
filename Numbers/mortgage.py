"""
Calculate the monthly payments of a fixed term mortage for P dollars over N terms at an interest rate r (term percentage). P, N, and r are arguments 1, 2, and 3.
The original prompt from the list did not make much sense, since a fixed term mortgage, by definition, takes a given amount of time to pay off.
All in all, this is more of an exercise in money management than programming :).
Formula from: en.wikipedia.org/wiki/Fixed-rate_mortgage
Author: Jimmy Zuber
"""
import sys

def main():
    if len(sys.argv) < 4:
        print "usage: python mortgage.py Principal Years Interest"
        return
    try:
        P, N, r = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
    except:
        print "P, N, and r must be numbers."
        return

    # percentage -> fraction
    r /= 100
    # years -> months
    N *= 12
    r /= 12

    val = r * P / (1 - ((1 + r) ** -N))
    print "Monthly payment = %.2f" % val

main()

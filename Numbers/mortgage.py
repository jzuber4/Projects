"""
Calculate the monthly payments of a fixed term mortage for P dollars over N terms at an interest rate r (term percentage). P, N, and r are arguments 1, 2, and 3.
The original prompt from the list did not make much sense, since a fixed term mortgage, by definition, takes a given amount of time to pay off.
All in all, this is more of an exercise in money management than programming :).
Formula from: en.wikipedia.org/wiki/Fixed-rate_mortgage
Author: Jimmy Zuber
"""
import sys

def main():
    # life is too short to write input validation code for toy projects
    # but I do it anyway :)
    if len(sys.argv) < 4:
        print "usage: python mortgage.py P N r"
        return
    try:
        P, N, r = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
    except:
        print "P, N, and r must be numbers."
        return

    # percentage -> fraction (should already be in term form)
    # i.e. monthly, not yearly fraction if payments are monthly
    r /= 100

    val = r * P / (1 - ((1 + r) ** -N))
    print "Monthly payment =", val

main()

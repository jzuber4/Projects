"""
Prints the first n digits of pi.
Verified up to 10,000 digits, see: (from http://www.geom.uiuc.edu/~huberty/math5337/groupe/digits.html)
Author: Jimmy Zuber
"""
from decimal import *
import math

"""
Asks the user for the number of digits to be calculated.
"""
def user_input():
    while True:
        precision_str = raw_input('Generate Pi to digit #: ')
        try:
            precision = int(precision_str)
            break
        except:
            print 'Please input an integer greater than 0'

    return precision

"""
Calculate pi to 'precision' number of digits.
Returns a Decimal object containing pi precise to 'precision' digits
Uses Gauss-Legendre algorithm: en.wikipedia.org/wiki/Gauss-Legendre_algorithm
"""
def calculate_pi(precision):

    # guard against rounding errors
    getcontext().prec = precision + 10

    a_prev = Decimal('1')
    b_prev = Decimal('1') / Decimal('2').sqrt()
    t_prev = Decimal('0.25')
    p_prev = Decimal('1')

    # digits of precision essentially double each iteration
    # Again, use extra iterations to make sure
    for i in xrange(int(math.sqrt(precision) + 2)):
        a_next = (a_prev + b_prev) / Decimal('2')
        b_next = (a_prev * b_prev).sqrt()
        t_next = t_prev - p_prev * (a_prev - a_next) ** Decimal('2')
        p_next = Decimal('2') * p_prev

        a_prev, b_prev, t_prev, p_prev = Decimal(a_next), Decimal(b_next), Decimal(t_next), Decimal(p_next)


    result = ((a_next + b_next) ** Decimal('2')) / (Decimal('4') * t_next)

    # dirty quantize (yes I know there is one already)
    return str(result)[:precision+1]

def main():
    precision = user_input()
    result = calculate_pi(precision)
    print result

main()


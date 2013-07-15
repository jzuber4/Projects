"""
Binary to decimal and decimal to binary converter. Doesn't use pre-made libraries (since that would complete the whole assignment).
Author: Jimmy Zuber
"""
import sys

def main():
    if len(sys.argv) < 3 or sys.argv[1] != 'b' and sys.argv[1] != 'd':
        print "usage: python binary_decimal.py option amount"
        print "option = 'b' for binary to decimal"
        print "         'd' for decimal to binary"
        return

    isDecimal = sys.argv[1] == 'd'
    number = sys.argv[2]
    valid_nums = {}

    if isDecimal:
        max_nums = 9
    else:
        max_nums = 1

    for k in range(max_nums + 1):
        valid_nums[str(k)] = True

    for c in number:
        if not c in valid_nums:
            print "Incorrect number or base"
            return

    if isDecimal:
        # turn decimal string into binary
        # big endian
        number = int(number)
        power = 0
        # find highest binary power
        while 2 ** (power + 1) < number:
            power += 1

        bin_string = ""
        while number > 0:
            # if digit fits, must be 1
            digit = 2 ** power
            if digit <= number:
                number -= digit
                bin_string += "1"
            else:
                bin_string += "0"
            power -= 1
        print bin_string

    else:
        # big endian
        decimal = 0
        power = len(number) - 1
        for i in number:
            if i == "1":
                decimal += 2 ** power
            power -= 1
        print decimal

main()

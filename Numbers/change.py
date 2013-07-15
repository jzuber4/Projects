"""
Change! Albeit less political.
Uses 'greedy' algorithm (doesn't calculate based on availability or other fanciness)
Calculates change for a given dollar amount and cost.
"""
import sys

def main():
    if(len(sys.argv) < 3):
        print "usage: python change.py paid cost"
        return
    try:
        paid, cost = float(sys.argv[1]), float(sys.argv[2])
    except:
        print "Enter numbers for paid and cost"
        return

    # integers are just oh so easier
    # and who's gonna notice if I take fractions of cents? - Office Space
    paid, cost = int(100 * paid), int(100 * cost)
    paid -= cost

    # names and amounts for possible change
    money_units = [10000, 5000, 2000, 1000, 500, 100, 25, 10, 5, 1]
    money_types = {25:'Quarters', 10:'Dimes', 5:'Nickels', 1:'Pennies'}
    change = []

    # greedily pick the highest available change unit
    temp = paid
    for m in money_units:
        amount = temp / m
        temp -= amount * m
        change.append(amount)
        if temp == 0:
            break

    # print change and units with formatting
    print "change = %d.%02d" % (paid / 100, paid % 100)
    for i, v in enumerate(change):
        if v == 0:
            continue
        k = money_units[i]
        money_type = money_types.get(k, '%d dollar bills' % (k/100))
        money_type
        print "%s: %d" % (money_type.rjust(16), v)

main()



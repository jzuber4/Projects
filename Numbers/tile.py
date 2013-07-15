"""
Program to calculate the cost of tile for tiling a floor plan of width and height, using a cost entered by the user.
Hey, it was on the list!
Author: Jimmy Zuber
"""
import sys

def main():
    if(len(sys.argv) < 4):
        print "usage: python tile.py width length cost"
        return
    try:
        w, l, c = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
    except:
        print "Enter valid numbers for width, length, and cost"
        return

    print "Cost is:", w * l * c

main()


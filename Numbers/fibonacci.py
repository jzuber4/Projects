"""
Memoized fibonacci, even though this circumstance
doesn't really require a dedicated function.
Prints the first N numbers of the fibonacci sequence.
Woe be on the exponential algorithm.
"""
import sys

# decorators, gotta try to use these more
def memoize(func):
    saved = {}
    def inner_function(num):
        if not num in saved:
            saved[num] = func(num)
            return saved[num]
        else:
            return saved[num]
    return inner_function

@memoize
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def main():
    if len(sys.argv) != 2:
        print 'usage: python fibonacci.py fibonacci_index'
        return

    # again, memoized not really required, but that's ok
    for i in xrange(int(sys.argv[1])):
        print fibonacci(i),

main()



"""
Simple calculator.
Supports order of operations as specified by parentheses.
Implements:
    binary: + - / // * ** % << >> & ^ |
    unary: +, -, ~, not
    boolean: and or not
    comparisons: < <= == != > >=
A bit hard-coded to fit the specific circumstances, but I
would use yacc or something if I wanted powerful/actual control
over syntax. Tested against the python command line.
Author: Jimmy Zuber
"""
import re
import fileinput


def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def div(a, b):
    return a / b
def int_div(a, b):
    return a // b
def mul(a, b):
    return a * b
def pwr(a, b):
    return a ** b
def mod(a, b):
    return a % b
def lshift(a, b):
    return a << b
def rshift(a, b):
    return a >> b
def bitwise_and(a, b):
    return a & b
def bitwise_xor(a, b):
    return a ^ b
def bitwise_or(a, b):
    return a | b
def lt(a, b):
    return a < b
def gt(a, b):
    return a > b
def lte(a, b):
    return a <= b
def gte(a, b):
    return a >= b
def eq(a, b):
    return a == b
def neq(a, b):
    return a != b
def and_bool(a, b):
    return a and b
def or_bool(a, b):
    return a or b
def not_unary(a):
    return ~a
def not_unary_bool(a):
    return not a
def pos(a):
    return +a
def neg(a):
    return -a

# Strings that could be both (we will use "unary" + c for a c that qualifies for both)
ambiguous = {
        '+':True,
        '-':True,
        }
# operators with weird grouping rules
weird_grouping = {
        pwr:'right',
        lt:'chain', gt:'chain', lte:'chain', gte:'chain', eq:'chain', neq:'chain',
        }
# map strings to functions
unary_operators = {
        'unary+':(10, pos),
        'unary-':(10, neg),
        '~':(10, not_unary),
        'not':(3, not_unary_bool),
        }
binary_operators = {
        '**':(11, pwr),
        '/':(9, div), '*':(9, mul), '%':(9, mod), '//':(9, int_div),
        '+':(8, add), '-':(8, sub),
        '<<':(7, lshift), '>>':(7, rshift),
        '&':(6, bitwise_and),
        '^':(5, bitwise_xor),
        '|':(4, bitwise_or),
        '<':(3, lt), '>':(3, gt), '<=':(3, lte), '>=':(3, gte), '==':(3, eq), '!=':(3, neq),
        'and':(1, and_bool), 'or':(0, or_bool),
        }

# converts an expression to a number result
def resolve_expressions(nums, ops):

    # no empty expressions
    if len(nums) == 0:
        raise ValueError("Empty expression.")
    if len(nums) <= len(ops):
        if len(ops) == len(nums) == 1:
            return ops[0](nums[0])
        else:
            raise ValueError("Binary operators take two operands")
    if len(ops) == 0:
        return nums[0]

    # group from right with exponentiation
    if ops[0] == pwr:
        curr_num = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            curr_num = pwr(nums[i], curr_num)
        return curr_num
    # chain for comparisons a < b < c means a < b and b < c
    if ops[0] in weird_grouping:
        for i in range(len(nums) - 1):
            if not ops(nums[i], nums[i + 1]):
                return False
        return True

    # normal grouping left -> right
    curr_num = nums[0]
    for i in range(1, len(nums)):
        curr_op = ops[i - 1]
        curr_num = curr_op(curr_num, nums[i])
    return curr_num

# Hackish :)
def format_line(line):
    tkns = []
    i = 0
    while True:
        if i == len(line):
            break

        if len(line[i].strip()) == 0:
            i += len(line[i])
            continue

        # check for parens
        if line[i] == '(' or line[i] == ')':
            tkns.append(line[i])
            i += 1
            continue

        j = i + 1
        found_num = False
        found_op = False

        # longest number match
        try:
            while j <= len(line):
                num = float(line[i:j])
                found_num = True
                j += 1
        except:
            pass
        if found_num:
            j -= 1
            if '.' in line[i:j]:
                tkns.append(float(line[i:j]))
            else:
                tkns.append(int(line[i:j]))
            i = j
            continue

        # longest operator match
        while j <= len(line):
            test = line[i:j]
            if test in unary_operators or test in binary_operators:
                found_op = True
                found_max = j
            j += 1

        if not found_op:
            print "Syntax Error at '%s'" % line[i]
            return

        tkns.append(line[i:found_max])
        i = found_max

    return tkns



def parse_line(line):
    line = format_line(line)
    if line == None:
        return
    top_ops = []
    all_ops = [top_ops]
    top_nums = []
    all_nums = [top_nums]
    top_prec = -2 # reserved for bottom stack
    all_precs = [top_prec]
    last = ""

    for c in line:
        # number
        try:
            _ = float(c)
            num = c
            top_nums.append(num)
            if last and last == "num":
                print "Two numbers cannot be next to each other."
                return
            last = "num"
            continue

        # Get rid of indent
        except ValueError:
            pass

        # differentiate binary vs unary + and -
        if c in ambiguous:
            if not last or last == "op":
                c = "unary" + c

        # Verify operator or parenthesis
        if c == ")":
            if last == "op":
                print "Closing parentheses should not follow operator"
                return
            prec = -20 # way higher - must push

        elif c == "(":
            if last == "num":
                print "Opening parentheses should not follow operator."
                return
            prec = 20 # way lower - must pop

        elif c in unary_operators:
            if last == "num":
                print "Unary operator should not follow number or expression"
                return
            prec, func = unary_operators[c]

            if top_prec > prec:
                # not operator cannot be preceded by non boolean operator
                if func == not_unary_bool:
                    print "Syntax error at \"%s\"." % c
                    return
                # + - ~ unary operators bind tightly on left
                else:
                    prec = 12

        elif c in binary_operators:
            if last == "op":
                print "Binary operator should be between two numbers or expressions."
                return
            prec, func = binary_operators[c]

        else:
            print "Unexpected symbol \"%s\"." % c
            return

        # aggressively reduce first
        while prec < top_prec:
            try:
                val = resolve_expressions(all_nums.pop(), all_ops.pop())
                all_precs = all_precs[:-1]
            except ValueError as e:
                print e
                return

            # matched closing parens
            if c == ")":
                if top_prec == -1:
                    prec = all_precs[-1]
                elif top_prec == -2:
                    print "Unmatched parentheses )"
                    return
            top_nums = all_nums[-1]
            top_ops = all_ops[-1]
            top_prec = all_precs[-1]
            top_nums.append(val)

        # then add new context for precedence
        if prec > top_prec:
            last = ""
            if c in binary_operators: # + - ** * / etc.
                carry_up_num = top_nums.pop()
                all_nums.append([carry_up_num])
                all_ops.append([func])
                all_precs.append(prec)
            elif c in unary_operators: # not, ~, -, +
                all_nums.append([])
                all_ops.append([func])
                all_precs.append(prec)
            else: # parens
                all_nums.append([])
                all_ops.append([])
                all_precs.append(-1)
            top_ops = all_ops[-1]
            top_nums = all_nums[-1]
            top_prec = all_precs[-1]
            last = ""
        else:
            if c != "(" and c != ")":
                top_ops.append(func)
                last = "op"

    while len(all_nums) > 0:
        try:
            val = resolve_expressions(all_nums.pop(), all_ops.pop())
            if all_nums:
                all_nums[-1].append(val)
        except ValueError as e:
            print e
            return
    return val


def main():
    print "type q to quit"
    while True:
        line = raw_input("calculator.py: ")
        if line.strip() == "q":
            return
        val = parse_line(line)
        if val != None:
            print "calculator.py: =", val

main()


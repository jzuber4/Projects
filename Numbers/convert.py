"""
Converts units of temperature or currency. Adding volume, mass and distance did not present any (non busywork) additional challenge, and were omitted.
I also just realized argparse existed.
Supported temperature units: Kelvin, Celsius, Fahrenheit, Rankine, Delisle, Newton, Reaumur, Romer
Supported currencies (as of 21 August 2013): USD - US Dollar, EUR - Euro, GBP - British Pound, INR - Indian Rupee, AUD - Australian Dollar, CAD - Canadian Dollar, AED - Emirati Dirham, BTC - Bitcoin
Source for temperature conversions: http://en.wikipedia.org/wiki/Conversion_of_units_of_temperature
Source for currency conversions: 8/24/13: google (and bitcoincharts.com mtgoxUSD average for BTC)
Author: Jimmy Zuber
"""
import sys
import argparse

# I use a 'base unit' so that I only need the conversion table of one unit (instead of each ordered pairwise conversion table)
# unit:(name, (coefficient, offset)) | base unit = Kelvin
temperature = {'k':('Kelvin', (1, 0)), 'c':('Celsius', (1, -273.15)), 'f':('Fahrenheit', (1.8, -459.67)), 'r':('Rankine', (1.8, 0)), 'de':('Delisle', (-1.5, 559.725)), 'n':('Newton', (0.33, -90.1395)), 're':('Reaumur', (0.8, -218.52)), 'ro':('Romer', (0.525, -135.90375))}
# unit:(name, coefficient) | base unit = US Dollar
currency = {'USD':('US Dollar', 1), 'EUR':('Euro' ,0.75), 'GBP':('British Pound Sterling', 0.64), 'INR':('Indian Rupee', 63.22), 'AUD':('Australian Dollar', 1.11), 'CAD':('Canadian Dollar',1.05), 'AED':('United Arab Emirates Dirham', 3.67), 'BTC':('Bitcoin', 0.009259)}
def s(dictionary):
    s = ""
    for k,v in dictionary.iteritems():
        s += "\n" + str(k).ljust(2) + " - " + v[0]
    return s

def convert(general_type, from_type, to_type, value):
    pass

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description='Convert units of temperature or currency.')
    group = parser.add_subparsers(help='Choose (t)emperature or (c)urrency conversion')
    # choose temperature mode
    parser_t = group.add_parser('t', formatter_class=argparse.RawDescriptionHelpFormatter,
            description="Convert between units of temperature:" + s(temperature))
    # choose currency mode
    parser_c = group.add_parser('c', formatter_class=argparse.RawDescriptionHelpFormatter,
            description="Convert between units of currency" + s(currency))
    # arguments must be in dict
    parser_t.add_argument('from_unit', type=str, choices = temperature.keys(), help="unit converted from")
    parser_t.add_argument('to_unit', type=str, choices = temperature.keys(), help="unit converted to")
    parser_t.add_argument('value', type=float, help="value to be converted")
    parser_t.set_defaults(which=temperature)
    parser_c.add_argument('from_unit', type=str, choices = currency.keys(), help="unit converted from")
    parser_c.add_argument('to_unit', type=str, choices = currency.keys(), help="unit converted to")
    parser_c.add_argument('value', type=float, help="value to be converted")
    parser_c.set_defaults(which=currency)
    args = parser.parse_args(sys.argv[1:])
    v = args.value
    if args.which == temperature:
        # convert to kelvin
        v = (1.0 / temperature[args.from_unit][1][0]) * (v - temperature[args.from_unit][1][1])
        # convert from kelvin
        v = temperature[args.to_unit][1][0] * v + temperature[args.to_unit][1][1]
    else:
        # convert to USD
        v = (1.0 / currency[args.from_unit][1]) * v
        # convert from USD
        v = currency[args.to_unit][1] * v
    print v

main()


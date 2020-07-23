import argparse
parser = argparse.ArgumentParser()

parser.add_argument("city", type=int, help="Enter the city to get weather updates")

args = parser.parse_args()

if args.cube:
    print(args.number * args.number * args.number)
else:
    print(args.number * args.number)
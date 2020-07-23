import argparse
parser = argparse.ArgumentParser()


parser.add_argument("number", type=int, help="Enter number")

parser.add_argument("-c", "--cube")

args = parser.parse_args()

if args.cube:
    print(args.number * args.number * args.number)
else:
    print(args.number * args.number)
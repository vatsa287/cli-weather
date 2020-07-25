
import argparse
from get_by_city import get_by_city_args, city_parse

def main():
    parser = argparse.ArgumentParser('cli-weather')
    subparsers = parser.add_subparsers()
    get_by_city_args(subparsers)
    args = parser.parse_args()
    if args.city is not None:
        city_parse(args)

if __name__ == "__main__":
    main()

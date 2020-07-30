from __future__ import print_function
import argparse

# handle ModuleNotFoundError python3 execution
try:
    from cli_weather.get_by_city import get_by_city_args, city_parse
    from cli_weather.get_by_postalcode import get_by_postalcode_args, postalcode_parse
except ModuleNotFoundError:
    from get_by_city import get_by_city_args, city_parse
    from get_by_postalcode import get_by_postalcode_args, postalcode_parse

def main():
    parser = argparse.ArgumentParser('cli-weather')

    # dest - name of the attribute under which sub-command name will be stored, defalut=None
    subparsers = parser.add_subparsers(dest="city_or_postalcode")
    subparsers.required = True
    get_by_city_args(subparsers)
    get_by_postalcode_args(subparsers)
    args = parser.parse_args()

    # args.selected_subparser holds selectd subparser in <str>
    if args.city_or_postalcode == "city":
        city_parse(args)
    elif args.city_or_postalcode == "postalcode":
        postalcode_parse(args)

if __name__ == "__main__":
    main()

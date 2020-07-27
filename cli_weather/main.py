import argparse
from get_by_city import get_by_city_args, city_parse 
from get_by_postalcode import get_by_postalcode_args, postalcode_parse

def main():
    parser = argparse.ArgumentParser('cli-weather')
    # dest - name of the attribute under which sub-command name will be stored, defalut=None
    subparsers = parser.add_subparsers(dest="selected_subparser")
    get_by_city_args(subparsers)
    get_by_postalcode_args(subparsers)
    args = parser.parse_args()
    # args.selected_subparser holds selectd subparser in <str>
    if args.selected_subparser == "city":
        city_parse(args)
    elif args.selected_subparser == "postalcode":
        postalcode_parse(args)

if __name__ == "__main__":
    main()
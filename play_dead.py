#! /usr/bin/env python
import argparse
from internetarchive import *

default_query_string = "collection:(GratefulDead) AND Subject:(Soundboard)"


def play_dead():
    parser = argparse.ArgumentParser(description="play-dead argument parser")
    parser.add_argument("-y", "--year", 
                        help="select from shows in the specified year")
    parser.add_argument("-d", "--date", help="play the specified date")
    parser.add_argument("-r", "--range", nargs=2, 
                        metavar=("LOW_YEAR", "HIGH_YEAR"),
                        help="select from shows between the provided years")
    args = parser.parse_args()

    # if all arguments are None
    if all(getattr(args, arg) is None for arg in vars(args)):
        print("play random show selected from entire career")
    
    if ((args.year is not None and args.date is not None) or
       (args.year is not None and args.range is not None) or
       (args.date is not None and args.range is not None)
       ):
        print("please supply only one out of: --year, --date, --range")
        exit()
    if args.year is not None:
        try:
            if 1965 <= int(args.year) <= 1995:
                print("play random show from " + args.year)
        except ValueError:
            print("invalid year: " + args.year)
    if args.date is not None:
        print("play " + args.date)
    if args.range is not None:
        print("play show between", args.range[0], args.range[1])


if __name__ == '__main__':
    play_dead()


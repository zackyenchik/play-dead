#! /usr/bin/env python
import argparse
import re
import sys
from internetarchive import *

DEFAULT_QUERY_STRING = "collection:(GratefulDead) AND Subject:(Soundboard)"
QUERY_AND = " AND "
QUERY_DATE = "date:{year}-{month}-{day}"
QUERY_RANGE = "date:[{lo_year}-{lo_month}-{lo_day} TO {hi_year}-{hi_month}-{hi_day}]"


def build_query_string(args):
    query_string = DEFAULT_QUERY_STRING
    # if all arguments are None
    if all(getattr(args, arg) is None for arg in vars(args)):
        query_string += QUERY_AND + QUERY_RANGE.format(lo_year= "1965",
                                                       lo_month= "01",
                                                       lo_day= "01",
                                                       hi_year= "1995",
                                                       hi_month= "12",
                                                       hi_day= "31")
    if args.date is not None:
        if re.match(r"[\d]{4}-[\d]{2}-[\d]{2}", args.date):
            date_pieces = args.date.split("-")
            date_year = date_pieces[0]
            date_month = date_pieces[1]
            date_day = date_pieces[2]
            query_string += QUERY_AND + QUERY_DATE.format(year= date_year,
                                                          month= date_month,
                                                          day= date_day)
        else:
            sys.exit("date does not match format: YYYY-MM-DD")
    if args.range is not None:
        if re.match(r"[\d]{4}", args.range[0]) != None and \
           re.match(r"[\d]{4}", args.range[1])!= None \
           :
               query_string += QUERY_AND + QUERY_RANGE.format(lo_year= args.range[0],
                                                              lo_month= "01",
                                                              lo_day= "01",
                                                              hi_year= args.range[1],
                                                              hi_month= "12",
                                                              hi_day= "31")
        else:
            sys.exit("range does not match format: YYYY-YYYY")
    if args.year is not None:
        if re.match(r"[\d]{4}", args.year):
            query_string += QUERY_AND + QUERY_RANGE.format(lo_year= args.year,
                                                           lo_month= "01",
                                                           lo_day= "01",
                                                           hi_year= args.year,
                                                           hi_month= "12",
                                                           hi_day= "31")
        else:
            sys.exit("year does not match format: YYYY")
    return query_string


def play_dead():
    parser = argparse.ArgumentParser(description="play-dead argument parser")
    parser.add_argument("-y", "--year", 
            help="select from shows in the specified year: YYYY")
    parser.add_argument("-d", "--date", help="play the specified date: YYYY-MM-DD")
    parser.add_argument("-r", "--range", nargs=2, 
                        metavar=("LOW_YEAR", "HIGH_YEAR"),
                        help="select from shows between the provided years")
    args = parser.parse_args()

    # make sure user provides only one date related argument
    if (args.year is not None and args.date is not None) or \
       (args.year is not None and args.range is not None) or \
       (args.date is not None and args.range is not None) \
       :
        sys.exit("please supply only one out of: --year, --date, --range")

    query_string = build_query_string(args)
    print(query_string)


if __name__ == '__main__':
    play_dead()


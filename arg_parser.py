import argparse
from datetime import datetime


def valid_date(s):
    try:
        return datetime.strptime(s, '%Y-%m-%d')
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)
        
        
def argument_parser():
    p = argparse.ArgumentParser(
        description="converts a fixed width windows-1252 encoded file to delimited utf-8 file"
    )
    p.add_argument(
        "-s",
        "--specs",
        required=False,
        type=str,
        help="spec.json file path",
        default="./data/spec.json"
    )
   
    p.add_argument(
        "-o",
        "--delimited_output_file",
        required=False,
        type=str,
        help="fixed width input file path",
        default="./output/delimited_output.csv"
    )
    
    p.add_argument(
        '-e',
        '--end_date',
        required=False,
        # validates the date string input
        type=valid_date,
        help='end time of format yyyy-mm-dd, default to today',
        default=datetime.now()
    )
    p.add_argument(
        '-s',
        '--start_date',
        required=False,
        type=valid_date,
        help='start time of format yyyy-mm-dd, default to yesterday',
        default=datetime.now() - timedelta(1)
    )
    args = p.parse_args()

    if args.end_date <= args.start_date:
        raise ValueError('{0} should be greater than {1}'.format(args.end_date, args.start_date))
        
    return args.specs,  args.delimited_output_file, args.start_date, args.end_date

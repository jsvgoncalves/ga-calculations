import argparse
from datetime import datetime as dt
from datetime import timedelta
import csv

def valid_date(s):
    try:
        return dt.strptime(s, "%d.%m.%Y")
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)

def calculate(to_date):
    year_ago = to_date - timedelta(days=365)
    print('Counting from {} to {}'.format(
        dt.strftime(year_ago, '%d.%m.%Y'),
        dt.strftime(dt.now(), '%d.%m.%Y')))
    total = 0
    with open('2018.csv') as f:
        d = csv.reader(f)
        d_count = sum(1 for r in d if dt.strptime(r[0], '%d.%m.%Y') >= year_ago)
        total += d_count
        print('2018: {} days'.format(d_count))

    with open('2019.csv') as f:
        d = csv.reader(f)
        d_count = sum(1 for r in d if dt.strptime(r[0], '%d.%m.%Y') <= dt.now())
        total += d_count
        print('2019: {} days'.format(d_count))

    print('Total: {} travel days'.format(total))

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Count total travelling days.')
    parser.add_argument('--to', 
                       help='end date for the calculation (DD.MM.YYYY)',
                       type=valid_date,
                       default=dt.now())
    args = parser.parse_args()
    calculate(args.to)


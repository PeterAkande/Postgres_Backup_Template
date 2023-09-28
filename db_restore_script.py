import argparse

parser = argparse.ArgumentParser(description="Restore POSTGRES Database",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('-c', '--compressed', action='store_true',
                    help='Indicate that File is compressed. Only gzip supported')
parser.add_argument('-d', '--database', help='Database Name', required=True)
parser.add_argument('-U', '--user', help='Postgres User name. Defaults to current logged in user')
parser.add_argument('src', help='Database File location. ABSOLUTE LOCATION NOT RELATIVE')

args = parser.parse_args()
config = vars(args)


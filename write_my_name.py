import argparse

parser = argparse.ArgumentParser(description='Najgorsza rzecz to --thing')
parser.add_argument('--thing', type=str, help='Najgorsza rzecz to')

args = parser.parse_args()

with open('my_name.txt', 'w') as my_file:
    my_file.write(args.thing)
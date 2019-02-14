import argparse

parser = argparse.ArgumentParser(description='Witam Pana --name')
parser.add_argument('--name', type=str, help='Twoje imie prosze Pana')
parser.add_argument('--powitanie', type=str, help='Twoje imie prosze Pana')

args = parser.parse_args()

print('Witaj ' + args.name)
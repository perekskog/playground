import csv
import sys
import json


def fetch_items(file):
    items = list()
    session = str()
    with open(file, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            if(len(row)==1):
                session = row[0]
            else:
                item = {'session': session, 'task':row[0], 'time': row[1]}
                items.append(item)
    return items


def print_items(items):
    print(items)


def main(file):
    items = fetch_items(file)
#    print_items(items)
    jsonitems = json.dumps(items, sort_keys=True, indent=4)
    print_items(jsonitems)

if __name__ == '__main__':
    main(sys.argv[1])

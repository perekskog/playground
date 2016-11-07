import csv
import sys
import json


def fetch_items(file):
    items = list()
    session = str()
    task = str()
    starttime = str()
    stoptime = str()
    with open(file, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            if(len(row)==1):
                # Start of session
                session = row[0]
            else:
                # Not start of session
                if row[0] == "":
                    # Stop and add ongoing task, don't start new
                    stoptime = row[1]
                    item = {'session': session, 'task':task, 'start': starttime, 'stop': stoptime}
                    items.append(item)
                    task = ""
                else:
                    if task == "":
                        # No ongoing task, start a new task
                        task = row[0]
                        starttime = row[1]
                    else:
                        # Stop and add ongoing task, start new task
                        stoptime = row[1]
                        item = {'session': session, 'task':task, 'start': starttime, 'stop': stoptime}
                        items.append(item)
                        task = row[0]
                        starttime = row[1]
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

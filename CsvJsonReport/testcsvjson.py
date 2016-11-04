import csv
import sys
import json


def fetch_items(file):
    items = list()
    with open(file, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        headline = reader.__next__()
        for row in reader:
            item = {'date':row[0], 'activity': row[1], 'starttime': row[2]}
            items.append(item)
    return items


def print_items(items):
    print(items)


def main(file):
    items = fetch_items(file)
    print_items(items)
    jsonitems = json.dumps(items, sort_keys=True, indent=4)
    print_items(jsonitems)

if __name__ == '__main__':
    main(sys.argv[1])


#jsonData='{"name": "Frank", "age":39, "list":[{"1":"a"},{"2":"b"}]}'
#jsonToPython=json.loads(jsonData)
#print(jsonToPython)
#{'age': 39, 'name': 'Frank', 'list': [{'1': 'a'}, {'2': 'b'}]}
#dictionaryToJson=json.dumps(jsonToPython)
#print(dictionaryToJson)
#{"age": 39, "name": "Frank", "list": [{"1": "a"}, {"2": "b"}]}

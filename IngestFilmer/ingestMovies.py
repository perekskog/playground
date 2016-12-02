import sys
import json


def fetch_items(filein):
    movies = list()
    with open(filein, 'r', encoding='utf-8') as f:
        for row in f:
            print(row)
    return movies


def main(filein, fileout):
    items = fetch_items(filein)
    open(fileout, 'wb').write(json.dumps(items, sort_keys=True, indent=4, ensure_ascii=False).encode('utf8'))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
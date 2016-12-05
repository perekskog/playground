import sys
import json


def fetch_items(filein):
    movies = list()
    with open(filein, 'r', encoding='utf-8') as f:
        for row in f:
            # file = [ comment | movie ]*
            # comment = # string
            # movie = disk SPACE title_with_attributes
            # title_with_attributes =  title SPACE *format | COMMA § category | COMMA # language | COMMA & mirrored_on_mediaserver
            # title = string [string SPACE]*
            # language = audio SLASH subtitle
            # mirrored_on_mediaserver = & ms

            # comment
            if row[0] == "#":
                print("continue 1")
                continue
            print(row)

            # movie
    return movies


def main(filein, fileout):
    items = fetch_items(filein)
    open(fileout, 'wb').write(json.dumps(items, sort_keys=True, indent=4, ensure_ascii=False).encode('utf8'))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
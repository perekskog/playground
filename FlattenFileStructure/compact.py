"""Make a list of pathnames

Usage:
    python3 compact.py db list

db is a list of pathnames, for example, created by
>find top-of-filetree > db

list is a list of filenames, for example, created by
>ls > list

compact will match names in "list" with the basemane of
paths in "db".
"""

import sys
import os


def read_db(dbname):
    with open(dbname, mode="rt", encoding="utf-8") as f:
        return {os.path.basename(line.strip()).lower(): line.strip() for line in f}


def get_files(filelist):
    with open(filelist, mode="rt", encoding="utf-8") as f:
        return [line.strip() for line in f]

def map_files(db, basenames):
    return [ db[file.lower()] for file in basenames ]


def main(dbname, filelist):
    db = read_db(dbname)
    files = get_files(filelist)
    filepaths = map_files(db, files)
    for file in filepaths:
        print(file)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

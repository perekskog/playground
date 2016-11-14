import sys
import json
from datetime import datetime
from TpCsv2Json import fetch_items

sheets = [
    {
    'name': "21 dec - 27 dec-Tabell 1.csv",
    'basedate': "15-12-21",
    'columns': [0, 2, 4, 6, 8, 10, 12]
    }#,
    # {
    # 'name': "30 dec - 4 jan - Tabell1.csv",
    # 'basedate': "15-12-30",
    # 'columns': [0, 2, 4, 6, 8, 10]
    # },
    # {
    # 'name': "5 jan - 10 jan - Tabell1.csv",
    # 'basedate': "16-01-05",
    # 'columns': [0, 2, 4, 6, 8, 10]
    # }
]

def date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    elif isinstance(obj, ...):
        return ...
    else:
        raise TypeError('Object of type %s with value of %s is not JSON serializable' % (type(obj), repr(obj)))

def main(basedirectory, json_store):
    f = open(json_store, 'wb')
    for sheet in sheets:
        for column in sheet['columns']:
            items = fetch_items(basedirectory+sheet['name'], "utf-8", ';', datetime.strptime(sheet['basedate'], "%y-%m-%d"), column)
            f.write(json.dumps(items, sort_keys=True, indent=4, default=date_handler, ensure_ascii=False).encode('utf8'))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

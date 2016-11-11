import sys
import json
from datetime import datetime, date, time


def datetime_parser(json_dict):
    for (key, value) in json_dict.items():
        try:
            json_dict[key] = dateutil.parser.parse(value)
        except (ValueError, AttributeError):
            pass
    return json_dict


def date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    elif isinstance(obj, ...):
        return ...
    else:
        raise TypeError('Object of type %s with value of %s is not JSON serializable' % (type(obj), repr(obj)))


def main(store):
#    items = fetch_items(file)
    items = json.loads
    print_items(items)


if __name__ == '__main__':
    main(sys.argv[1])

import sys
import json
from datetime import datetime, date, time


def datetime_parser(json_dict):
    for (key, value) in json_dict.items():
        try:
            json_dict[key] = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')
        except (ValueError, AttributeError, TypeError):
            pass
    return json_dict


def date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    elif isinstance(obj, ...):
        return ...
    else:
        raise TypeError('Object of type %s with value of %s is not JSON serializable' % (type(obj), repr(obj)))


def main(store, first_date, last_date):
#    items = fetch_items(file)
    items = json.load(open(store, 'r', encoding="utf-8"), object_hook=datetime_parser)

    # Filter
    kostnad = [ s for s in items if s['projectname']=="Kostnad"]
    first = datetime.strptime(first_date, "%y-%m-%d").date().toordinal()
    last = datetime.strptime(last_date, "%y-%m-%d").date().toordinal()
    subset_kostnad = [ s for s in kostnad if s['date_created'].date().toordinal() >= first and
                                        s['date_created'].date().toordinal() <= last ]

    # Map
    # ...

    for session in subset_kostnad:
        print(session['projectname'], session['date_created'])

datetime.strptime("16-11-10", "%y-%m-%d")


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])

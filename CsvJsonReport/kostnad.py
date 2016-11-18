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


def session_between_dates(session, projectname, startdate, enddate):
    if session['projectname']==projectname and session['date_created'].date().toordinal() >= startdate and session['date_created'].date().toordinal() <= enddate:
        return True
    else:
        return False


def main(store, first_date, last_date):
#    items = fetch_items(file)
    items = json.load(open(store, 'r', encoding="utf-8"), object_hook=datetime_parser)
    # Filter: Select subset of sessions
    # Merge filters, use a function for filtering
    first = datetime.strptime(first_date, "%y-%m-%d").date().toordinal()
    last = datetime.strptime(last_date, "%y-%m-%d").date().toordinal()
    subset_kostnad = [ s for s in items if session_between_dates(s, "Kostnad", first, last)]

    # For each session:
    # Map to [date, taskname, totaltime]
    for session in subset_kostnad:
        task_summary = { (t['taskname'], timedelta(0)) for t in session['taskentries'] }
        for taskentry in session['taskentries']:
            name = taskentry['taskname']
            totaltime = taskentry['stop']-taskentry['start']
            task_summary[taskname] += totaltime
        print(task_summary)

    # Print result
    print("subset_kostnad")
    for session in subset_kostnad:
        print(session['projectname'], session['date_created'])



if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])

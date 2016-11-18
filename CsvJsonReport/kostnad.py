import sys
import json
import functools
from datetime import datetime, date, time, timedelta


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


#        s = { x for x in task_summary.keys()}
#        tasknames.update(s)

def add_task(summary, name, time):
    try:
        summary[name] += time
    except KeyError:
        summary[name] = time


def session_summary(session):
#    task_summary = { t['taskname']: timedelta(0) for t in session['taskentries'] }
    summary = dict()
    for taskentry in session['taskentries']:
        name = taskentry['taskname']
        totaltime = taskentry['stop']-taskentry['start']
        if name=="STOD dok (???)":
            add_task(summary, "STOD Vz", totaltime*2/3)
            add_task(summary, "CMCC", totaltime/3)
        else:
            add_task(summary, name, totaltime)
    return summary


def timesheet(store, first_date, last_date):
    first = datetime.strptime(first_date, "%y-%m-%d").date().toordinal()
    last = datetime.strptime(last_date, "%y-%m-%d").date().toordinal()
    subset_kostnad = [ s for s in store if session_between_dates(s, "Kostnad", first, last)]

    tasknames = set()
    for session in subset_kostnad:
        summary = session_summary(session)
        print(session['date_created'].date())
        for task in summary:
            print(task, round(summary[task].seconds/3600, 2))
        totals = [s for s in summary.values() ]
        total = functools.reduce(lambda x,y: x+y, totals)
        print(round(total.seconds/3600, 2))
        print()


def main(store, report, first_date, last_date):
    items = json.load(open(store, 'r', encoding="utf-8"), object_hook=datetime_parser)
    if report=="timesheet":
        timesheet(items, first_date, last_date)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

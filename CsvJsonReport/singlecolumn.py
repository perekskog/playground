import csv
import sys
import json
from datetime import datetime, date, time


def get_date(initial_year, initial_month, initial_day, a_day):
    year = initial_year
    month = initial_month
    day = initial_day
    if a_day < initial_day:
        month = initial_month+1
    if month > 12:
        month = month-12
        year = year+1

    return date(year,month,day)


def session_time(session_started, session_day_offset, timestamp):
    d = session_started.date().toordinal()
    t = datetime.strptime(timestamp, "%H:%M:%S").time()
    st = datetime.combine(date.fromordinal(d+session_day_offset), t)
    return st


def fetch_items(file, skipcolumns):
    sessions = list()
    taskentries = list()
    sessionname = str()
    sessioncreated = str()
    sessionisongoing = False
    taskname = str()
    starttime = str()
    stoptime = str()
    with open(file, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            print(row)
            if(len(row)<=skipcolumns):
                print("continue 1")
                continue;
            if(len(row)>=skipcolumns+1 and row[0+skipcolumns]=="" and row[1+skipcolumns]==""):
                print("continue 2")
                continue;
            if(len(row)==1+skipcolumns or (len(row)>=2+skipcolumns and row[1+skipcolumns] == "")):
                if sessionname == "":
                    # Start of new sesseion
                    d = get_date(2016,10,7, int(row[0+skipcolumns].split()[-1]))
                    sessioncreated = datetime.combine(d, time(0,0))
                    if row[0+skipcolumns].startswith("*"):
                        print("case s1")
                        sessionisongoing = True
                        sessionname = row[0+skipcolumns].split()[1]
                    else:
                        print("case s2")
                        sessionisongoing = False
                        sessionname = row[0+skipcolumns].split()[0]
                else:
                    # Switch session
                    session = {'sessionname': sessionname, 'isongoing': sessionisongoing, 'created': sessioncreated, 'taskentries': taskentries}
                    sessions.append(session)
                    taskentries = list()
                    d = get_date(2016,10,7, int(row[0+skipcolumns].split()[-1]))
                    sessioncreated = datetime.combine(d, time(0,0))
                    if row[0+skipcolumns].startswith("*"):
                        print("case s3")
                        sessionisongoing = True
                        sessionname = row[0+skipcolumns].split()[1]
                    else:
                        print("case s4")
                        sessionisongoing = False
                        sessionname = row[0+skipcolumns].split()[0]
            else:
                # Not start of session
                print(len(row))
                if row[0+skipcolumns] == "":
                    # Stop and add ongoing task, don't start new
                    print("case t1")
                    stoptime = session_time(sessioncreated, 0, row[1+skipcolumns])
                    taskentry = {'taskname':taskname, 'start': starttime, 'stop': stoptime}
                    taskentries.append(taskentry)
                    taskname = ""
                else:
                    if taskname == "":
                        # No ongoing task, start a new task
                        print("case t2")
                        taskname = row[0+skipcolumns]
                        starttime = session_time(sessioncreated, 0, row[1+skipcolumns])
                    else:
                        # Stop and add ongoing task, start new task
                        print("case t3")
                        stoptime = session_time(sessioncreated, 0, row[1+skipcolumns])
                        taskentry = {'taskname':taskname, 'start': starttime, 'stop': stoptime}
                        taskentries.append(taskentry)
                        taskname = row[0+skipcolumns]
                        starttime = session_time(sessioncreated, 0, row[1+skipcolumns])
    if len(taskentries) > 0:
        session = {'sessionname': sessionname, 'isongoing': sessionisongoing, 'created': sessioncreated, 'taskentries': taskentries}
        sessions.append(session)

    return sessions


def print_items(items):
    print(items)


def date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    elif isinstance(obj, ...):
        return ...
    else:
        raise TypeError('Object of type %s with value of %s is not JSON serializable' % (type(obj), repr(obj)))


def main(file, skipcolumns):
    items = fetch_items(file, int(skipcolumns))
#    print_items(items)
    jsonitems = json.dumps(items, sort_keys=True, indent=4, default=date_handler)
    print_items(jsonitems)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

import csv
import sys
import json
from datetime import datetime, date, time


def get_date(base_date, a_day):
    year = base_date.year
    month = base_date.month
    day = base_date.day
    if a_day < day:
        month = month+1
    day = a_day
    if month > 12:
        month = month-12
        year = year+1

    return date(year,month,day)


def session_time(session_started, session_day_offset, timestamp):
    d = session_started.date().toordinal()
    t = datetime.strptime(timestamp, "%H:%M:%S").time()
    st = datetime.combine(date.fromordinal(d+session_day_offset), t)
    return st


def fetch_items(file, input_encoding, input_delimiter, base_date, skipcolumns):
    sessions = list()
    taskentries = list()
    sessionname = str()
    sessioncreated = str()
    sessionisongoing = False
    session_day_offset = 0
    taskname = str()
    starttime = datetime(1,1,1)
    stoptime = datetime(1,1,1)
    #with open(file, 'r', encoding='iso-8859-1') as f:
    with open(file, 'r', encoding=input_encoding) as f:
        #reader = csv.reader(f, delimiter='\t')
        reader = csv.reader(f, delimiter=input_delimiter[0])
        for row in reader:
            print(row)
            if(len(row)<=skipcolumns):
                # Not enough columns
                print("continue 1")
                continue;
            if(len(row)>=skipcolumns+1 and row[0+skipcolumns]=="" and row[1+skipcolumns]==""):
                # Empty row
                print("continue 2")
                continue;
            if(len(row)>=skipcolumns+2 and row[skipcolumns+1]=="..."):
                # Unfinished task, skip row, next row will be empty or start of new session
                print("continue 3")
                taskname = ""
                continue;
            if(len(row)==1+skipcolumns or (len(row)>=2+skipcolumns and row[1+skipcolumns] == "")):
                if sessionname == "":
                    # Start of new sesseion, no previous session
                    d = get_date(base_date, int(row[0+skipcolumns].split()[-1]))
                    sessioncreated = datetime.combine(d, time(0,0))
                    if row[0+skipcolumns].startswith("*"):
                        print("case s1")
                        sessionisongoing = True
                        sessionname = " ".join(row[0+skipcolumns].split()[1:-1])
                    else:
                        print("case s2")
                        sessionisongoing = False
                        sessionname = " ".join(row[0+skipcolumns].split()[0:-1])
                else:
                    # Switch session
                    now = datetime.now()
                    session = {
                        'projectname': sessionname,
                        'isongoing': sessionisongoing,
                        'date_created': sessioncreated,
                        'date_ingested': now,
                        'date_modified': now,
                        'taskentries': taskentries}
                    sessions.append(session)
                    session_day_offset = 0
                    taskentries = list()
                    starttime = datetime(1,1,1)
                    stoptime = datetime(1,1,1)

                    d = get_date(base_date, int(row[0+skipcolumns].split()[-1]))
                    sessioncreated = datetime.combine(d, time(0,0))
                    if row[0+skipcolumns].startswith("*"):
                        print("case s3")
                        sessionisongoing = True
                        sessionname = " ".join(row[0+skipcolumns].split()[1:-1])
                    else:
                        print("case s4")
                        sessionisongoing = False
                        sessionname = " ".join(row[0+skipcolumns].split()[0:-1])
            else:
                # Not start of session
                print(len(row))
                if row[0+skipcolumns] == "":
                    # Stop and add ongoing task, don't start new
                    print("case t1")
                    stoptime = session_time(sessioncreated, session_day_offset, row[1+skipcolumns])
                    if stoptime < starttime:
                        print("case t1 - new day")
                        session_day_offset = session_day_offset+1
                        stoptime = session_time(sessioncreated, session_day_offset, row[1+skipcolumns])
                    print(starttime, stoptime)
                    taskentry = {'taskname':taskname, 'start': starttime, 'stop': stoptime}
                    taskentries.append(taskentry)
                    taskname = ""
                else:
                    if taskname == "":
                        # No ongoing task, start a new task
                        print("case t2")
                        taskname = row[0+skipcolumns]
                        starttime = session_time(sessioncreated, session_day_offset, row[1+skipcolumns])
                        if starttime < stoptime:
                            # Compensate for start of new day
                            print("case t2 - new day")
                            session_day_offset = session_day_offset+1
                            starttime = session_time(sessioncreated, session_day_offset, row[1+skipcolumns])
                        print(starttime, stoptime)
                    else:
                        # Stop and add ongoing task, start new task
                        print("case t3")
                        stoptime = session_time(sessioncreated, session_day_offset, row[1+skipcolumns])
                        if stoptime < starttime:
                            # Compensate for start of new day
                            print("case t3 - new day")
                            session_day_offset = session_day_offset+1
                            stoptime = session_time(sessioncreated, session_day_offset, row[1+skipcolumns])
                        print(starttime, stoptime)
                        taskentry = {'taskname':taskname, 'start': starttime, 'stop': stoptime}
                        taskentries.append(taskentry)
                        taskname = row[0+skipcolumns]
                        starttime = stoptime
    if len(taskentries) > 0:
        now = datetime.now()
        session = {
            'projectname': sessionname,
            'isongoing': sessionisongoing,
            'date_created': sessioncreated,
            'date_ingested': now,
            'date_modified': now,
            'taskentries': taskentries}
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


def main(filein, input_encoding, input_delimiter, base_date, skipcolumns, fileout):
    if input_delimiter=="tab":
        items = fetch_items(filein, input_encoding, '\t', datetime.strptime(base_date, "%y-%m-%d"), int(skipcolumns))
    else:
        items = fetch_items(filein, input_encoding, input_delimiter, datetime.strptime(base_date, "%y-%m-%d"), int(skipcolumns))

    open(fileout, 'wb').write(json.dumps(items, sort_keys=True, indent=4, default=date_handler, ensure_ascii=False).encode('utf8'))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])

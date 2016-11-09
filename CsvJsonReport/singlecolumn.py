import csv
import sys
import json


def fetch_items(file):
    sessions = list()
    taskentries = list()
    sessionname = str()
    sessionisongoing = False
    taskname = str()
    starttime = str()
    stoptime = str()
    with open(file, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            if(len(row)==1):
                if sessionname == "":
                    # Start of new sesseion
                    sessionname = row[0]
                    if sessionname.startswith("* "):
                        sessionisongoing = True
                        sessionname = sessionname.lstrip("* ")
                    else:
                        sessionisongoing = False
                else:
                    # Switch session
                    session = {'sessionname': sessionname, 'isongoing': sessionisongoing, 'taskentries': taskentries}
                    sessions.append(session)
                    taskentries = list()
                    sessionname = row[0]
                    if sessionname.startswith("* "):
                        sessionisongoing = True
                        sessionname = sessionname.lstrip("* ")
                    else:
                        sessionisongoing = False
            else:
                # Not start of session
                if row[0] == "":
                    # Stop and add ongoing task, don't start new
                    stoptime = row[1]
                    taskentry = {'taskname':taskname, 'start': starttime, 'stop': stoptime}
                    taskentries.append(taskentry)
                    taskname = ""
                else:
                    if taskname == "":
                        # No ongoing task, start a new task
                        taskname = row[0]
                        starttime = row[1]
                    else:
                        # Stop and add ongoing task, start new task
                        stoptime = row[1]
                        taskentry = {'taskname':taskname, 'start': starttime, 'stop': stoptime}
                        taskentries.append(taskentry)
                        taskname = row[0]
                        starttime = row[1]
    if len(taskentries) > 0:
        session = {'sessionname': sessionname, 'isongoing': sessionisongoing, 'taskentries': taskentries}
        sessions.append(session)

    return sessions


def print_items(items):
    print(items)


def main(file):
    items = fetch_items(file)
#    print_items(items)
    jsonitems = json.dumps(items, sort_keys=True, indent=4)
    print_items(jsonitems)


if __name__ == '__main__':
    main(sys.argv[1])

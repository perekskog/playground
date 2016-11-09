import csv
import sys
import json


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
                    sessioncreated = row[0+skipcolumns].split()[-1]
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
                    sessioncreated = row[0+skipcolumns].split()[-1]
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
                    stoptime = row[1+skipcolumns]
                    taskentry = {'taskname':taskname, 'start': starttime, 'stop': stoptime}
                    taskentries.append(taskentry)
                    taskname = ""
                else:
                    if taskname == "":
                        # No ongoing task, start a new task
                        print("case t2")
                        taskname = row[0+skipcolumns]
                        starttime = row[1+skipcolumns]
                    else:
                        # Stop and add ongoing task, start new task
                        print("case t3")
                        stoptime = row[1+skipcolumns]
                        taskentry = {'taskname':taskname, 'start': starttime, 'stop': stoptime}
                        taskentries.append(taskentry)
                        taskname = row[0+skipcolumns]
                        starttime = row[1+skipcolumns]
    if len(taskentries) > 0:
        session = {'sessionname': sessionname, 'isongoing': sessionisongoing, 'created': sessioncreated, 'taskentries': taskentries}
        sessions.append(session)

    return sessions


def print_items(items):
    print(items)


def main(file, skipcolumns):
    items = fetch_items(file, int(skipcolumns))
#    print_items(items)
    jsonitems = json.dumps(items, sort_keys=True, indent=4)
    print_items(jsonitems)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

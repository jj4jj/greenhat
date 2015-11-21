# Copyright (c) 2015 Angus H. (4148)
# Distributed under the GNU General Public License v3.0 (GPLv3).

from datetime import date, timedelta
from random import randint
from time import sleep
import sys
import subprocess
import os

# returns a date string for the date that is N days before STARTDATE
def get_date_string(n, startdate):
	d = startdate - timedelta(days=n)
	rtn = d.strftime("%a %b %d %X %Y %z -0400")
	return rtn

# main app
def main(argv):
    if len(argv) < 1 or len(argv) > 4:
        print "Error: Bad input."
        print "usage :python " + __file__ + " <max days commit> [<end date> (eg:2015/01/01) [<max random skip days> [<max random commit one day>] ] ]"
        sys.exit(1)
    n = int(argv[0])
    if len(argv) >= 2:
        startdate = date(int(argv[1][0:4]), int(argv[1][5:7]), int(argv[1][8:10]))
    else:
        startdate = date.today()

    if len(argv) >= 3:
        max_skip_days = int(argv[2])
    else:
        max_skip_days = 1  # default value

    if len(argv) == 4:
        max_commit_a_day = int(argv[3])
    else:
        max_commit_a_day = 5  # default value	i = 0
    i = 0
    while i <= n:
        curdate = get_date_string(i, startdate)
        num_commits = randint(1, max_commit_a_day)
        for commit in range(0, num_commits):
            subprocess.call("echo '" + curdate + str(randint(0, 1000000)) +"' > realwork.txt; git add realwork.txt; GIT_AUTHOR_DATE='" + curdate + "' GIT_COMMITTER_DATE='" + curdate + "' git commit -m 'update'; git push;", shell=True)
            sleep(.5)
        i += randint(1, max_skip_days)
    subprocess.call("git rm realwork.txt; git commit -m 'delete'; git push;", shell=True)

if __name__ == "__main__":
    main(sys.argv[1:])

#!/usr/bin/python

### FOR BORROWER RECORDS ###
# New and Improved for Columns that match up.

import re
from datetime import datetime
from datetime import timedelta

now = datetime.now()
year = now.year
month = now.month
day = now.day
date = "%i/%i/%i" % (month, day, year)
lend_period = timedelta(days=30)
due = now + lend_period
due = due.strftime("%m/%d/%Y")


textfile = open(r'/tmp/accessRecord.txt', 'r')
filetext = textfile.read()
textfile.close()
splitext = list(filetext.splitlines())

for i in splitext:
	if re.search(r'(Author)', i) is not None:
		author = i[16:]
		author = author.strip()
	elif re.search(r'(Journal Title)', i) is not None:
		title = i[23:]
		title = title.strip()
	elif re.search(r'( Lender  )', i) is not None:
		lender = i[8:]
		lender = lender.strip()
	elif re.search(r'( Borrower  )', i) is not None:
		borrower = i[10:]
		borrower = borrower.strip()
	elif re.search(r'(Request Number)',i) is not None:
		ill_num = ill_num = re.search(r'(\d{6,})', i)
		ill_num = ill_num.group()

#print '\n' #for CLI prettiness
try:
	print date + '\t' + author + '\t' + title + '\t' + lender + '\t' + borrower + '\t' + due + '\t' + '' + '\t' + ill_num
except NameError:
	author = ''
	print date + '\t' + author + '\t' + title + '\t' + lender + '\t' + borrower + '\t' + due + '\t' + '' + '\t' + ill_num
#print '\n'#for CLI prettiness

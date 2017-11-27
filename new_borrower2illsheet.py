#!/usr/bin/python

### FOR BORROWER RECORDS ###
# New and Improved for Columns that match up.

import re
from datetime import datetime

now = datetime.now()
year = now.year
month = now.month
day = now.day

date = "%i/%i/%i" % (month, day, year)

textfile = open(r'/tmp/accessRecord.txt', 'r')
filetext = textfile.read()
textfile.close()
splitext = list(filetext.splitlines())

for i in splitext:
	if re.search(r'(Author)', i) is not None:
		author = i[20:]
		author = author.strip()
	elif re.search(r'(Journal Title)',i) is not None:
		title = i[23:]
		title = title.strip()
	elif re.search(r'( Lender  )',i) is not None:
		lender = re.search(r'([A-Z]{5}.*)', i)
		lender = lender.group()
	elif re.search(r'(Patron\'s Last Name)',i) is not None:
		patron = i[20:]
		patron = patron.strip()
	elif re.search(r'(Due Date)',i) is not None:
		due = re.search(r'(\d+/\d+/\d{4})', i)
		due = due.group()
	elif re.search(r'(Request Number)',i) is not None:
		ill_num = ill_num = re.search(r'(\d{6,})', i)
		ill_num = ill_num.group()

#print '\n'
try:
	print date + '\t' + author + '\t' + title + '\t' + lender + '\t' + patron + '\t' + due + '\t' + '' + '\t' + ill_num
except NameError:
	author = ''
	print date + '\t' + author + '\t' + title + '\t' + lender + '\t' + patron + '\t' + due + '\t' + '' + '\t' + ill_num
#print '\n'

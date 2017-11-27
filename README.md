# access2google
Access2google is actually two modules that scrape data from Access PA lender (pending) or borrower (shipped or received) record to be stored in a Google Sheet.
They use pyautogui along with regex and slicing to select and copy all text from a record (left browser tab) parse the text for relevant data and ctrl+tab (right browser tab) for pasting into the spreadsheet, which has the columns Date, Author, Title,	From,	To,	Due[date],	Returned[date], ILL #, and Comments.  
One should assign keybindings to executables access_borrower and access_lender (I use super+B and super+N respectively) for a similar experience to copying and pasting with ctrl+c and ctrl+v.

Depends: bash, xclip, python2, python3, pyautogui, re

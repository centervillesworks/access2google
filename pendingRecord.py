#!/usr/bin/python3

##Start on AccessPA website in the BORROWER'S FULL RECORD DISPLAY
##of the record to be scraped

import pyautogui
from time import sleep as s

#pyautogui.hotkey('alt','tab')#not required for use with keybinding
#s(2)
pyautogui.click()
pyautogui.hotkey('ctrl','a')
#s(0.5)
pyautogui.hotkey('ctrl','c')

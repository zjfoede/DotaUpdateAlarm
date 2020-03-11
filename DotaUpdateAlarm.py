import webbrowser
import time
from time import strftime, localtime
import urllib.request
import sys
import os
import platform
 
blogPage = "http://blog.dota2.com"
page = urllib.request.urlopen(blogPage).read()
clearCommand = "clear"
 
if (platform.system() == 'Windows'):
    clearCommand = 'cls'
 
while True:
    newPage = urllib.request.urlopen(blogPage).read()
    if newPage != page:
        print("Update to the Dota 2 Blog found at  " + strftime("%a, %d %b %Y %H:%M:%S +0000", localtime())[:25])
        break
    else:
        time.sleep(15)

webbrowser.open(blogPage)

#!/usr/bin/env python3
# chmod +x main.py

import config
from log import log

from guizero import App, Text

# dislay time */

app = App(title="User Interface", width=config.displayWidth, height=config.displayHeight)
text0 = Text(app, "xx", grid=[1, 0], size=config.fontSize) # most recent speed test
text1 = Text(app, "xx", grid=[2, 0], size=config.fontSize)
text2 = Text(app, "xx", grid=[3, 0], size=config.fontSize)
text3 = Text(app, "xx", grid=[4, 0], size=config.fontSize)
text4 = Text(app, "xx", grid=[5, 0], size=config.fontSize) # oldest speed test

logFile = log(config.logFilePath)

def loop():
    """Loop used to update display"""
    recents = logFile.read('all')
    i = 0
    for runs in recents:
        data = config.conversion.capitalize() + ": " + str(runs["value"]) + " Time: " + runs["time"][0]
        if (i == 0):
            text0.value = data
        elif (i == 1):
            text1.value = data
        elif (i == 2):
            text2.value = data
        elif (i == 3):
            text3.value = data
        elif (i == 4):
            text4.value = data
            break
        i+=1
        
print('starting ui')

text0.repeat(100, loop)

app.display()

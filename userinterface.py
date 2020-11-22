import config
from log import read

from guizero import App, Text

app = App(title="User Interface", width=config.displayWidth, height=config.displayHeight)
title = Text(app, 'Speed:', grid=[0, 0])
text0 = Text(app, "xx", grid=[1, 0]) # most recent speed test
text1 = Text(app, "xx", grid=[2, 0])
text2 = Text(app, "xx", grid=[3, 0])
text3 = Text(app, "xx", grid=[4, 0])
text4 = Text(app, "xx", grid=[5, 0]) # oldest speed test

def loop():
    recents = read('recents')
    i = 0
    for runs in recents:
        if (i == 0):
            text0.value = runs["value"]
        elif (i == 1):
            text1.value = runs["value"]
        elif (i == 2):
            text2.value = runs["value"]
        elif (i == 3):
            text3.value = runs["value"]
        elif (i == 4):
            text4.value = runs["value"]
        i+=1
        
print('starting ui')

title.repeat(100, loop)

app.display()
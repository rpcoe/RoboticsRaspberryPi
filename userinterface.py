#!/usr/bin/env python3
# chmod +x main.py

import time

import config
from log import log
from guizero import App, TextBox

logFile = log(config.logFilePath)
app = App(title="User Interface", width=config.displayWidth, height=config.displayHeight)
text = TextBox(app, width="fill", height="fill", multiline=True, scrollbar=True)
text.text_size = config.fontSize

text.disable()

textBoxData = ""

def loop():
    """
    Loop used to update display
    """
    newData = logFile.read("all")

    global textBoxData
    for x in reversed(newData):
        textData = config.conversion.capitalize() + ": " + str(x["value"]) + " Time: " + x["time"][0] + "\n"
        if textData not in text.value:
            textBoxData = textData + textBoxData
            text.enable()
            text.value = textBoxData
            text.disable()

print("starting ui")

text.repeat(300, loop)

app.display()
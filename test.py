import time
# import random

import config
from log import log
from guizero import App, Text

logFile = log(config.logFilePath)
app = App(title="User Interface", width=config.displayWidth, height=config.displayHeight)
# text = TextBox(app, width="fill", height="fill", multiline=True, scrollbar=True)
text = Text(app, "xx", size=config.fontSize)

def runTest():
    """
    Just used for testing implementation of new commands
    """
    arr = logFile.read("all")
    print("for loop starting")
    for x in range(len(arr) -1, -1, -1):
        string = (config.conversion.capitalize() + ": " + str(arr[x]["value"]) + " Time: " + arr[x]["time"][0] + "\n")
        print(string)
        text.value += string
    # final = round(random.uniform(8.3, 14.5), 2)
    # newArr = logFile.read("all")
    # newArr.insert(0,{"value": final, "time": log.time()})
    # logFile.write("all", newArr)

# while True:
#     runTest()
#     time.sleep(2)

print("starting ui")

text.repeat(1000, runTest)

app.display()
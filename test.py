import time
# import random

import config
from log import log
from guizero import App, TextBox

logFile = log(config.logFilePath)
app = App(title="User Interface", width=config.displayWidth, height=config.displayHeight)
text = TextBox(app, width="fill", height="fill", multiline=True, scrollbar=True)

text.disable()

def runTest():
    """
    Just used for testing implementation of new commands
    """
    arr = logFile.read("all")
    data = "test"
    for x in range(len(arr), 0):
        text.enable()
        text.append(config.conversion.capitalize() + ": " + str(arr[x]["value"]) + " Time: " + arr[x]["time"][0])
        text.disable()
        # data += config.conversion.capitalize() + ": " + str(arr[x]["value"]) + " Time: " + arr[x]["time"][0] + "\n"
    # text.value = data
    # final = round(random.uniform(8.3, 14.5), 2)
    # newArr = logFile.read("all")
    # newArr.insert(0,{"value": final, "time": log.time()})
    # logFile.write("all", newArr)

# while True:
#     runTest()
#     time.sleep(2)

text.repeat(1000, runTest)

app.display()
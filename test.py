import time
import random
from log import log

logFile = log("log.json")

def runTest():
    """
    Just used for testing implementation of new commands
    """
    final = random.uniform(8.3, 14.5)
    newArr = logFile.read("recents")
    print(len(newArr))
    if (len(newArr) == 5):
        del newArr[-1]
    newArr.insert(0,{"value": final, "time": log.time()})
    logFile.write("recents", newArr)

while True:
    runTest()
    time.sleep(2)
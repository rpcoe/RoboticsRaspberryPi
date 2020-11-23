import time
import random
import log

def runTest():
    final = random.uniform(8.3, 14.5)
    newArr = log.read("recents")
    print(len(newArr))
    if (len(newArr) == 5):
        del newArr[-1]
    newArr.insert(0,{"value": final, "time": log.time()})
    log.write("recents", newArr)

while True:
    runTest()
    time.sleep(2)
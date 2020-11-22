import json

#parameters are the value you want to log and the name is a term used to refer to the value
def writeLog(name, value, logFile="log.json"):
    writeData = {}
    writeData[name] = value
    with open(logFile, 'r+') as f:
        data = json.load(f)
        data.update(writeData)
        f.seek(0)
        json.dump(data, f)
    print('%s, %s' % (name, value))
    
def readLog(name, logFile="log.json"):
    with open(logFile, 'r') as f:
        return json.load(f)[name]
        
def deleteLog(name, logFile="log.json"):
    with open(logFile, 'r+') as f:
        data =  json.load(f)
        there = False
        print(data)
        for x in data:
            if name in x:
                there = True
        if there:
            del data[x]
        #data.pop(name, None)
        data = json.dump(data, f)
        
print(readLog('math'))
deleteLog('math')
print(readLog('math'))
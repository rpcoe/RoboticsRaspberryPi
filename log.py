import json

from datetime import datetime


class log:
    def __init__(self, path="/home/pi/Documents/log.json"):
        self.path = path

    def setPath(self, pathAddress):
        """
        Sets log file's path
        """
        self.path = pathAddress

    #parameters are the value you want to log and the name is a term used to refer to the value
    def write(self, name, value):
        """
        Writes values to an inputted json file
        """
        writeData = {}
        writeData[name] = value
        with open(self.path, 'r') as f:
            data = json.load(f)
        
        data.update(writeData)
        
        with open(self.path, 'w') as fd:
            fd.seek(0)
            json.dump(data, fd)
        # print('%s, %s' % (name, value))

    #writes to a value in an object inside of the log file (e.g. "test": {"num": 12, "string": "Hello World"}  log.subWrite("test", "num", 41))
    def subWrite(self, name, subName, value):
        """
        Writes to a value inside of an object in inputted json file
        """
        val = read(name, self.path)
        val[subName] = value
        write(name, val, self.path)

    def read(self, name):
        """
        Outputs value of inputted name in json file
        """
        with open(self.path, 'r') as f:
            try:
                return json.load(f)[name]
            except Exception as e: 
                # print(e)
                print("Value not found")
            
    def delete(self, name):
        """
        Completely removes data from inputted json file
        """
        with open(self.path, 'r') as data_file:
            data = json.load(data_file)

        data.pop(name, None)

        with open(self.path, 'w') as data_file:
            data = json.dump(data, data_file)

    @staticmethod
    def time():
        """
        Static method that outputs an array [(minute, seconds, milliseconds), hour, (month, day, year)]
        """
        now = datetime.now()
        return now.strftime("%M:%S.%f")[:-3], now.strftime("%H"), now.strftime("%m/%d/%Y")
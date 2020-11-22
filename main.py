import config

from time import sleep
from objectspeed import checkSpeed

#run commands on startup
def initial():
	print("started")

#run loop commands
def loop():
    currentSpeed = checkSpeed()
    if currentSpeed != None:
        print("something there")

initial()

while True:
	loop()
	sleep(config.loopDelay)
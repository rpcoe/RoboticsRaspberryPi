import config
import time

from gpiozero import Button

first = Button(config.firstInput)
last = Button(config.lastInput)
firstActive = False
lastActive = False

def firstEvent():
	global firstActive
	global lastActive
	if not(firstActive):
		firstActive = True
		lastActive = False
		global firstTime
		firstTime = time.time()
		#print("top activated")
		#print(firstTime)
	
def lastEvent():
	global lastActive
	global firstTime
	if firstTime != 0 and not(lastActive):
		#print("bottom activated")
		lastActive = True
		timeDiff = time.time() - firstTime
		print(1/(timeDiff*(4*(3/config.lightSensorDistance))))
		return 1/(timeDiff*(4*(3/config.lightSensorDistance)))

def checkSpeed():
	#global firstActive
	#global lastActive
	#global firstTime
	if first.is_pressed:
		firstEvent()
	elif last.is_pressed:
		return lastEvent()
	else:
		global firstActive
		#global lastActive
		#global firstTime
		firstActive = False
		#lastActive = False
		#firstTime = 0
		#print("nothing there")
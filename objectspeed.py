import config
import time

from gpiozero import Button

first = Button(config.firstInput)
last = Button(config.lastInput)
firstActive = False
lastActive = False
firstTime = None

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
		final = 1/(timeDiff*(4*(3/config.lightSensorDistance)))
		if (config.conversion == 'fpm'):
			final *= 60
		elif (config.conversion == 'mph'):
			final *= 3600/5280
		elif (config.conversion == 'custom'):
			final = config.customConversion(final)
		print(final)
		return final

def checkSpeed():
	if first.is_pressed:
		firstEvent()
	elif last.is_pressed:
		return lastEvent()
	else:
		global firstActive
		firstActive = False
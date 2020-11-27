import config
import log
import time

from gpiozero import Button

first = Button(config.firstInput)
last = Button(config.lastInput)
firstActive = False
lastActive = False
firstTime = None

def firstEvent():
	"""
	Notes time when an object passes in front of the first light sensor https://github.com/griffing52/RoboticsRaspberryPi
	"""
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
	"""
	Compares current time to time when object passed in front of the first light sensor and calculates the speed
	"""
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
			final = final * (3600/5280)
			print(final)
		elif (config.conversion == 'custom'):
			final = config.customConversion(final)
		newArr = log.read("recents")
		if (len(newArr) == 5):
			del newArr[-1]
		newArr.insert(0,{"value": final, "time": log.time()})
		log.write("recents", newArr)
		print(final)
		return final

def checkSpeed():
	"""
	Checks to see if an object is in front of the light sensors. Runs associated functions
	"""
	if first.is_pressed:
		firstEvent()
	elif last.is_pressed:
		return lastEvent()
	else:
		global firstActive
		firstActive = False
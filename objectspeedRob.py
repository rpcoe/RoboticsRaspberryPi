
import config
from log import log
import time

from gpiozero import Button

logFile = log(config.logFilePath)
first = Button(config.firstInput)
last = Button(config.lastInput)
firstTime = 0
lastTime = 0
timeDiff = 0

def firstEvent():
	"""
	Notes time when an object passes in front of the first light sensor
	"""
	global firstTime
	global lastTime
	if firstTime == 0:
	    firstTime = time.time()
	    #print("test")
	
	while (not(last.is_pressed)):  # try wait for press  with timeout??
                """
		lastTime = time.time()
		timeDiff = lastTime - firstTime
		if(timeDiff > .200) :
                        print("Too Slow")
                        break
		#print(lastTime)
		"""
	#timeDiff = lastTime - firstTime
	
	#print(last)
	#last.wait_for_press(1)
	
	timeDiff= time.time() - firstTime
	final = config.lightSensorDistance/timeDiff/12
	final = round(final,2)
	print(final)
	firstTime = 0


def setUp():
	# """
	# Checks to see if an object is in front of the light sensors. Runs associated function/s
	# """
	#last.when_pressed = lastEvent
	first.when_pressed = firstEvent


def reset():
	global firstTime
	"""
	if (firstTime != 0):
		if (time.time() - firstTime > 4):
			print("firstTime back to 0")
			firstTime = 0
	"""
	#else:
	#	firstTime = 0
	# except:
	# 	print(f'reset Error; firstTime {firstTime}')

def measureSpeed():
        global firstTime
	#while True:
		# reset()
		
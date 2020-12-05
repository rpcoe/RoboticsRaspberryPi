#inputs
lastInput = 24
firstInput = 23

#loop variables
loopDelay = 0.00001 # delay between each running the loop function in seconds

#file specific variables
logFilePath = "/home/pi/Documents/log.json"
lightSensorDistance = 1.5 # distance in inches, 1 hole separation = 3 inches, 0 hole = 1.5 inches

#uncomment desired unit for the output of the objectspeed file
conversion = 'fps' # feet per second
# conversion = 'fpm' # feet per minute
# conversion = 'mph' # miles per hour

# conversion = 'mps' #add a custom conversion in form of function with parameter as the feet per second value. Change this value to whatever your custom conversion is called
def customConversion(x): # ex. feet per second to meters per second; change numerical value to what ever conversion you desire
    return x * 3.281

#user interface settings
displayWidth = 800
displayHeight = 480
fontSize = 30
recentBalls = 5 # amount of balls displayed on the userinterface as well as recorded in the recents array in log.json

#tests
test = 3

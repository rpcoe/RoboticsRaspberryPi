#inputs
lastInput = 24
firstInput = 23

#loop variables
loopDelay = 0.00001 #delay between each running the loop function in seconds

#file specific variables
lightSensorDistance = 3 #distance in inches, 1 hole separation = 3 inches, 0 hole = 1.5 inches

#uncomment desired unit for the output of the objectspeed file
conversion = 'fps' # feet per second
# conversion = 'fpm' # feet per minute
# conversion = 'mph' # miles per hour

# conversion = 'custom' #add a custom conversion in form of function with parameter as the feet per second value
def customConversion(x): #ex. feet per second to meters per second; change numerical value to what ever conversion you desire
    return x * 3.281

#user interface settings
displayWidth = 500
displayHeight = 500

#tests
test = 3

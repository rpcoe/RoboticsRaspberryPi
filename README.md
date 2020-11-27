# RoboticsRaspberryPi

2 light sensors display the speed of an object moving in front of it in feet per second (this can be changed). The 5 most recent speeds are displayed on the user interface.

# Setup

From the two light sensors, plug the red wires into 5v and the black wires into ground.

# Framework

There are 3 important files: [main.py](#mainpy), [config.py](#configpy), and [userinterface.py](#userinterfacepy). 

## main.py

### What it does

This file is the main loop. All commands apart from the user interface are run through this file.

### How to use

  1. Ensure importation of your command or function.
  2. Add function that is supposed to loop in the main.py loop function

### Example

```python
from objectspeed import checkSpeed
```
```python
def loop():
    checkSpeed() # adding checkSpeed function to the loop from objectspeed file
```

## config.py

### What it does

A single place to store variables which affect how the program runs

### How to use
  
  Change variable values to change how functions work

### Example

This is a variable used in the objectspeed file. Changing this variable will specify the distance between the two light sensors, which is necessary for the calculation of speed
```python
lightSensorDistance = 3 # distance in inches, 1 hole separation = 3 inches, 0 hole = 1.5 inches
```

## userinterface.py

### What it does

The information which the user can see at a glance. This updates on a different loop compared to the main.py loop.

### How to use

  1. Create text using guizero library
  2. Change text using guizero library in loop function

### Example

```python
text4 = Text(app, "xx", grid=[5, 0]) # creation of text
```
```python
def loop():
    recents = read('recents') # views content of array in log.json file
    text4.value = recents[-1]["value"] # sets the initialized text to the value of the last element in the recents array 
```

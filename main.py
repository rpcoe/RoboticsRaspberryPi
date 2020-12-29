#!/usr/bin/env python
# chmod +x main.py

import config

from time import sleep
# from objectspeed import checkSpeed
import objectspeedRob as osc

def initial():
    """Run commands on main.py startup"""
    print("Starting...")
    osc.setUp()


#run loop commands
"""
def loop():
    # Run loop commands with a delay set in conifg.py (loopDelay)
    osc.reset() 
    # checkSpeed()
"""

initial()

while True:
	#loop()
	#sleep(config.loopDelay)
    osc.measureSpeed()
#!/usr/bin/python
from phue import Bridge
import random
import logging
import time
import sys
logging.basicConfig()

b = Bridge('10.10.11.16','UUANOzMU9w9h1tqc-rAYZ99to5xU0lJjwwWLK4OZ') # Enter bridge IP here.

interval = 5

#If running for the first time, press button on bridge and run with b.connect() uncommented
#b.connect()

def main():
  while True:   
    b.get_light_objects()

    for x in range (1,9):
        b.set_light(x, 'on', True)
        time.sleep(2)
        b.set_light(x, 'on', False)

    time.sleep(5)

if __name__ == "__main__":
    sys.exit(main())

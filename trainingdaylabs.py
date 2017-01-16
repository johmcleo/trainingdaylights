#!/usr/bin/python

import requests
from phue import Bridge
import random
import logging
import time
import sys
logging.basicConfig()

b = Bridge('10.10.11.16','UUANOzMU9w9h1tqc-rAYZ99to5xU0lJjwwWLK4OZ') # Enter bridge IP here.

arch = ['Enterprise Networks','Datacenter','Collaboration','Security','Devnet','Meraki']

whitexy = [0.4449, 0.4066]
bluexy = [0.1684, 0.0416]
greenxy = [0.17, 0.7]
yellowxy = [0.4449, 0.4066]
orangexy = [0.577, 0.3943]
redxy = [0.577, 0.3943]


def main():
    while True:
      for x in arch: 
          url = 'http://ec2-54-90-189-154.compute-1.amazonaws.com/api/labs/arch/' + x
          r = requests.get(url)
          if len(r.json()) == '0':
                    print ("Light Off!")
          if 1 <= len(r.json()) <= 2:
                   b.set_light(x, 'on', True)
                   b.set_light(x, 'bri', 254)
                   b.set_light(x, 'xy', whitexy)
          if 3 <= len(r.json()) <= 5:
                   b.set_light(x, 'on', True)
                   b.set_light(x, 'bri', 254)
                   b.set_light(x, 'xy', bluexy)
	  if 6 <= len(r.json()) <= 8:
                   b.set_light(x, 'on', True)
                   b.set_light(1, 'bri', 254)
		   b.set_light(x, 'xy', greenxy)
	  if 9 <= len(r.json()) <= 12:
                   b.set_light(x, 'on', True)
                   b.set_light(1, 'bri', 254)
		   b.set_light(x, 'xy', yellowxy)
          if 13 <= len(r.json()) <= 16:
                   b.set_light(x, 'on', True)
                   b.set_light(1, 'bri', 254)
		   b.set_light(x, 'xy', orangexy)
          if len(r.json()) > 16:         
                   b.set_light(x, 'on', True)
                   b.set_light(1, 'bri', 254)
                   b.set_light(x, 'xy', redxy)

if __name__ == "__main__":
    sys.exit(main())

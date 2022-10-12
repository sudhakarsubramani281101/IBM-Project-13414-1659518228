#LED blinking

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
cnt = 0
FREQ = 1
RED_LED = 4
GPIO.setup(RED_LED, GPIO.OUT)
while True:
 if cnt == 0 :
 GPIO.output(RED_LED, False)
 cnt = 1
 else:
 GPIO.output(RED_LED, True)
 cnt = 0
time.sleep(FREQ)
GPIO.cleanup() 


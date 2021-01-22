import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
while 1:
	try:
		GPIO.output(7,True)
		time.sleep(1)
		GPIO.output(7,False)
		time.sleep(1)
	except KeyboardInterrupt:
		GPIO.cleanup()

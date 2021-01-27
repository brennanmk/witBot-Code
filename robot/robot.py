# This file contains all the critical robot handling code
import RPi.GPIO as GPIO
import time
import robot.bot_config as config

MOTOR_NAMES = ('LEFT','RIGHT')

def init():
	GPIO.setmode(GPIO.BCM)
	# Setup line sensor
	GPIO.setup(config.PINS['line/sense'],GPIO.IN)
	# Setup ultrasonic sensor
	GPIO.setup(config.PINS['ultrasonic/trig'],GPIO.OUT)
	GPIO.setup(config.PINS['ultrasonic/echo'],GPIO.IN)
	GPIO.output(config.PINS['ultrasonic/trig'],0)

def getLineSensor():
	return GPIO.input(config.PINS['line/sense'])

def getDistanceCM():

	pin_trigger = config.PINS['ultrasonic/trig']
	pin_echo = config.PINS['ultrasonic/echo']

	GPIO.output(pin_trigger,1)
	time.sleep(0.0001)
	GPIO.output(pin_trigger,0)

	# Wait for pulse
	while GPIO.input(pin_echo) == 0:
		pulse_start = time.time()
	while GPIO.input(pin_echo) == 1:
		pulse_end = time.time()
	# Returns distance in CM
	return round((pulse_end - pulse_start)*17150,2)

def getDistanceIN():
	return round(getDistanceCM() * 0.3937008,2)

def setMotorPower(motor,power):
	# Validate inputs
	power = min(100,max(power,-100))
	if motor not in MOTOR_NAMES:
        	return
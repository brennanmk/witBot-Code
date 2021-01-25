import RPi.GPIO as GPIO
import time

pin_trigger = -1
pin_echo = -1

def init(trig,echo):
    pin_trigger = trig
    pin_echo = echo
    GPIO.setup(echo, GPIO.IN)
    GPIO.setup(trig, GPIO.OUT)
    GPIO.output(trig,0)

def read_cm():
    GPIO.output(trig,1)
    time.sleep(0.0001)
    GPIO.output(trig,0)

    # Wait for pulse
    while GPIO.input(echo) == 0:
        pulse_start = time.time()
    while GPIO.input(echo) == 1:
        pulse_end = time.time()

    # Returns distance in CM
    return round((pulse_end - pulse_start)*17150,2)

def read_in():
    return read_cm() * 0.3937008 
import RPi.GPIO as GPIO
from time import sleep

channel = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

while True:
	print("-> Turning on  LED...")
	GPIO.output(channel, GPIO.HIGH)
	sleep(2)
	print("-> Turning off LED...")
	GPIO.output(channel, GPIO.LOW)
	sleep(2)

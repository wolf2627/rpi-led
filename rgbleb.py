import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

channel = [19, 13, 12]

GPIO.setup(channel, GPIO.OUT)

for c in channel:
	print(f"Checking channel {c}")
	GPIO.output(c, GPIO.LOW)
	sleep(1)
	GPIO.output(c, GPIO.HIGH)

# GPIO.output(channel, GPIO.HIGH)
# GPIO.output(channel, GPIO.LOW)



try:
	while True:
		try:
			n = int(input("Enter a number between 0-7: "))

			if n < 0 or n >= 8:
				print("Invalid input range. Give Between 0 - 7..")
				continue

			rgb = format(n , '03b')
			for i, c in enumerate(channel):
				GPIO.output(c , not bool(int(rgb[i])))

		except ValueError:
			print("Invalid Input, Try again...")
			continue


except KeyboardInterrupt:
	GPIO.cleanup()
	print("Quitting...")

import RPi.GPIO as GPIO

channel = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

p = GPIO.PWM(channel, 1000) # 0.5 

p.start(100)

i = None

try:
	while i != 'q':

		try:
			# d = input('set a duty cycle: ')
			d = input("Set Brightness: ")
			# f = input('set a frequency: ')

			# if(d == 'q' or f == 'q'):
			# 	break

			if(d == 'q'):
				break

			p.ChangeDutyCycle(int(d))
			# p.ChangeFrequency(int(f))

		except ValueError as e:
			print("Value Error Rasied, Skipping..")
			pass
except KeyboardInterrupt as e:
	print("Received Ctrl+c --> Quitting...")
	pass

p.stop()
GPIO.cleanup()
print("I am exiting")

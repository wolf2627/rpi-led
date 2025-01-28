import time
import RPi.GPIO as GPIO

class RGBA():
    def __init__(self, r, g, b):
        GPIO.setmode(GPIO.BCM)
        self.channel = [r, g, b]
        GPIO.setup(self.channel, GPIO.OUT)
        
        self.r = GPIO.PWM(r, 60)
        self.g = GPIO.PWM(g, 60)
        self.b = GPIO.PWM(b, 60)
        
        # Start PWM with 0% duty cycle
        self.r.start(0)
        self.g.start(0)
        self.b.start(0)
        
    def setColor(self, r, g, b):
        print("Setting Color...")
        
        # r = max(0, min(100, (100-(r / 255) * 100)))
        # g = max(0, min(100, (100-(g / 255) * 100)))
        # b = max(0, min(100, (100-(b / 255) * 100)))
        
        r = 100 - (r / 255) * 100
        g = 100 - (g / 255) * 100
        b = 100 - (b / 255) * 100
        
        self.r.ChangeDutyCycle(r)
        self.g.ChangeDutyCycle(g)
        self.b.ChangeDutyCycle(b)
        
    def cleanup(self):
        self.r.stop()
        self.g.stop()
        self.b.stop()
        GPIO.cleanup()


try:
    led = RGBA(19, 13, 12)
    led.setColor(162, 210, 255)  
    time.sleep(3)           
finally:
    led.cleanup()

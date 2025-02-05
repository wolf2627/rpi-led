import time
import RPi.GPIO as GPIO
from colour import Color

class RGBA():
    def __init__(self, r, g, b):
        GPIO.setmode(GPIO.BCM)
        self.channel = [r, g, b]
        GPIO.setup(self.channel, GPIO.OUT)
        
        self.r = GPIO.PWM(r, 120)
        self.g = GPIO.PWM(g, 120)
        self.b = GPIO.PWM(b, 120)
        
        # Start PWM with 0% duty cycle
        self.r.start(0)
        self.g.start(0)
        self.b.start(0)
        
    def setColor(self, r, g, b):
        print("Setting Color...")
        
        r = 100 - (r / 255) * 100
        g = 100 - (g / 255) * 100
        b = 100 - (b / 255) * 100
        
        self.r.ChangeDutyCycle(r)
        self.g.ChangeDutyCycle(g)
        self.b.ChangeDutyCycle(b)
        
     # 0 - 100 (for color module)   
    def setRGB(self, rgb):

        r = abs(rgb[0] * 100 - 100)
        g = abs(rgb[1] * 100 - 100)
        b = abs(rgb[2] * 100 - 100)
        # print(r, b, b)
        self.r.ChangeDutyCycle(r)
        self.g.ChangeDutyCycle(g)
        self.b.ChangeDutyCycle(b)
        
    def cleanup(self):
        self.r.stop()
        self.g.stop()
        self.b.stop()
        GPIO.cleanup()


try:
    GPIO.cleanup()
    led = RGBA(19, 13, 12)

    # while True:
    #     col = input("Enter any color: ")
    #     led.setRGB(Color(col).rgb) 

    print("Generating Colors..")    
    while True:
        for c in Color("red").range_to(Color("blue"), 100):
            led.setRGB(c.rgb)
            time.sleep(0.03)
    
        for c in Color("blue").range_to(Color("red"), 100):
            led.setRGB(c.rgb)
            time.sleep(0.03)
except:
    print("Exiting")
         
finally:
    led.cleanup()

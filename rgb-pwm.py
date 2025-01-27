import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

channel = [19, 13, 12]

GPIO.setup(channel, GPIO.OUT)

r = GPIO.PWM(19, 1000)
g = GPIO.PWM(13, 1000)
b = GPIO.PWM(12, 1000)

r.start(100)
sleep(1)
g.start(100)
sleep(1)
b.start(100)
sleep(1)

try:
    while True:
        try:
            
            choice = input('R or G or B: ')
            
            if choice.lower() == 'r':
                rd = input("Red:  ")

                # Quit if the user enters 'q'
                if rd.lower() == 'q':
                    break

                duty_cycle = int(rd)
                if 0 <= duty_cycle <= 100:
                    r.ChangeDutyCycle(duty_cycle)  # Update duty cycle
                else:
                    print("Please enter a value between 0 and 100.")
                    
            elif choice.lower() == 'g':
                gd = input("Green:  ")

                # Quit if the user enters 'q'
                if gd.lower() == 'q':
                    break

                duty_cycle = int(gd)
                if 0 <= duty_cycle <= 100:
                    g.ChangeDutyCycle(duty_cycle)  # Update duty cycle
                else:
                    print("Please enter a value between 0 and 100.")
                    
            elif choice.lower() == 'b':
                bd = input("Blue:  ")

                # Quit if the user enters 'q'
                if bd.lower() == 'q':
                    break

                duty_cycle = int(bd)
                if 0 <= duty_cycle <= 100:
                    b.ChangeDutyCycle(duty_cycle)  # Update duty cycle
                else:
                    print("Please enter a value between 0 and 100.")
            else:
                print("Invalid choice. Please enter 'R', 'G', or 'B'.")

           
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 100, or 'q' to quit.")

except KeyboardInterrupt:
    print("\nReceived Ctrl+C --> Quitting...")

finally:
    # Cleanup GPIO and stop PWM
    r.stop()
    g.stop()
    b.stop()
    GPIO.cleanup()
    print("I am exiting")

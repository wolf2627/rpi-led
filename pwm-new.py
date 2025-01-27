import RPi.GPIO as GPIO

channel = 19  # GPIO pin to use for PWM output

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

# Initialize PWM with a frequency of 1000 Hz
p = GPIO.PWM(channel, 1000)

# Start PWM with 100% duty cycle (fully ON)
p.start(100)

try:
    while True:
        try:
            # Prompt user to input brightness as duty cycle
            d = input("Set Brightness (0-100, or 'q' to quit): ")

            # Quit if the user enters 'q'
            if d.lower() == 'q':
                break

            # Convert input to integer and validate range
            duty_cycle = int(d)
            if 0 <= duty_cycle <= 100:
                p.ChangeDutyCycle(duty_cycle)  # Update duty cycle
            else:
                print("Please enter a value between 0 and 100.")
        
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 100, or 'q' to quit.")

except KeyboardInterrupt:
    print("\nReceived Ctrl+C --> Quitting...")

finally:
    # Cleanup GPIO and stop PWM
    p.stop()
    GPIO.cleanup()
    print("I am exiting")

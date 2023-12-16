# A generic class to get Raspberry Pi GPIO pin states
# from the RPi.GPIO package. This class can be configured
# to read (INPUT) or write (OUTPUT) but not both at the same time

import RPi.GPIO as GPIO

class ToggleSwitch:
    def __init__(self, pin, mode):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)

        # Config switch as either INPUT or OUTPUT
        # throw an error if neither is passed
        if mode.lower() == 'input':
            GPIO.setup(self.pin, GPIO.IN)
        elif mode.lower() == 'output':
            GPIO.setup(self.pin, GPIO.OUT)
        else:
            raise ValueError("Invalid mode provided. Mode should be 'input' or 'output'.")
        
    def read(self):
        if GPIO.gpio_function(self.pin) == GPIO.IN:
            return GPIO.input(self.pin)
        else:
            raise RuntimeError("GPIO pin not set as INPUT")
        
    def write(self, value):
        if GPIO.gpio_function(self.pin == GPIO.OUT):
            GPIO.output(self.pin, value)
        else:
            raise RuntimeError("GPIO pin not set as OUTPUT")
        
    def cleanup(self):
        GPIO.cleanup(self.pin)
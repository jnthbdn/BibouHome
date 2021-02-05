import time

from rpi_rf  import RFDevice
import RPi.GPIO as GPIO

class RFSwitch:

    def __init__(self, gpio, invert_output=False):
        self.device = RFDevice(gpio)
        self.device.tx_repeat = 5
        self.gpio = gpio

        #~self.low  = GPIO.HIGH if invert_output else GPIO.LOW
        #~self.high = GPIO.LOW if invert_output else GPIO.HIGH
        self.low  = GPIO.LOW
        self.high = GPIO.HIGH

    def __del__(self):
        self.device.cleanup()

    def usleep(self, t):
        time.sleep( t / 1000000.0 )

    def send_decimal(self, value, lengthMsg=24, protocol=1, pulseWidth=185):
        self.device.enable_tx()
        self.device.tx_code( value, protocol, pulseWidth, lengthMsg )
        self.device.disable_tx()

    def send_timing(self, values):

        GPIO.setmode(GPIO.BCM)
        GPIO.setup( self.gpio, GPIO.OUT )
        GPIO.output( self.gpio, self.low )

        is_low = False

        for i in range( 0, 5 ):
            for t in values:
                if is_low :
                    GPIO.output( self.gpio, self.low )
                else:
                    GPIO.output( self.gpio, self.high )

                is_low = not is_low
                time.sleep( t / 1000000.0 )

        GPIO.output( self.gpio, self.low )
        GPIO.cleanup( self.gpio )

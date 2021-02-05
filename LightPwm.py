import wiringpi

# Control light with hardware pwm
class LightPwm:

    def __init__(self, gpio_pin):
        self.pin = gpio_pin
        wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode( gpio_pin, wiringpi.PWM_OUTPUT )
        wiringpi.pwmSetRange( 100 )
        wiringpi.pwmWrite( gpio_pin, 0 )
        
    def __del__(self):
        pass

    def set_value(self, value):
        if value > 100:
            value = 100
        elif value < 0:
            value = 0

        wiringpi.pwmWrite( self.pin, value )

    def on(self):
        self.set_value(100)


    def off(self):
        self.set_value(0)


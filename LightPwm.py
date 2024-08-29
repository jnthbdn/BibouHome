import pigpio
import atexit

# Control light with hardware pwm
class LightPwm:

    def __init__(self, gpio_pin):
        self.pin = gpio_pin
        self.pi = pigpio.pi()
        self.pi.hardware_PWM(self.pin, 800, 0)
        self.pi.set_PWM_range(self.pin, 100)

    def __del__(self):
        self.pi.stop()

    def set_value(self, value):
        if value > 100:
            value = 100
        elif value < 0:
            value = 0

        self.pi.set_PWM_dutycycle(self.pin, value )

    def on(self):
        self.set_value(100)


    def off(self):
        self.set_value(0)


if __name__ == '__main__':
    import time

    light = LightPwm(13)

    print("===== LightPWM Main =====")

    while(True):
        for dc in range(0, 101, 10):
            light.set_value(dc)
            time.sleep(0.5)

        for dc in range(100, -1, -10):
            light.set_value(dc)
            time.sleep(0.5)

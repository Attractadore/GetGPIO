import RPi.GPIO as GPIO

pins = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
power_pin = 17
compare_pin = 4

max_voltage = 3.3

def digitalToVoltage(value):
    return value / 255 * max_voltage

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pins, GPIO.OUT)
    GPIO.setup(leds, GPIO.OUT)
    GPIO.setup(power_pin, GPIO.OUT)
    GPIO.setup(compare_pin, GPIO.IN)
    GPIO.output(pins, [0] * len(pins))
    GPIO.output(leds, [0] * len(leds))

def teardown():
    GPIO.output(pins, [0] * len(pins))
    GPIO.output(leds, [0] * len(leds))
    GPIO.output(power_pin, 0)
    GPIO.cleanup()

def bDigitalGreater():
    return not GPIO.input(compare_pin)

def wrapMain(f, bWrap=True):
    if bWrap:
        try:
            setup()
            f()
        except:
            pass
        finally:
            teardown()
    else:
        setup()
        f()
        teardown()
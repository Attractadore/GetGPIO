import RPi.GPIO as GPIO

from num2dac import num2dac, dec2bin
from util import bDigitalGreater, digitalToVoltage, wrapMain, leds
from time import sleep

def getVoltageBinary():
    low = 0
    high = 256
    while (low + 1 < high):
        mid = (low + high) // 2
        num2dac(mid)
        sleep(0.001)
        if bDigitalGreater():
            high = mid
        else:
            low = mid
    return low

def num2Leds(value):
    num_lit = round(value / 32)
    light_up = [0] * (8 - num_lit) + [1] * num_lit
    GPIO.output(leds, light_up)

def main():
    while(True):
        v = getVoltageBinary()
        num2Leds(v)
        print("Binary  value: {0}, Analog value: {1:.2f}V".format(v, digitalToVoltage(v)))

if __name__ == "__main__":
    wrapMain(main, True)
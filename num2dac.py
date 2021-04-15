import RPi.GPIO as GPIO

from util import pins

def dec2bin(value):
    lst = [0] * 8
    for i in range(8):
        lst[7-i] = value & 1
        value >>= 1
    return lst

def num2dac(value):
    GPIO.output(pins, dec2bin(value))
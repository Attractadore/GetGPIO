from num2dac import num2dac

from util import bDigitalGreater, digitalToVoltage, wrapMain

from time import sleep

def getVoltage():
    for i in range(256):
        num2dac(i)
        sleep(.001)
        if (bDigitalGreater()):
            break
    return i

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

def main():
    while(True):
        #v = getVoltage()
        #print("Digital value: {0}, Analog value: {1:.2f}V".format(v, digitalToVoltage(v)))
        v = getVoltageBinary()
        print("Binary  value: {0}, Analog value: {1:.2f}V".format(v, digitalToVoltage(v)))

if __name__ == "__main__":
    wrapMain(main)
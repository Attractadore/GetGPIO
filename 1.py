from num2dac import num2dac

from util import wrapMain

def main():
    while(True):
        v = 0
        try:
            v = int(input("Enter value (-1 to exit) > "))
            if (v < -1 or v > 255):
                raise ValueError
        except ValueError:
            print("Please enter a valid value")
        if (v == -1):
            break
        num2dac(v)
        print("{0} = {1:.2f}V".format(v, v / 255 * 3.3))

if __name__ == "__main__":
    wrapMain(main)
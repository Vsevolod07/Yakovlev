import RPi.GPIO as gpio
dac = [8,11,7,1,0,5,12,6]

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

def binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

b = 1

try:
    while(b > 0):
        a = input("Input a number from 0 to 255")
        gpio.output(dac,binary(int(a)))
        print("expexted value of voltage")
        print(3.3 * int(a) / 256)

except KeyboardInterrupt:
    print("Keybord exception")
except ValueError:
    print("Invalid input of number")
except RuntimeError:
    print("Number is to big")


finally:
    gpio.output(dac,0)
    gpio.cleanup()
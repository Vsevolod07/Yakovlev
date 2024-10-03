import RPi.GPIO as gpio
import time
dac = [8,11,7,1,0,5,12,6]

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

def binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

b = 1

try:
    t = input("Input a period")
    while(b > 0):
        for i in range(256):
            gpio.output(dac,binary(i))
            print(3.3 * i / 256)
            time.sleep(float(t) / 512)


        for i in range(255, 0, -1):
            gpio.output(dac,binary(i))
            print(3.3 * i / 256)
            time.sleep(float(t) / 512)

finally:
    gpio.output(dac,0)
    gpio.cleanup()
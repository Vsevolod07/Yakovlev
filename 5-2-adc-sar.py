import RPi.GPIO as gpio
import time
dac = [8,11,7,1,0,5,12,6]
comp = 14
troyka = 13

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial = gpio.HIGH)
gpio.setup(comp, gpio.IN)

def binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    s = 0
    for i in range(7, -1, -1):
        s += 2 ** i
        gpio.output(dac, binary(s))
        time.sleep(0.02)
        a = gpio.input(comp)
        if a == 1:
            s -= 2 ** i

    return s

b = 1

try:
    while(b > 0):
        c = adc()
        if c != 0 and c:
            print(c, 3.3 * c / 256, sep = ' ')
        

finally:
    gpio.output(dac,0)
    gpio.output(troyka,0)
    gpio.cleanup()
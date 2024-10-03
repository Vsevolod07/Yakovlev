import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(19, gpio.OUT)

p = gpio.PWM(19,1000)
p.start(0)
b = 1
try:
    while (b > 0):
        a = input("Input a number")
        if (int(a) >= 0 and int(a) <=100):
            p.start(int(a))
        else:
            print("Incorrect number")

        print (int(a) * 3.3 / 100)

finally:
    gpio.output(19,0)
    gpio.cleanup()

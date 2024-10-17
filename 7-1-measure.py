import RPi.GPIO as gpio
import time
import matplotlib.pyplot as plt

dac = [8,11,7,1,0,5,12,6]
comp = 14
troyka = 13
leds = [2,3,4,17,27,22,10,9]

def binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def bileds(c):
    gpio.output(leds, binary(c))

def adc():
    s = 0
    for i in range(7, -1, -1):
        s += 2 ** i
        gpio.output(dac, binary(s))
        time.sleep(0.001)
        a = gpio.input(comp)
        if a == 1:
            s -= 2 ** i

    return (s * 3.3 / 256)

gpio.setmode(gpio.BCM)

gpio.setup(dac, gpio.OUT)
gpio.setup(leds, gpio.OUT)
gpio.setup(troyka, gpio.OUT)
gpio.setup(comp, gpio.IN)

a = 0
t1 = 0
t2 = 0
count = 0

try:
    #Получение экспериментальных значений
    x = list()
    t1 = time.time()
    gpio.output(troyka, 1)

    while (a <= 3.3 * 0.97):
        a = adc()
        print('Зарядка конденсатора')
        print(a)
        x.append(a)
        count += 1

    gpio.output(troyka, 0)

    while (a >= 3.3 * 0.02):
        a = adc()
        print('Разрядка конденсатора')
        print(a)
        x.append(a)
        count += 1

    t2 = time.time()

    print("time", (t2 - t1))
    print(count)

    #Добавление данных в файлы

    with open('data.txt', 'w') as f:
        for i in x:
            f.write(str(i) + '\n')

    with open('settings.txt', 'w') as f:
        f.write(str(3.3 / 256) + '\n')
        f.write(str(1/(t2 - t1)/count) + '\n')

    #Построение графиков
    tm=[i * (t2 - t1) / count for i in range(count)]
    plt.plot(tm,x)
    plt.xlabel('Время')
    plt.ylabel('Напряжения')
    plt.show()


finally:
    gpio.output(dac,0)
    gpio.output(troyka,0)
    gpio.cleanup()



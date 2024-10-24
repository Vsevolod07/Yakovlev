import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

y = []
set = []
x = []
c = 0

with open('data1.txt', 'r') as f:
        for line in f:
            y.append([float(i) * 3.3 / 256 for i in line.split()])
            c += 1

with open('settings1.txt', 'r') as f1:
        for line in f1:
            set.append([float(i) for i in line.split()])

y = np.array(y)
set = np.array(set)

freq = float(set[0])
step = float(set[1])

x = np.linspace(0.0, freq * c, c)

fig, ax=plt.subplots(figsize = (16,9), dpi = 150)

plt.plot(x,y,'r',marker = '*',label = '$U(t)$',linewidth = 0.7,markersize = 1)
plt.text(7, 2.5, r'$Время$')
plt.text(8.4, 2.5, r'$зарядки = 5,14с$')
plt.text(7, 2, r'$Время$')
plt.text(8.4, 2, r'$разрядки = 6,89с$')

plt.axis([0,13,0,4])
ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())

plt.grid(which = 'major', color = 'black')
plt.grid(which = 'minor', linestyle = ':', color = 'grey')

plt.legend()

plt.ylabel('Напряжение, В')
plt.xlabel('Время, с')
plt.suptitle('Процесс заряда и разряда конденсатор в RC цепочке')

plt.show()






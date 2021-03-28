import sys
import csv
import matplotlib.pyplot as plt
from dateutil.parser import parse
file= open("dane.csv", "r")
iterator = csv.reader(file, delimiter= ",")
lista = list(iterator)
print(lista)
plt.subplot(2,1,1)
czas=[]
temperatura=[]
for element in lista:
    czas.append(parse(element[0]))
    temperatura.append(float(element[1]))

plt.plot(czas, temperatura)
plt.show()


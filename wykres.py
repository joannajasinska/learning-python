import sys
import csv
file= open("dane.csv", "r")
iterator = csv.reader(file, delimiter= ",")
lista = list(iterator)
print(lista)

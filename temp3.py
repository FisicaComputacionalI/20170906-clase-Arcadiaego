import numpy as np
import pylab as pl
#Crea un vector (arreglo) con los valores del eje X
x = [ 6000, 7000, 8000, 9000, 10000]
#Crea un vector (arreglo) con valores en el eje Y para cada valor en el eje X
y = [ 73, 80, 85, 87, 89]
#Grafica el vector x contra el vector y
pl.plot(x, y)
pl.axis([5000,12000, 60,100])
pl.plot(x, y, 'b*')

#Crea un vector (arreglo) con los valores del eje X
x1 = [7000, 8000, 9000, 10000, 11000]
#Crea un vector (arreglo) con valores en el eje Y para cada valor en el eje X
y2 = [ 80, 83, 85, 86, 88]
#Grafica el vector x1 contra el vector y2
pl.plot(x1, y2)
pl.axis([5000,12000, 60,100])
pl.plot(x1, y2, 'cH')

pl.xlabel('Voltaje [V]')
pl.ylabel('Eficiencia [%]')
#Guarda la grafica en formato png
pl.savefig('temp3.png')
pl.show()

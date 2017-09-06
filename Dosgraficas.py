# http://docs.scipy.org/doc/numpy/reference/generated/numpy.exp.html
import numpy as np
import pylab as pl
# http://matplotlib.org/doc/devdocs/api/_as_gen/matplotlib.pyplot.html
import matplotlib.pyplot as plt
# Declaramos una funcion que nos devuelva f(x) = exp(-x)* cos (2pi*x)
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

# Definimos el rango de dos variables y el intervalo en el que cambian
t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

# Crea el grupo de graficas
plt.figure(1)
# Crea el lienzo con dos renglones, una columna y entra a la primera seccion de esta division.
plt.subplot(211)
# Grafica la variable t1 contra la funcion f(t1) con circulos azules y grafica la variable t2 contra la funcion f(t2) con una linea negra.
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
# Entra a la segunda seccion del lienzo dividido
plt.subplot(212)
# Grafica la variable t2 contra la funcion cos(2pi*x) con una linea punteada roja.
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# Guardar la grafica
plt.savefig('dosfunciones.png')
# muestra la grafica
plt.show()


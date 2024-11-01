# Numerical Python 
# Ocupa menos memoria a las listas de python 
import numpy as np 

a = np.array([1,2,3]) 
print("1D array ")
print(a)
print()

b = np.array([(1,2,3),(4,5,6)])
print("2D array:")
print(b)

# np.array() usar la funcion np.array() y se le agrega una lista y si quieres el tipo de dato

# matrices de unos
print()
unos = np.ones((3,4))
print(unos)

# matrices de ceros
print()
ceros = np.zeros((3,4))
print(ceros)

# matriz aleatoria 
print()
aleatorios = np.random.random((2,2))
print(aleatorios)

# matriz vacia 
print()
vacia = np.empty((3,2))
print(vacia)

# matriz valor unico 
print()
full = np.full((2,2),7)
print(full)

# matriz con valores espaciados uniformes 
print()
espacio1 = np.arange(0,30,5) 
print(espacio1)

print()
espacio2 = np.linspace(0,2,5) # matriz con 5 valores entre 0 y 2 
print(espacio2)



# matriz identidad 
print()
identidad1 = np.eye(4,4)
print(identidad1)

print()
identidad2 = np.identity(4)
print(identidad2)


print()
print("____________________Solicitud en matrices______________________")
print()


# dimenciones de la matriz 
print()
print(b.ndim)
print()

# tipo de datos de los elementos de una matriz 
print()
print(b.dtype)
print()

# tamaño y forma de la matriz 
print()
print(b.size)
print(b.shape)
print()

# cambio de forma a una matriz ejm 2x3 a 3x2 
print()
b = b.reshape(3,2)
print(b)

# extraer un elemento de la matriz 
print()
print(b[0,1])
print()

# todos los valores de las filas hubicasdos en la columna deseada 
print()
print(b[0:,1])


print()
print("____________________Operacion en matrices______________________")
print()

# valor minimo, maximo y la suma 
c = np.array([2,4,8])
print(c.min())
print(c.max())
print(c.sum())
print()

# raiz cuadrada y desviacion estandar 
d = np.array([(2,4,8),(3,6,9)])
print(np.sqrt(d))
print(np.std(d))
print()

# suma resta multiplicacion y divicion 
e = np.array([(1,2,3),(4,5,6)])
print(d+e)
print(d-e)
print(d*e)
print(d/e)
import numpy as np
a=np.empty((4,8))#Lo anterior crea un arreglo de tamaño 4x8 una matriz 4x8, notar que el parametro "(f,c)", es todo un size completo
print(a)
a=np.zeros((4,8))#Lo mismo pero todos los elementos de la matriz son cero
print("Generando arreglo con zeros\n",
      a)
a=np.ones((4,8))#Lo mismo pero todos los elementos de la matriz son 1
print("Generando arreglo con metodo ones\n",a)
a=np.full((4,8),11)#Lo mismo pero todos los elementos de la matriz son el segundo parametro, en este caso "11", donde el primer parametro es un size
print("Generando arreglo con metodo full\n",a)
a=np.random.rand(4,8)#Lo mismo pero todos los elementos de la matriz son numeros aleatorios
print("Generando arreglo con metodo random.rand\n",a)
a=np.random.randint(5,25,40)
"""
Este metodo requiere tres parametros, el primero un entero minimo, el segundo un entero máximo y el tercero denota el tamaño del array, en principio se genera un array 
unidimensional con numeros en el intervalo (5,25), todos enteros hasta completar 40 elementos
"""
print("Generando arreglo con metodo random.randint\n",a)
b=np.reshape(a,(8,5))
"""
Este metodo resulta util para tomar un array de una dimensión y transformarlo en uno de 2, el primer parametro es un array y el segundo es la nueva forma, en 
este caso la forma es un arreglo rectangular de tamaño 40, el mismo tamño que el arreglo anterior, el acomodo es fila tras fila
"""
print("Hemos reformado nuestro arreglo, a una matriz de 40 entradas\n",b)
l=[1,2,3,4,5]
a=np.array(l)#Este metodo es simple, crea un array a partir de una lista
print("Transformamos una lista a un array\n",a)
l=[[1,2,3,4,5],[1,2,3,4,5]] #Una lista de listas
a=np.array(l) #Tambien se pueden transformar listas de listas en arrays
"""
El método tambien funciona con listas de listas, agrupando una tras otra (fila tras fila)
"""
print("Array resultado de listas de listas",a)
a=np.linspace(3,9,3)
"""
El primer parametro es un número menor, el segundo es uno mayor y el tercero establece el tamaño del arreglo, entonces se toman numeros dividiendoi ntervalo 
(3,9) de manera proporcional hasta completar 3 lugares
"""
print("Array creado de manera aleatoria mediante un rango, este es de una sola dimensión\n",a)
"""
A continuación se emplean los metodos shape y ndim, el primero nos da la forma del array, dando la lengh para cada axix(el tamaño del matriz), mientras que 
ndim nos da el numero de axis(dimensión del array), es posible determinar el tamaño del arreglo mediante su metodo size
"""
print("La forma del arreglo ''b'' es: ",b.shape)
print("La dimensión del arreglo, ''a'' es: ",a.ndim)
print("El tamaño del arreglo ''b'' es: ",b.size)
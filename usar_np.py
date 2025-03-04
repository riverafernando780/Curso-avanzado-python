import numpy as np
a=np.empty((4,8))#Lo anterior crea un arreglo de tamaño 4x8 una matriz 8x4, notar que el parametro "(c,f)", es todo un size completo
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
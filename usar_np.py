import numpy as np
a=np.empty((4,8))
print(a)
print("Generando arreglo con zeros\n",
      a)
a=np.zeros((4,8))
print("Generando arreglo con metodo ones\n",a)
a=np.ones((4,8))
print("Generando arreglo con metodo full\n",a)
a=np.full((4,8),11)
print("Generando arreglo con metodo random.rand\n",a)
a=np.random.rand(4,8)
print("Generando arreglo con metodo random.randint\n",a)
a=np.random.randint(5,25,40)
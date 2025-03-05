import numpy as np

print("Este programa permite operar con matrices de tamaño nxn")
def creaMatriz():
    n=int(input("Ingrese el tamaño ''n'' de la matriz: "))
    print(f"Se va crear una matriz de tamaño {n}x{n}")
    colector=[]
    for i in range(1,n+1):
        for j in range(1,n+1):
            colector.append(float(input(f"Ingrese el elemento: ({i},{j}): ")))
    matriz=np.array(colector)
    matriz=np.reshape(matriz,(n,n))
    return matriz

a=creaMatriz()
print(a)

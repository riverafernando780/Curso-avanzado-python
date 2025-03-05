print("Este programa permite operar con matrices de tamaño nxn")
n=int(input("Ingrese el tamaño ''n'' de la matriz: "))
colector=[]
for i in range(1,n+1):
    for j in range(1,n+1):
        colector.append(float(input("Ingrese el elemento: (",i,",",j,")")))
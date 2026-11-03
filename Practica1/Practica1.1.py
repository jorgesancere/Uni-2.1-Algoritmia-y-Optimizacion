import numpy as np
import time
x = np.random.randint(0,100,size=10)
print(x)
#Algoritmo de ordenacion 1
def ordenacion_uno(arr):
    n = len(arr)
    for i in range (n-1):
        for j in range (n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

inicio = time.perf_counter()
resultado = ordenacion_uno(x)
fin = time.perf_counter()

print (" Resultado :" , resultado)
print (" Tiempo transcurrido :" , fin - inicio , " segundos ")
    
  
#Algoritmo de ordenacion 2
def ordenacion_dos(arr):
    if len(arr) <=1:
        return arr
    pivote = arr[0]
    izq = []
    der = []
    for i in range(1, len(arr)):
        if arr[i] <= pivote:
            izq.append(arr[i])
        else:
            der.append(arr[i])
    return ordenacion_dos(izq) + [pivote] + ordenacion_dos(der)

y = np.random.randint(0,100,size=10)
print(y)
inicio = time . perf_counter ()
resultado = ordenacion_dos(y)
fin = time . perf_counter ()
print (" Resultado :" , resultado )
print (" Tiempo transcurrido :" , fin - inicio , " segundos ") 
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# ordenacion_dos()

import numpy as np
import matplotlib.pyplot as plt
import time

def g(n):
    if n == 1:
        return
    
    g(n-1)
    g(n-1)
    
x =np.linspace(1,10,9)
y = []
for xi in x:
    start = time.time()
    for i in range(5):
        g(int(xi))
    end = time.time()
    y.append((end-start)/5)
    
y2 = 2**x
scale = y2[-1]/y[-1]
print(scale)

plt.plot(x, np.array(y)*scale, label = "empirico")
plt.plot(x, y2, label = "teorico")

plt.legend()
plt.xlabel("n")
plt.ylabel("timepo(s)")
plt.show()



    
def ordenacion_dos(arr):
    if len(arr) <= 1:
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
    
x =np.linspace(0,10,9)
y = []
for xi in x:
    start = time.time()
    for i in range(5):
        ordenacion_dos(x)
    end = time.time()
    y.append((end-start)/5)
    
y2 = x**2 #Teorico
scale = y2[-1]/y[-1]
print(scale)

plt.plot(x, np.array(y)*scale, label = "empirico")
plt.plot(x, y2, label = "teorico")

plt.legend()
plt.xlabel("n")
plt.ylabel("tiempo(s)")
plt.show()
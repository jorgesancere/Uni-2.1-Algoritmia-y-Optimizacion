#Practica 2.1 Algoritmia
import numpy as np
import matplotlib.pyplot as plt
import time
import math
import random
#Definimos los subejercicios del ejercicio 1
def jnim(n, m):
  if n == 0:
    return False  # Caso base: sin fichas, el jugador en turno pierde

  for i in range(1, min(n, m) + 1):
    # Si existe una jugada que deje al rival en posición perdedora:
    if not jnim(n - i, m):
      return True  # Encontramos un movimiento ganador

  # Si ninguna jugada nos asegura ganar, la posición es perdedora
  return False

def quick(v):
    if len(v) <= 1:
        return v
    else:
        pivote = random.choice(v)
        izquierda = []
        derecha = []
        centro = []

        for i in v:
            if i < pivote:
                izquierda.append(i)
            elif i > pivote:
                derecha.append(i)
            else:
                centro.append(i)

        return (quick(izquierda) + centro + quick(derecha))


    
def mezclar(vi, vd):
  i = d = 0  # Corregido: asignación múltiple correcta
  resultado = []

  # Comparamos y añadimos el menor
  while i < len(vi) and d < len(vd):
    if vi[i] <= vd[d]:
      resultado.append(vi[i])  # Corregido: .append() en lugar de +=
      i += 1
    else:
      resultado.append(vd[d])  # Corregido: .append() en lugar de +=
      d += 1

  # FUERA DEL WHILE: Añadimos los elementos sobrantes de cualquiera de las dos listas
  resultado += vi[i:]
  resultado += vd[d:]

  return resultado  # FUERA DEL WHILE: Retornamos la lista combinada


def merge(v):
  if len(v) <= 1:
    return v

  mitad = len(v) // 2  # Corregido: división entera con //

  v_i = merge(v[:mitad])
  v_d = merge(v[mitad:])

  return mezclar(v_i, v_d)
def inv():
    return None


#Definimos los subejercicios del ejercicio 2
def director_deportivo():
    return None
def gira_conciertos():
    return None
def viaje_marte():
    return None
def reforestacion():
    return None
def salvar_princesa():
    return None


#Deinimos el main
def main():

    print("Bienvenido a la pratica 2.1")
    ej = int(input("Elije ejercicio (1/2):"))
    if ej == 1:
        ej1 = int(input("Elije subejercicio (1/2/3/4): "))
        print("1: Juego del Nim")
        print("2: QuickSort")
        print("3: MergeSort")
        print("4: Contar Inversiones")

        if ej1 == 1:

            n = int(input("Define el numero de fichas en la mesa: "))
            m = int(input("Define el numero de fichas que se pueden robar por turno: "))

            print(jnim(n, m))

        elif ej1 == 2:
            v = []
            for i in range(random.randint(5, 15)):
                v.append(random.randint(0,100))
            print(v)
            print(quick(v))

        elif ej1 == 3:
            v = []
            for i in range(random.randint(5, 15)):
                v.append(random.randint(0,100))
            print(v)
            print(merge(v))
        elif ej1 == 4:
            inv()
        else:
            print("Error")
    if ej == 2:
        ej2 = int(input("Elije subejercicio (1/2/3/4/5)"))
        print("1: Director Deportivo")
        print("2: Gira de conciertos")
        print("3: Viaje a Marte")
        print("4: Reforestacion")
        print("5: Salvar a la princesa")
        if ej2 == 1:
            director_deportivo()
        if ej2 == 2:
            gira_conciertos()
        if ej2 == 3:
            viaje_marte()
        if ej2 == 4:
            reforestacion()
        if ej2 == 5:
            salvar_princesa()
        else:
            print("Error")

main()
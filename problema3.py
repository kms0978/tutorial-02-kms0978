#Problema 2  / 7 ptos x4 pruebas / 28 puntos
#Ingreso de valores en árbol TRI-nario
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios números y cree un árbol trinario con listas
# esto es igual que el binario, pero los elementos que son iguales van en una lista
# centro, de la forma [numero, [subarbol IZQ], [mismo NUM], [subarbol DER] ]
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 30 90 90 8 5 90
#La salida debe ser
#         [20, [8, [5, [], [], []], [], []], [], [30, [], [], [90, [], [90, [], [90, [], [], []], []], []]]]


def insertar_arbol(arbol, numero):
    if not arbol:
        return [numero, [], [], []]
    elif numero == arbol[0]:
        if isinstance(arbol[2], list) and not arbol[2]: 
            arbol[2] = [numero, [], [], []]
        elif numero not in arbol[2]:
            arbol[2] = insertar_arbol(arbol[2], numero)
    elif numero < arbol[0]:
        arbol[1] = insertar_arbol(arbol[1], numero)
    else:
        arbol[3] = insertar_arbol(arbol[3], numero)
    return arbol

def imprimir_arbol(arbol):
    if not arbol:
        return
    if isinstance(arbol, int):
        print(arbol, end=" ")
        return
    print("[", arbol[0], end=" ")
    for i in range(len(arbol)):
      if arbol[i]:
          imprimir_arbol(arbol[i])
      else:
          print("[]", end=" ")
    print("]", end="")

t = input().split()
arbol = None
for numero in t:
    arbol = insertar_arbol(arbol, int(numero))

imprimir_arbol(arbol)

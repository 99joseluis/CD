"""
Programa que simula el recorrido bfs en un arbol


@author1 García Santamaría José Luis 316174646
@author2 Reyes Martínez Antonio 316184931

@date 5 de octubre de 2020
"""



def bfs(arbol, raiz):
    """
        Funcion para obtener el recorrido bfs de un arbol representado como un diccionario 
    
        @param arbol -> diccionario que representa el arbol
        @param raiz  -> nodo distinguido que representara la raiz del arbol
        @return lista de los nodos del arbol con formato bfs
    """
    visitados = []
    visitados.append(raiz)
    for n in range(0, len(arbol)):
        hijos = []
        for i in arbol[visitados[n]]:
            if i not in visitados:
                visitados.append(i)
            hijos.append(i)
    return visitados

#Ingresa el arbol en forma de un diccionario de python
#Ejemplo: {'A'=['B','C','D'], 'B'=['E','F'], 'C'=['G','H'], 'D'=['I','J'] }
#donde 'A' simula ser un nodo y la lista ['B','C','D'] son sus nodos hijos 
arbol = dict(A=['B','C','D'], B=['E','F'], C=['G','H'], D=['I','J'])

# Ingresar que nodo se tomará como la raiz del arbol
raiz = 'A'

print("Arbol -> ",arbol)
print("Recorrido bfs -> ",bfs(arbol , raiz))

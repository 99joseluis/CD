import simpy
from Nodo import Nodo 
from Canales.Canal import Canal

env = simpy.Environment()
canal = Canal(env)

grafica = []
vecindades = [[1,2], [0,2,7], [0,1,3,7], [2,4,6], [2,3,5], [4], [3,7], [1,2,6]]
for i in range(0, len(vecindades)):
    grafica.append(Nodo(i , vecindades[i], canal.crea_canal_de_entrada(), canal))
    print("El nodo %d tiene "%(grafica[i].id_nodo))
    print(*grafica[i].vecinos, sep=" , ")

for i in grafica:
    env.process(i.algo1())

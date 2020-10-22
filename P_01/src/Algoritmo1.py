import simpy
from Nodo import * 
from Canales.Canal1 import * 

class Algoritmo1(Nodo):
    def __init__(self, id_nodo, vecinos, canal_entrada,
                canal_salida):
        '''Inicializa los atributos del nodo.'''
        self.id_nodo = id_nodo
        self.vecinos = vecinos
        self.canal_entrada = canal_entrada
        self.canal_salida  = canal_salida
        self.conocidos = []
        self.seen_msg = False

    def eliminaRep(self, conocidos):
        '''Elimina los las sublistas repetidas en self.conocidos'''
        nuevalista = []
        for i in conocidos:
            if i not in nuevalista:
                nuevalista.append(i)
        self.conocidos = nuevalista
    
    def algo1(self,nodo, envi):
        '''Implementa el algoritmo 1'''
        for j in self.vecinos:
            self.canal_salida.envia(self.vecinos)
            yield envi.timeout(1)
        
        while True:
            msj = yield self.canal_entrada.get()
            self.seen_msg = True
            print('%d recibío el mensaje %s en el %d' %(self.id_nodo, msj, envi.now))
            yield envi.timeout(1)
            self.conocidos.append(msj)
            self.eliminaRep(self.conocidos)
    


if __name__ == "__main__":
     # Inicializamos ambiente y canal
    envi = simpy.Environment()
    envi_algo = Canal1(envi)

    # Creamos los nodos
    grafica = []
    adyacencias = [[1, 2], [0, 2, 7], [0, 1, 3, 7], [2, 4, 6], [4], [3, 7], [1, 2, 6]]

    #Creamos la grafica
    for i in range(0, len(adyacencias)):
        grafica.append(Algoritmo1(i, adyacencias[i], envi_algo.crea_canal_de_entrada(), envi_algo))
    
    for j in range(0, len(adyacencias)):
        envi.process(grafica[j].algo1(j,envi))
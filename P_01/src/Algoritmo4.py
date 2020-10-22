import simpy
from Nodo import * 
from Canales.Canal4 import * 

class Algoritmo4(Nodo):
    def __init__(self, id_nodo, vecinos, canal_entrada, canal_salida):
        '''Inicializa los atributos del nodo.'''
        self.id_nodo = id_nodo
        self.vecinos = vecinos
        self.canal_entrada = canal_entrada
        self.canal_salida = canal_salida
        self.expected_msg = 0
        self.padre = 0
        self.hijos = []
        
    def quitavecino(self, l, id):
        lista = []
        for i in l:
            if i != id:
                lista.append(i)
        return lista

    def algo4(self, envi):
        if self.id_nodo == 0 : #Checo que sea la raiz
            yield envi.timeout(1)
            self.padre = self.id_nodo
            self.expected_msg = len(self.vecinos)
            self.canal_salida.envia(["GO", self.id_nodo], self.vecinos)   
        else:
            self.padre = -1  #Si no soy la raiz solo inicializo mis variables
        self.hijos = []

        while True:
            msj = yield self.canal_entrada.get()
            print(msj)
            if (msj[0] == 'GO'):
                self.seen_msg = True
                if (self.padre == -1):
                    self.padre = msj[1]
                    # print("Le asigna a %d el padre %d" %(self.id_nodo, msj[1]))
                    self.expected_msg = (len(self.vecinos) - 1)
                    if self.expected_msg == 0:
                        self.canal_salida.envia(["BACK", self.id_nodo],[msj[1]])
                    else:
                        self.canal_salida.envia(["GO", self.id_nodo], self.quitavecino(self.vecinos, msj[1]))
                else:
                    self.canal_salida.envia(["BACK", 0], [msj[1]])
                
            if (msj[0] == 'BACK'):
                self.expected_msg = self.expected_msg - 1

                if (msj[1] != 0):
                    self.hijos.append(msj[1])
                if self.expected_msg == 0 :
                    if self.padre != self.id_nodo:
                        self.canal_salida.envia(["BACK", self.id_nodo], [self.padre])



if __name__ == "__main__":
    # Inicializamos ambiente y canal
    envi = simpy.Environment()
    envi_algo = Canal4(envi)

    # Creamos los nodos
    grafica = []
    #                0          1           2           3       4     5       6          7
    adyacencias = [[1, 2], [0, 2, 7], [0, 1, 3, 7], [2, 4, 6], [4,5], [3, 7], [1, 2, 6], [7]]

    for i in range(0, len(adyacencias)):
        grafica.append(Algoritmo4(i, adyacencias[i], envi_algo.crea_canal_de_entrada(), envi_algo))


    #envi.process(grafica[0].algo4(0, envi))
    for i in range(0, len(adyacencias)):
        envi.process(grafica[i].algo4(envi))
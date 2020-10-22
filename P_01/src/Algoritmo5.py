import simpy
from Nodo import * 
from Canales.Canal4 import * 

class Algoritmo5(Nodo):
    
    def __init__(self, id_nodo, hijos, canal_entrada, canal_salida):
        '''Inicializa los atributos del nodo.'''
        self.id_nodo = id_nodo
        self.hijos = hijos
        self.canal_entrada = canal_entrada
        self.canal_salida = canal_salida
        self.data = 0

    def algo5(self, mensaje, envi):
        if self.id_nodo == 0: #Checamos si es la raiz
            yield envi.timeout(1)
            self.data = mensaje
            self.canal_salida.envia(self.data, self.hijos)
        else:
            self.data = 0

        while True:
            msj = yield self.canal_entrada.get()
            yield envi.timeout(1)
            #print("LLega el mensaje %s al nodo %d en el tiempo %s" %(msj, self.id_nodo, envi.now))
            self.canal_salida.envia(msj, self.hijos)


if __name__ == "__main__":
    # Inicializamos ambiente y canal
    envi = simpy.Environment()
    envi_algo = Canal4(envi)

    #Leemos el mensaje 
    mensaje = input("Ingresa el mensaje a diseminar ")

    # Creamos los nodos
    grafica = []
    #                0       1      2     3    4    5  6   7    8
    adyacencias = [[1, 2], [3,4], [5,6], [7], [8], [], [], [], []]

    #Creamos la gráfica 
    for i in range(0, len(adyacencias)):
        grafica.append(Algoritmo5(i, adyacencias[i], envi_algo.crea_canal_de_entrada(), envi_algo))

    #Inicializamos el algoritmo para cada nodo
    for i in range(0, len(adyacencias)):
        envi.process(grafica[i].algo5(mensaje, envi))


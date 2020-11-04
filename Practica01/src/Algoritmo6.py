import simpy
from Nodo import * 
from Canales.Canal6 import * 

class Algoritmo6(Nodo):
    
    def __init__(self, id_nodo, hijos, padre, canal_entrada, canal_salida):
        '''Inicializa los atributos del nodo.'''
        self.id_nodo = id_nodo
        self.hijos = hijos
        self.padre = padre
        self.canal_entrada = canal_entrada
        self.canal_salida = canal_salida
        self.val_set = []
        self.valor_env = 0
    
    def algo6(self, v, envi):
        if (len(self.hijos) == 0):  #Revisamos que sea una hoja
            print("Es hoja el nodo %d y envia %s a su padre %d" %(self.id_nodo, v, self.padre))
            self.valor_env = v
            self.canal_salida.envia([self.id_nodo, v], self.padre)

        while True:
            msj = yield self.canal_entrada.get()
            yield envi.timeout(1)
            print("El nodo %d leyo el mensaje %s en el tiempo %d" %(self.id_nodo, msj, envi.now))
            self.val_set.append(msj)
            if (self.padre != self.id_nodo):
                self.canal_salida.envia(self.val_set, self.padre)
            else:
                print("Llego hasta la raiz y el val_set termino como :")
                print(self.val_set)



if __name__ == "__main__":
    # Inicializamos ambiente y canal
    envi = simpy.Environment()
    envi_algo = Canal6(envi)

    #Leemos el mensaje 
    mensaje = input("Ingresa el mensaje a diseminar ")

    # Creamos los nodos
    grafica = []
    #          0       1      2     3    4    5  6   7    8
    hijos = [[1, 2], [3,4], [5,6], [7], [8], [], [], [], []]
    padres =[0,    0,    0, 1, 2, 1, 1, 2, 2]
       
    #Creamos la gráfica 
    for i in range(0, len(hijos)):
        grafica.append(Algoritmo6(i, hijos[i], padres[i], envi_algo.crea_canal_de_entrada(), envi_algo))

    #Inicializamos el algoritmo para cada nodo
    for i in range(0, len(hijos)):
        envi.process(grafica[i].algo6(mensaje, envi))
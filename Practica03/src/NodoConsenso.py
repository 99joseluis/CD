import simpy
from Nodo import *
from Canales.CanalRecorridos import *

# La unidad de tiempo
TICK = 1

class NodoConsenso(Nodo):
    ''' Implementa la interfaz de Nodo para el algoritmo de Consenso.'''

    def __init__(self, id_nodo, vecinos, canal_entrada, canal_salida):
        ''' Constructor de nodo que implemente el algoritmo de consenso. '''
        self.id_nodo = id_nodo
        self.vecinos = vecinos
        self.canal_entrada = canal_entrada
        self.canal_salida = canal_salida
        # Atributos extra
        self.V = [None] * (len(vecinos) + 1) # Llenamos la lista de Nones
        self.V[id_nodo] = {id_nodo}
        self.New = set([id_nodo])
        self.rec_from = [None] * (len(vecinos) + 1)
        self.fallare = False      # Colocaremos esta en True si el nodo fallará
        self.lider = None         # La elección del lider.

    def consenso(self, env, f):
        '''El algoritmo de consenso.
        recibe un environment y un numero f de procesos que fallarán
        '''
        #Condición para saber si el nodo va a fallar
        self.fallare = (self.id_nodo < f)
        #Se efectuan f+1 rondas desde la ronda 0
        while (env.now < f +1):
            #Checamos si los nodos fallaron o no
            if (not self.fallare):
                #Revisamos que la variable New_i sea distinta de vacia para enviar nuestros datos a los vecinos
                if(self.New != set()):
                    self.canal_salida.envia((self.New,self.id_nodo),self.vecinos)
                yield env.timeout(TICK)
                #recibimos los datos de un vecino de la forma (v,k)
                msg = yield self.canal_entrada.get()
                #Obtenemos la variable rec_from
                self.rec_from = msg
                self.New = set ()
                #Actualizamos la posicion V[k] con los datos del vecino k
                if (self.rec_from[1] != self.id_nodo):
                    if self.V[self.rec_from[1]] is None: 
                        self.V[self.rec_from[1]] = set(self.rec_from[0])
                        self.New = self.New.union(set(self.rec_from[0])) 
            else:
                break
        # Seleccionamos al lider del nodo
        for i in self.V:
            if i is not None:
                self.lider = i
                break
            

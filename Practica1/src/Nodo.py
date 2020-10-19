import simpy
from Canales.Canal import Canal
class Nodo:
    """Representa un nodo.

    Cada nodo tiene un id, una lista de vecinos y dos canales de comunicación.
    Los métodos que tiene son únicamente getters.
    """
    def __init__(self, id_nodo: int, vecinos: list, canal_entrada: simpy.Store,
                 canal_salida: simpy.Store):
        '''Inicializa los atributos del nodo.'''
        print("se inicializa el nodo")
        self.id_nodo = id_nodo
        self.vecinos = vecinos
        self.canal_entrada = canal_entrada
        self.canal_salida = canal_salida
        self.mensaje = False


    def algo1(self):
        print("Entra el proceso algo1")
        if self.id_nodo == 0:
            #Solo la raiz envia el primer mensaje 
            print("Enviando el primer mensaje (raiz)")
            self.mensaje = True
            self.canal_salida.envia(self.id_nodo, self.vecinos)
        else:
            while true:
                if self.mensaje is not True:
                    msj = yield self.canal_entrada.get()
                    print("Mensaje get = ")
                    print(msj)
                    self.mensaje = msj

                    #print("%d recibío el mensaje de %d " %(self.id_nodo, msj))
                    # lo reenviamos a los vecinos
                    self.canal_salida.envia(self.id_nodo, self.vecinos)
                    print("Canal de entrada : ")
                    print(self.canal_entrada.canales)
                    print("Canal de salida :")
                    print(self.canal_salida.canales)
                    break



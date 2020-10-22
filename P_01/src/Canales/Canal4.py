import simpy
from Canales.Canal import Canal


class Canal4(Canal):
    '''
    clase que implementa la interfaz que modela el comportamiento que cualquier canal debe tomar.
    '''
    def __init__(self, env, capacidad=simpy.core.Infinity):
        self.env = env
        self.capacidad = capacidad
        self.canales = []
        self.canal_de_salida = None

    def envia(self, mensaje, vecinos):
        '''
        Envia un mensaje a los canales de salida de los vecinos.
        '''
        if not self.canales:
            raise RuntimeError('No hay canales de salida.')
        eventos = list()
        for i in range(len(self.canales)):
            if i in vecinos:
                eventos.append(self.canales[i].put(mensaje))
        return self.env.all_of(eventos)

    def crea_canal_de_entrada(self):
        '''
        Creamos un objeto Store en el cual recibiremos los mensajes.
        '''
        canal = simpy.Store(self.env, capacity=self.capacidad)
        self.canales.append(canal)
        self.canal_de_salida = canal
        return canal

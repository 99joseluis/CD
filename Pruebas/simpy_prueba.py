import simpy

class Carro(object):
	def __init__(self, id_Carro, env, estacion_carga):
		self.env = env
		self.id_carro = id_Carro
		self.accion = env.process(self.run())
		self.estacion_carga = estacion_carga
		self.accion = env.process(self.run())
	def run(self):
		while True:
			# Estacionada y carga
			print("%d llegó a la estacion en el  %d" % (self.id_carro, self.env.now))
			with estacion_carga.request() as req:
				yield req
			print("%d empezo a cargar en el %d"% (self.id_carro, self.env.now))
			duracion_carga = 5
			yield self.charge(duracion_carga)
			
			# Conduccion
			print("Empieza a conducir en el %d" % self.env.now)
			duracion_viaje = 4
			yield self.env.timeout(duracion_viaje)

	def charge(self, duracion):
		yield self.env.timeout(duracion)
# Main
env = simpy.Environment()
estacion_carga = simpy.Resource(env, capacity=1)
carros = []
for i in range(4):
	carros.append(Carro(i, env, estacion_carga))


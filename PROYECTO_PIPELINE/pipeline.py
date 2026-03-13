from typing import List

class Pipeline:
    def __init__(self, modelo, metricas):
        self.modelo = modelo   
        self.metricas = metricas  
        self.transformaciones = [] 
    def agregar_transformacion(self, transformacion):
        self.transformaciones.append(transformacion)

    def ejecutar(self):
        pass
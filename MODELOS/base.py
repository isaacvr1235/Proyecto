from abc import ABC, abstractmethod

class Modelo(ABC):
    @abstractmethod
    def entrenar(self, datos):
        pass

class ModeloSupervisado(Modelo, ABC):
    passKN

class ModeloNoSupervisado(Modelo, ABC):
    pass
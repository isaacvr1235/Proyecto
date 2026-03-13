from abc import ABC, abstractmethod

class Transformacion(ABC):
    @abstractmethod
    def aplicar(self, datos):
        pass

class Scaler(Transformacion):
    def aplicar(self, datos):
        pass

class LimpiadorNulos(Transformacion):
    def aplicar(self, datos):
        pass
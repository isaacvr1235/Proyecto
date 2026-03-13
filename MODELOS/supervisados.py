from .base import ModeloSupervisado

class Clasificacion(ModeloSupervisado): 
    pass

class Regresion(ModeloSupervisado):
    pass

class DecisionTree(Clasificacion):
    pass

class LogisticRegression(Clasificacion):
    pass

class ModeloRegresionLineal(Regresion):
    pass
from abc import ABC, abstractmethod

class Pokemon(ABC):
    def __init__(self, nombre, vida_maxima, energia_maxima):
        self.nombre = nombre
        self._vida_maxima = vida_maxima
        self._energia_maxima = energia_maxima
        self._vida_actua = vida_maxima
        
    
    @property
    def vida_actual(self):
        return self._vida_actual
        
        
    @abstractmethod
    def atacar(self):
        pass
    @abstractmethod   
    def defensa(self):
        pass
    @abstractmethod
    def descanso(self):
        pass    
    
    
    
        

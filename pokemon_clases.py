from abc import ABC, abstractmethod
from pokedex import CATALOGO_POKEMON


class Pokemon(ABC):
    def __init__(self, nombre, hp_maximo, energia_maxima):
        self.nombre = nombre
        
        self._hp_maximo = hp_maximo
        self._hp_actual = self.hp_maximo
        
        self._energia_maxima = energia_maxima
        self._energia_actual = energia_maxima
        
        self.defendiendo = False
        self.paralizado = False
        
        
    @property
    def hp_actual(self):
        return self._hp_actual
    
    
    
    @property
    def hp_maximo(self):
        return self._hp_maximo
    
    
    @property
    def energia_actual(self):
        return self._energia_actual
    
    @property
    def energia_maxima(self):
        return self._energia_maxima
    
    
    @hp_actual.setter
    def hp_actual(self, valor):
        if valor < 0:
            self._hp_actual = 0
        elif valor > self._hp_maximo:
            self._hp_actual = self._hp_maximo
        else:
            self._hp_actual = valor 
        
    @energia_actual.setter
    def energia_actual(self, valor):
        if valor < 0:
            self._energia_actual = 0
        elif valor > self._energia_maxima:
            self._energia_actual = self._energia_maxima
        else:
            self._energia_actual = valor 
        
    @abstractmethod
    def atacar(self, oponente):
        pass
    
    @abstractmethod   
    def defensa(self):
        pass
    
    @abstractmethod
    def descanso(self):
        pass  
    
    
    
    
        

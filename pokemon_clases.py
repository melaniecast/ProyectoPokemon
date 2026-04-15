from abc import ABC, abstractmethod

class Pokemon:
    def __init__(self, nombre, __vida_maxima, __energia_maxima):
        self.nombre = nombre
        self.__vida_maxima = vida_maxima
        

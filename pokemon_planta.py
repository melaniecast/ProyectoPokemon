from pokemon_clases import Pokemon

class PokemonPlanta(Pokemon):
    def __init__(self, nombre, vida_maxima, energia_maxima):
        super().__init__(nombre, vida_maxima, energia_maxima)
        
        
    def atacar(self):
        return super().atacar()
    
    def defensa(self):
        return super().defensa()
    
    def descanso(self):
        return super().descanso()
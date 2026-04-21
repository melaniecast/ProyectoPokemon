from pokemon_clases import Pokemon
from pokedex import CATALOGO_POKEMON


class PokemonAgua(Pokemon):
    def __init__(self, nombre, vida_maxima, energia_maxima):
        super().__init__(nombre, vida_maxima, energia_maxima)
    
    
    def cambio_energia(self):
        if self.energia_actual < 0:
            self.energia_actual = 0
        elif self.energia_actual > self.energia_maxima:
            self.energia_actual = self.energia_maxima
            
    
    def atacar(self, oponente):
        self.energia_actual -= 15
        self.cambio_energia()
        return f"{self.nombre} uso chorro de Agua!"
    
    def defensa(self):
        self.energia_actual -= 5
        self.cambio_energia()
        return f"{self.nombre} se escondio en su caparazon"
    
    def descanso(self):
        self.energia_actual += 20
        self.cambio_energia()
        return f"{self.nombre} esta recuperando energia - sacrifica un turno"
    
    
    
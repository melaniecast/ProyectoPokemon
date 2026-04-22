from pokedex import CATALOGO_POKEMON
from pokedex import mostrar_catalogo_disponible
from pokemon_clases import Pokemon
from pokemon_agua import PokemonAgua
from pokemon_fuego import PokemonFuego
from pokemon_planta import PokemonPlanta

class PokemonElectrico(Pokemon):
    def __init__(self, nombre, vida_maxima, energia_maxima):
        super().__init__(nombre, vida_maxima, energia_maxima)
        self.paralizado = False
        
        
    def cambio_energia(self):
        if self.energia_actual < 0:
            self.energia_actual = 0
        elif self.energia_actual > self.energia_maxima:
            self.energia_actual = self.energia_maxima 
        
    def atacar(self, oponente):
        self.energia_actual -= 15
        self.cambio_energia()
        
        daño = 15
        oponente.hp_actual -= daño
        
        import random
        if random.random() <= 0.20:
            oponente.paralizado = True
        return f"{self.nombre} lanza rayo!"
    
    
    def defensa(self):
        self.energia_actual -= 5
        self.cambio_energia()
        return f"{self.nombre} utiliza estatica!"
    
    def descanso(self):
        self.energia_actual += 20
        self.cambio_energia()
        return f"{self.nombre} esta recuperando energia - sacrifica un turno"
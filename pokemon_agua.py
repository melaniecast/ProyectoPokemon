from pokedex import CATALOGO_POKEMON
from pokedex import mostrar_catalogo_disponible
from pokemon_clases import Pokemon
from pokemon_electrico import PokemonElectrico
from pokemon_fuego import PokemonFuego
from pokemon_planta import PokemonPlanta


class PokemonAgua(Pokemon):
    def __init__(self, nombre, vida_maxima, energia_maxima):
        super().__init__(nombre, vida_maxima, energia_maxima)
    
    
    

            
    
    def atacar(self, oponente):
        self.energia_actual -= 15
        
        
        daño = 15
        if isinstance(oponente,PokemonFuego):
            daño *= 2
        
        if oponente.defendiendo:
            daño //= 2
            oponente.defendiendo = False
        
        oponente.hp_actual -= daño
        
            
        return f"{self.nombre} uso chorro de Agua!"
    
    
    def defensa(self):
        self.energia_actual -= 5
        
        self.defendiendo = True
        return f"{self.nombre} se escondio en su caparazon"
        
    
    
    
    def descanso(self):
        self.energia_actual += 20
        
        return f"{self.nombre} esta recuperando energia - sacrifica un turno"
    
    
    
    
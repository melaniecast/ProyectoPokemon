
from pokemon_clases import Pokemon
from pokemon_planta import PokemonPlanta


class PokemonFuego(Pokemon):
    def __init__(self, nombre, vida_maxima, energia_maxima):
        super().__init__(nombre, vida_maxima, energia_maxima)
        

        
    def atacar(self, oponente):
        self.energia_actual -= 15
        
        
        daño = 15
        if isinstance(oponente,PokemonPlanta):
            daño *= 2
            
        if oponente.defendiendo:
            daño //= 2
            oponente.defendiendo = False
        
        
        oponente.hp_actual -= daño
        return f"{self.nombre} usa lanzallama"
    
    def defensa(self):
        self.energia_actual -= 5
        
        self.defendiendo = True
        return f"{self.nombre} genera pantalla de humo para evadir el ataque"
    
    def descanso(self):
        self.energia_actual += 20
        
        return f"{self.nombre} esta recuperando energia - sacrifica un turno"
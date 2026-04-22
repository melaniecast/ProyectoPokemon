
from pokemon_clases import Pokemon



class PokemonPlanta(Pokemon):
    def __init__(self, nombre, vida_maxima, energia_maxima):
        super().__init__(nombre, vida_maxima, energia_maxima)
        


    def atacar(self, oponente):
        from pokemon_agua import PokemonAgua
        self.energia_actual -= 15
        
        
        daño = 15
        if isinstance(oponente,PokemonAgua):
            daño *= 2
            
        if oponente.defendiendo:
            daño //= 2
            oponente.defendiendo = False
        
        oponente.hp_actual -= daño
        return f"{self.nombre} usa lianas para golpear"
    
    def defensa(self):
        self.energia_actual -= 5
        
        self.defendiendo = True
        return f"{self.nombre} lanza somnifero al oponente"
    
    def descanso(self):
        self.energia_actual += 20
        
        return f"{self.nombre} esta recuperando energia - sacrifica un turno"
    
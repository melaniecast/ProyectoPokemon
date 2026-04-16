from pokemon_clases import Pokemon

class PokemonPlanta(Pokemon):
    def __init__(self, nombre, vida_maxima, energia_maxima):
        super().__init__(nombre, vida_maxima, energia_maxima)
        
        
    def atacar(self):
        return f"{self.nombre} usa lianas para golpear"
    
    def defensa(self):
        return f"{self.nombre} lanza somnifero al oponente"
    
    def descanso(self):
        return f"{self.nombre} esta recuperando energia - sacrifica un turno"
    
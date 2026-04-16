from pokemon_clases import Pokemon

class PokemonElectrico(Pokemon):
    def __init__(self, nombre, vida_maxima, energia_maxima):
        super().__init__(nombre, vida_maxima, energia_maxima)
        
    def atacar(self):
        return f"{self.nombre} lanza rayo!"
    
    def defensa(self):
        return f"{self.nombre} utiliza estatica!"
    
    def descanso(self):
        return f"{self.nombre} esta recuperando energia - sacrifica un turno"
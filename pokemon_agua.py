from pokemon_clases import Pokemon

class PokemonAgua(Pokemon):
    def __init__(self, nombre, vida_maxima, energia_maxima):
        super().__init__(nombre, vida_maxima, energia_maxima)
        
    def atacar(self):
        return f"{self.nombre} uso chorro de Agua!"
    
    def defensa(self):
        return f"{slef.nombre} se escondio en su caparazon"
    
    def descanso(self):
        return f"{self.nombre} esta recuperando energia - sacrifica un turno"
    
    
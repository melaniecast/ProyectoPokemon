from pokemon_clases import Pokemon

class PokemonFuego(Pokemon):
    def __init__(self, nombre, vida_maxima, energia_maxima):
        super().__init__(nombre, vida_maxima, energia_maxima)
        
    def atacar(self):
        return f"{self.nombre} usa lanzallama"
    
    def defensa(self):
        return f"{self.nombre} genera pantalla de humo para evadir el ataque"
    
    def descanso(self):
        return f"{self.nombre} esta recuperando energia - sacrifica un turno"
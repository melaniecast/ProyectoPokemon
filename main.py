# '''proyecto integrador POO'''
from pokedex import CATALOGO_POKEMON
from pokedex import mostrar_catalogo_disponible
from pokemon_clases import Pokemon
from pokemon_agua import PokemonAgua
from pokemon_electrico import PokemonElectrico
from pokemon_fuego import PokemonFuego
from pokemon_planta import PokemonPlanta
# 

def menu_batalla():
    print ('='*50)
    print('     SIMLADOR DE BATALLAS POKÉMON (POO)     ')
    print ('='*50)
    print('Selecciones el Modo de Juego: \n1. Jugador vs Jugador\n2. Jugador vs Computadora')
    opcion = input('> Opción: ')
    if opcion =='1':
        mostrar_catalogo_disponible()
        eleccion_jugador_1 = input('Jugador 1, elija el numero de su Pokémon: ')
        print(f'¡Has seleccionado a {eleccion_jugador_1}')
        eleccion_jugador_2 = input('Jugador 2, elija el numero de su Pokémon: ')
        print(f'¡Has seleccionado a {eleccion_jugador_2}')
        if eleccion_jugador_1 == '1':
            
            
        
        
# 2 metricas absolutas*
# 1. HP(puntos de salud/ health points)
#    vitalidad fisica del pokemon*
#    hp == 0 = pkemon desmayado
#    hp != numeros negativos
# 2. EP(puntos de energia/ Energy points)
#     resistencia(stamina) del pokemon*
#     ataque(fisico/magico) = menos fuerza(cansancio)
#     ataque != si fuerza < EP minima (reserva)



# '''Combate por turnos 1 vs 1''' 
#dos modos de juego*
# 1. Modo jugador vsjugador(PvP)
#    se pide instruccion por teclado*
# 2. Modo jugador vs Computadora (PvE)\
#     usuario = pokemon , 
#     computadora = libreria nativa random(atacar, defender o descansar)

# '''modos''
# if modo == 'ataque' 
#     resta energia (EP) -  es especifica
#     dano =  calcula dano infligido al oponente basandose en la ventaja elemental 
# if modo == 'defensa'
#     resta energia (EP) - es minima
#     defensa == escudo (reduce dano proximo ataque recibido /2)

# if modo == 'descanso'
#     pokemon == no turno 
#     EP restaurada 

# '''Matriz de dano elemental'''
# ecosistema = [Agua, fuego, planta, electrico]

# agua = dano *2 contra fuego
# fuego = dano *2 contra planta
# planta = dano *2 contra agua 
# electrico no dano doble = 20% paralizar = pierde siguiente turno 

# '''archivos '''
# pokemon_clases.py* -  contiene las clases hijas (agua, fuego, planta, electrico)
# heredan de la clase pokemon**
# cada una en unarchivo diferente e importar cada clase* 

# pokedex.py* -diccionario - informacion en crudo 
# se debe importar el catalogo al archivo principal(*main.py*)**

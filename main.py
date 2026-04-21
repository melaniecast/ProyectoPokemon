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
        print('¡COMIENZA LA BATALLA!')
        print(f'{eleccion_jugador_1} ({tipo}) vs {eleccion_jugador_2} ({tipo})')
        
        datos_jugador1 = CATALOGO_POKEMON[eleccion_jugador_1]
        
       
        
        
        if tipo == 'Agua':
            pokemon_jugador1 = PokemonAgua(datos_jugador1['nombre'], datos_jugador1['hp_maximo'], datos_jugador1['energia_maxima'])
        elif tipo == 'Fuego':
            pokemon_jugador1 = PokemonFuego(datos_jugador1['nombre'], datos_jugador1['hp_maximo'], datos_jugador1['energia_maxima'])
        elif tipo == 'Planta':
            pokemon_jugador1 = PokemonPlanta(datos_jugador1['nombre'], datos_jugador1['hp_maximo'], datos_jugador1['energia_maxima'])
        elif tipo == 'Electrico':
            pokemon_jugador1 = PokemonElectrico(datos_jugador1['nombre'], datos_jugador1['hp_maximo'], datos_jugador1['energia_maxima'])
            
        
        
        datos_jugador2 = CATALOGO_POKEMON[eleccion_jugador_2]
        
        if tipo == 'Agua':
            pokemon_jugador2 = PokemonAgua(datos_jugador2['nombre'], datos_jugador2['hp_maximo'], datos_jugador2['energia_maxima'])
        elif tipo == 'Fuego':
            pokemon_jugador2 = PokemonFuego(datos_jugador2['nombre'], datos_jugador2['hp_maximo'], datos_jugador2['energia_maxima'])
        elif tipo == 'Planta':
            pokemon_jugador2 = PokemonPlanta(datos_jugador2['nombre'], datos_jugador2['hp_maximo'], datos_jugador2['energia_maxima'])
        elif tipo == 'Electrico':
            pokemon_jugador2 = PokemonElectrico(datos_jugador2['nombre'], datos_jugador2['hp_maximo'], datos_jugador2['energia_maxima'])
        
        
    elif opcion =='2':
        mostrar_catalogo_disponible()
        
        eleccion_jugador_1 = input('Jugador 1, elija el numero de su Pokémon: ')
        print(f'¡Has seleccionado a {eleccion_jugador_1}')
        import random
        eleccion_jugador_2 = random.choice(list(CATALOGO_POKEMON.keys()))
        
        print(f'¡COMPUTADORA has seleccionado a {eleccion_jugador_2}')
        print('¡COMIENZA LA BATALLA!')
        print(f'{eleccion_jugador_1} ({tipo}) vs {eleccion_jugador_2} ({tipo})')
        
        datos_jugador1 = CATALOGO_POKEMON[eleccion_jugador_1]
        
       
        
        
        if tipo == 'Agua':
            pokemon_jugador1 = PokemonAgua(datos_jugador1['nombre'], datos_jugador1['hp_maximo'], datos_jugador1['energia_maxima'])
        elif tipo == 'Fuego':
            pokemon_jugador1 = PokemonFuego(datos_jugador1['nombre'], datos_jugador1['hp_maximo'], datos_jugador1['energia_maxima'])
        elif tipo == 'Planta':
            pokemon_jugador1 = PokemonPlanta(datos_jugador1['nombre'], datos_jugador1['hp_maximo'], datos_jugador1['energia_maxima'])
        elif tipo == 'Electrico':
            pokemon_jugador1 = PokemonElectrico(datos_jugador1['nombre'], datos_jugador1['hp_maximo'], datos_jugador1['energia_maxima'])
            
        
        
        datos_jugador2 = CATALOGO_POKEMON[eleccion_jugador_2]
        
        if tipo == 'Agua':
            pokemon_jugador2 = PokemonAgua(datos_jugador2['nombre'], datos_jugador2['hp_maximo'], datos_jugador2['energia_maxima'])
        elif tipo == 'Fuego':
            pokemon_jugador2 = PokemonFuego(datos_jugador2['nombre'], datos_jugador2['hp_maximo'], datos_jugador2['energia_maxima'])
        elif tipo == 'Planta':
            pokemon_jugador2 = PokemonPlanta(datos_jugador2['nombre'], datos_jugador2['hp_maximo'], datos_jugador2['energia_maxima'])
        elif tipo == 'Electrico':
            pokemon_jugador2 = PokemonElectrico(datos_jugador2['nombre'], datos_jugador2['hp_maximo'], datos_jugador2['energia_maxima'])
        
        
        
        
        
        
        
        
        
        
        
        
        
        tipo = datos_jugador1['tipo']
        tipo = datos_jugador2['tipo']  
        
        





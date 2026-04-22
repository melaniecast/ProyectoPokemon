
from pokedex import CATALOGO_POKEMON
from pokedex import mostrar_catalogo_disponible
from pokemon_agua import PokemonAgua
from pokemon_electrico import PokemonElectrico
from pokemon_fuego import PokemonFuego
from pokemon_planta import PokemonPlanta



    
    
def crear_pokemon(datos_jugador): 
    tipo = datos_jugador['tipo']   
        
    if tipo == 'Agua':
        return PokemonAgua(datos_jugador['nombre'], datos_jugador['hp_maximo'], datos_jugador['energia_maxima'])
    elif tipo == 'Fuego':
        return PokemonFuego(datos_jugador['nombre'], datos_jugador['hp_maximo'], datos_jugador['energia_maxima'])
    elif tipo == 'Planta':
        return PokemonPlanta(datos_jugador['nombre'], datos_jugador['hp_maximo'], datos_jugador['energia_maxima'])
    elif tipo == 'Electrico':
        return PokemonElectrico(datos_jugador['nombre'], datos_jugador['hp_maximo'], datos_jugador['energia_maxima'])
 
           
def menu_batalla():
    print ('='*50)
    print('     SIMLADOR DE BATALLAS POKÉMON (POO)     ')
    print ('='*50)
    print('Selecciones el Modo de Juego: \n1. Jugador vs Jugador\n2. Jugador vs Computadora')
    try:
        opcion = int(input('> Opción: '))
    except ValueError:
        print('Error: ingrese un numero valido')
        return     
            
    
    if opcion =='1':
        mostrar_catalogo_disponible()
        
        eleccion_jugador_1 = input('Jugador 1, elija el numero de su Pokémon: ')
        eleccion_jugador_2 = input('Jugador 2, elija el numero de su Pokémon: ')
        
        datos_jugador1 = CATALOGO_POKEMON[eleccion_jugador_1]
        datos_jugador2 = CATALOGO_POKEMON[eleccion_jugador_2]
        
        tipo_jugador1 = datos_jugador1['tipo']
        tipo_jugador2 = datos_jugador2['tipo']
        
        
        pokemon_jugador1 = crear_pokemon(datos_jugador1)
        pokemon_jugador2 = crear_pokemon(datos_jugador2)
       
        print(f'¡Has seleccionado a {eleccion_jugador_1}')
        print(f'¡Has seleccionado a {eleccion_jugador_2}')
        
        print('¡COMIENZA LA BATALLA!')
        print(f'{eleccion_jugador_1} ({tipo_jugador1}) vs {eleccion_jugador_2} ({tipo_jugador2})')
        combate(pokemon_jugador1, pokemon_jugador2)
        
        
      

        
    elif opcion =='2':
        mostrar_catalogo_disponible()
        
        eleccion_jugador_1 = input('Jugador 1, elija el numero de su Pokémon: ')
        print(f'¡Has seleccionado a {eleccion_jugador_1}')
        
        import random
        eleccion_jugador_2 = random.choice(list(CATALOGO_POKEMON.keys()))
        
        datos_jugador1 = CATALOGO_POKEMON[eleccion_jugador_1]
        datos_jugador2 = CATALOGO_POKEMON[eleccion_jugador_2]
        
        tipo_jugador1 = datos_jugador1['tipo']
        tipo_jugador2 = datos_jugador2['tipo']
        
        pokemon_jugador1 = crear_pokemon(datos_jugador1)
        pokemon_jugador2 = crear_pokemon(datos_jugador2)
        
       
        
        print('Computadora eligiendo combatiente...')
        print(f'¡La computadora ha seleccionado a {eleccion_jugador_2}')
        
        print('¡COMIENZA LA BATALLA!')
        
        print(f'{eleccion_jugador_1} ({tipo_jugador1}) vs {eleccion_jugador_2} ({tipo_jugador2})')
        combate(pokemon_jugador1, pokemon_jugador2)



def combate(pokemon_jugador1, pokemon_jugador2):
    turno_jugador1 =True
    import random
    
    while pokemon_jugador1.hp_actual > 0 and pokemon_jugador2.hp_actual > 0:
        oponente_computadora = False
        print(f'\n Estado: {pokemon_jugador1.nombre} HP: {pokemon_jugador1.hp_actual}  | {pokemon_jugador2.nombre} HP: {pokemon_jugador2.hp_actual}') 
       
        if turno_jugador1:
            pokemon_actual = pokemon_jugador1
            pokemon_oponente = pokemon_jugador2
            
        else: 
            pokemon_actual = pokemon_jugador2
            pokemon_oponente = pokemon_jugador1   
            
            
        if pokemon_actual.paralizado:
            pokemon_actual.paralizado = False
            turno_jugador1 = not turno_jugador1
            continue
           
            
            
        
        print('¿Qué acción deseas realizar?')
        print('1. Atacar (Costo: 15 EP)\n2. Defender (Costo: 5 EP\n3. Descansar (Restaura: 20 EP)')
        
        
        if oponente_computadora:
            opcion = random.choice(['1','2','3'])
            print(f'[Computadora elige: {opcion}]')
        else:
            opcion = input('> Opción: ')
        
        if opcion == '1':
            pokemon_actual.atacar(pokemon_oponente)
        elif opcion == '2':
            pokemon_actual.defensa()
        elif opcion == '3':
            pokemon_actual.descanso()
            
        turno_jugador1 = not turno_jugador1
        
        
        
    

    if pokemon_jugador1.hp_actual == 0:
        print(f'¡Ha ganado {pokemon_jugador2.nombre}!')
        print(f'[HP: {pokemon_jugador2.hp_actual }]  | [EP: {pokemon_jugador2.energia_actual }]')
    else: 
        print(f'¡Ha ganado {pokemon_jugador1.nombre}!')
        print(f'[HP: {pokemon_jugador1.hp_actual }]  |  [EP: {pokemon_jugador1.energia_actual }]')
            
    
menu_batalla()

        
        
       
            
                
        
                    
                
                
                
                
                
                
                
                
                
                
                
        
                
                
        
        
    
    
        
        
        
        
   
        
        
        
        
        
    
        
    
        
        
        
        
        
        
        

        
        





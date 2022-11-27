import random

opciones = ['piedra', 'papel', 'tijera']

cualquier_opcion = random.choice(opciones)

def juego(mi_opcion, opcion_random):

    if mi_opcion != opcion_random:
        if mi_opcion == 'piedra' and opcion_random =='tijera':
            print('Ganaste!'.center(60,'-'))
            print(f'El programa eligio ({opcion_random}) y tu ({mi_opcion})')
        elif mi_opcion == 'papel' and opcion_random == 'piedra':
            print('Ganaste!'.center(60,'-'))
            print(f'El programa eligio ({opcion_random}) y tu ({mi_opcion})')
        elif mi_opcion == 'tijera' and opcion_random == 'papel':
            print('Ganaste!'.center(60,'-'))
            print(f'El programa eligio ({opcion_random}) y tu ({mi_opcion})')
        else:
            print('Perdiste!'.center(60,'*'))
            print(f'El programa eligio ({opcion_random}) y tu ({mi_opcion})')
    else:
        print('Empate!'.center(60,'-'))
        print(f'Ambos eligieron {mi_opcion}!')


def verificar_opcion(opcion_usuario):
    if (opcion_usuario == 'piedra' or opcion_usuario =='papel' or opcion_usuario == 'tijera'):
        juego(opcion_usuario, cualquier_opcion)
    else:
        raise ValueError('Opción erróneTa')
print(' - Piedra \n - Papel \n - Tijera ')



opcion = input('\n: ')
opcion_mandar = opcion.lower()

verificar_opcion(opcion_mandar)
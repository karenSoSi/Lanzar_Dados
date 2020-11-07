import random


def lanzar_dado():
    """ Función que lanza dos dados y suma sus valores"""
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma = dado1 + dado2
    print("El primer dado es: ", dado1)
    print('El segundo dado es: ', dado2)
    print("La suma de los dado es ", suma)
    return "\n"


print(lanzar_dado())
otroJuego = input("Desea continuar lanzando? si/no")
otroJuego = str(otroJuego.lower())
while otroJuego == ("si"):
    print(lanzar_dado())
    otroJuego = input("Desea continuar? ")
    otroJuego = str(otroJuego.lower())
print("\nfin del juego")

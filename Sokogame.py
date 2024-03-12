import time
import sys

class SokoGame_Retroversion:

    mapa = [] # mapa del juego
    personaje_columna = 0
    personaje_fila = 0
    caja_columna = 1
    caje_fila = 1
    meta_columna = 2
    meta_fila = 2

    def __init__(self):
        # Define el mapa de jueg
        self.mapa =[
            [3,3,3,3,3,3,3,3,3],
            [3,4,4,4,4,4,2,4,3],
            [3,4,4,4,4,4,4,4,3],
            [3,4,4,4,4,4,4,4,3],
            [3,4,4,4,0,4,4,4,3],
            [3,4,4,4,4,4,4,4,3],
            [3,4,4,4,4,4,1,4,3],
            [3,4,4,4,4,4,4,4,3],
            [3,3,3,3,3,3,3,3,3]
        ]

        # Definimos la posicion inicial del personaje
        self.personaje_columna = 4
        self.personaje_fila = 4
        self.caja_columna = 6
        self.caja_fila = 6

    def imprimirMapa(self):
        # Limpiar la pantalla
        print("\033[H\033[J", end="")
        for fila in self.mapa:
            for numero in fila:
                if numero == 4:
                    print("  ", end=" ")  # Imprime un espacio en lugar del número 4
                elif numero == 0:
                    print("😾", end=" ")  # Imprime un emoji de gato en lugar del numero 0
                elif numero == 3:
                    print("🚧", end=" ")  # Imprime un emoji de gato en lugar del numero 3
                elif numero == 1:
                    print("📦", end=" ")  # Imprime un emoji de gato en lugar del numero 1
                elif numero == 2:
                    print("🚩", end=" ")  # Imprime un emoji de gato en lugar del numero 2
                else:
                    print(numero, end=" ")
            print()  # Agrega un salto de línea después de cada fila

    def movimiento_derecha(self):
        # Comprobar si hay una pared (3) a la derecha
        if self.mapa[self.personaje_fila][self.personaje_columna + 1] != 3:
            # Donde estaba el personaje pone un piso
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Donde estaba el piso pone al personaje
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            # Actualiza la posicion del personaje
            self.personaje_columna += 1


    def movimiento_izquierda(self):
        # Comprobar si hay una pared (3) a la izquierda
        if self.mapa[self.personaje_fila][self.personaje_columna - 1] != 3:
            # Donde estaba el personaje pone un piso
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Donde estaba el piso pone al personaje
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            # Actualiza la posicion del personaje
            self.personaje_columna -= 1

    def movimiento_abajo(self):
        # Comprobar si hay una pared (3) abajo
        if self.mapa[self.personaje_fila + 1][self.personaje_columna] != 3:
            # Donde estaba el personaje pone un piso
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Donde estaba el piso pone al personaje
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            # Actualiza la posicion del personaje
            self.personaje_fila += 1

    def movimiento_arriba(self):
        # Comprobar si hay una pared (3) arriba
        if self.mapa[self.personaje_fila - 1][self.personaje_columna] != 3:
            # Donde estaba el personaje pone un piso
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Donde estaba el piso pone al personaje
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            # Actualiza la posicion del personaje
            self.personaje_fila -= 1


    def jugar(self):
        while True:
            # Imprime el mapa
            self.imprimirMapa()
            # Pide al usuario el movimiento
            movimiento = input("Selecciona el movimiento (a: Left, d: Right, w: Up, s: Down): ")
            # Moverse a la derecha
            if movimiento == 'd':
                self.movimiento_derecha()

            # Moverse a la izquierda
            if movimiento == 'a':
                self.movimiento_izquierda()

            # Moverse hacia arriba
            if movimiento == 'w':
                self.movimiento_arriba()

            # Moverse hacia abajo
            if movimiento == 's':
                self.movimiento_abajo()

soko = SokoGame_Retroversion()
soko.jugar()

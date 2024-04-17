"""
        Author: JONATHAN KEVIN CRUZ ARANDA
        Date: 16/04/2024
        Items:

        0 -> Personaje
        1 -> Caja
        2 -> Meta
        3 -> Pared
        4 -> Piso
        5 -> Personaje_meta
        6 -> Caja_meta

        Description: Juego Sokoban en una versión retro para consola.
"""
import time
import sys

class SokoGame_Retroversion:

        mapa = [] # mapa del juego
        personaje_columna = 0
        personaje_fila = 0

        def __init__(self):
                # Define el mapa de juego 1
                self.mapa =[
                        [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
                        [3,4,4,4,4,4,4,4,4,4,4,4,4,3,4,4,2,3],
                        [3,4,0,4,3,4,4,4,4,4,4,4,4,4,4,2,2,3],
                        [3,4,4,4,3,4,4,4,4,4,4,4,4,3,4,2,2,3],
                        [3,3,3,3,3,4,4,4,4,4,4,4,4,3,3,3,3,3],
                        [3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3],
                        [3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3],
                        [3,4,4,4,1,4,4,4,3,4,3,4,4,4,4,4,4,3],
                        [3,4,4,4,1,4,4,4,3,1,3,4,4,4,4,4,4,3],
                        [3,4,4,1,1,4,4,4,3,4,3,4,4,4,4,4,4,3],
                        [3,4,4,4,4,4,4,4,3,4,4,4,4,4,4,4,4,3],
                        [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
                ]

                # Definimos la posicion inicial del personaje
                self.personaje_columna = 2
                self.personaje_fila = 2

        def imprimirMapa(self):
                # Limpiar la pantalla
                print("\033[H\033[J", end="")
                for fila in self.mapa:
                        for numero in fila:
                                if numero == 4:
                                # Imprime un espacio en lugar del número 4
                                        print("  ", end=" ")
                                # Imprime un emoji de gato enojado en luegar del numero 0
                                elif numero == 0:
                                        print("😾", end=" ")  
                                # Imprime un emoji de barrera en lugar del numero 3
                                elif numero == 3:
                                        print("🚧", end=" ")
                                # Imprime un emoji de caja en lugar del numero 1
                                elif numero == 1:
                                        print("📦", end=" ")
                                # Imprime un emoji de meta en lugar del numero 2
                                elif numero == 2:
                                        print("🏁", end=" ")
                                # Imprime un emoji de meta roja en lugar de numero 6 
                                elif numero == 6:
                                        print("🚩", end=" ")
                                # Imprime un emoji de gato riendose en lugar del numero 5
                                elif numero == 5:
                                        print("😹", end=" ")
                                # Imprime un numero es caso de no coincidir con alguna condicion 
                                else:
                                        print(numero, end=" ")
                        print()  # Agrega un salto de línea después de cada fila

                # Cuenta la cantidad de cajas en el mapa
                BOXES = sum(fila.count(1) for fila in self.mapa)
                print ("Remainig boxes", BOXES)
                if BOXES == 0:
                    print("You finished the map! ")


        def movimiento_derecha(self):
            # Movimiento [0,4] -> [4,0]
            if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
                    self.mapa[self.personaje_fila][self.personaje_columna] = 4
                    self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
                    self.personaje_columna += 1
            
            # Movimiento [0,2] -> [4,5]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 4
                        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
                        self.personaje_columna += 1
                
            # Movimiento [0,1,4] -> [4,0,1]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 4
                        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
                        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
                        self.personaje_columna += 1
                
            # Movimiento [0,1,2] -> [4,0,6]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 2:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 4
                        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
                        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
                        self.personaje_columna += 1

            # Movimiento [0,6,4] -> [4,5,1]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 4
                        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
                        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
                        self.personaje_columna += 1

            # Movimiento [0,6,2] -> [4,5,6]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 2:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 4
                        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
                        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
                        self.personaje_columna += 1
                
            # Movmiento [5,4] -> [2,0]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 2
                        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
                        self.personaje_columna += 1

            # Movimiento [5,2] -> [2,5]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 2
                        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
                        self.personaje_columna += 1

            # Movmiento [5,1,4] -> [2,0,1]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 2
                        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
                        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
                        self.personaje_columna += 1
                
            # Movimiento [5,1,2] -> [2,0,6]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 2:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 2
                        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
                        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
                        self.personaje_columna += 1
                
            # Movmiento [5,6,4] -> [2,5,1]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 2
                        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
                        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
                        self.personaje_columna += 1

            # Movmiento [5,6,2] -> [2,5,6]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 2:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 2
                        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
                        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
                        self.personaje_columna += 1

        def movimiento_izquierda(self):
            # Movimiento [4,0] -> [0,4]
            if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna- 1] == 4:
                    self.mapa[self.personaje_fila][self.personaje_columna] = 4
                    self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
                    self.personaje_columna -= 1

            # Movimiento [2,0] -> [5,4]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 4
                        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
                        self.personaje_columna -= 1

            # Movimiento [4,1,0] -> [1,0,4]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 4
                        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
                        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
                        self.personaje_columna -= 1

            # Movimiento [2,1,0] -> [6,0,4]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 2:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 4
                        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
                        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
                        self.personaje_columna -= 1

            # Movimiento [4,6,0] -> [1,5,4]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 4
                        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
                        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
                        self.personaje_columna -= 1

            # Movimiento [2,6,0] -> [6,5,4]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 2:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 4
                        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
                        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
                        self.personaje_columna -= 1

            # Movmiento [4,5] -> [0,2]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 2
                        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
                        self.personaje_columna -= 1

            # Movimiento [2,5] -> [5,2]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 2
                        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
                        self.personaje_columna -= 1

            # Movmiento [4,1,5] -> [1,0,2]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 2
                        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
                        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
                        self.personaje_columna -= 1

            # Movimiento [2,1,5] -> [6,0,2]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 2:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 2
                        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
                        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
                        self.personaje_columna -= 1

            # Movmiento [4,6,5] -> [1,5,2]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 2
                        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
                        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
                        self.personaje_columna -= 1

            # Movmiento [2,6,5] -> [6,5,2]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 2:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 2
                        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
                        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
                        self.personaje_columna -= 1
                
        def movimiento_arriba(self):
            # Movimiento [0][4] -> [4][0]
            if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 4:
                    self.mapa[self.personaje_fila][self.personaje_columna] = 4
                    self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
                    self.personaje_fila -= 1

            # Movimiento [0][2] -> [4][5]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 2:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 4
                        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
                        self.personaje_fila -= 1

            # Movimiento [0][1][4] -> [4][0][1]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 4
                        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
                        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
                        self.personaje_fila -= 1

            # Movimiento [0][1][2] -> [4][0][6]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 4
                        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
                        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
                        self.personaje_fila -= 1

            # Movimiento [0][6][4] -> [4][5][1]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 4
                        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
                        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
                        self.personaje_fila -= 1

            # Movimiento [0][6][2] -> [4][5][6]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 4
                        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
                        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
                        self.personaje_fila -= 1

            # Movmiento [5][4] -> [2][0]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 4:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 2
                        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
                        self.personaje_fila -= 1

            # Movimiento [5][2] -> [2][5]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 2:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 2
                        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
                        self.personaje_fila -= 1

            # Movmiento [5][1][4] -> [2][0][1]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 2
                        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
                        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
                        self.personaje_fila -= 1

            # Movimiento [5][1][2] -> [2][0][6]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 2
                        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
                        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
                        self.personaje_fila -= 1

            # Movmiento [5][6][4] -> [2][5][1]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 2
                        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
                        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
                        self.personaje_fila -= 1

            # Movmiento [5][6][2] -> [2][5][6]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2:
                        self.mapa[self.personaje_fila][self.personaje_columna] = 2
                        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
                        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
                        self.personaje_fila -= 1
            
        def movimiento_abajo(self):
            # Movimiento [0][4] -> [4][0]
            if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 4:
                self.mapa[self.personaje_fila][self.personaje_columna] = 4
                self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
                self.personaje_fila += 1

            # Movimiento [2][0] -> [5][4]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 2:
                    self.mapa[self.personaje_fila][self.personaje_columna] = 4
                    self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
                    self.personaje_fila += 1

            # Movimiento [4][1][0] -> [1][0][4]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4:
                    self.mapa[self.personaje_fila][self.personaje_columna] = 4
                    self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
                    self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
                    self.personaje_fila += 1

            # Movimiento [2][1][0] -> [6][0][4]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 2:
                    self.mapa[self.personaje_fila][self.personaje_columna] = 4
                    self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
                    self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
                    self.personaje_fila += 1

            # Movimiento [4][6][0] -> [1][5][4]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4:
                    self.mapa[self.personaje_fila][self.personaje_columna] = 4
                    self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
                    self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
                    self.personaje_fila += 1

            # Movimiento [2][6][0] -> [6][5][4]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 2:
                    self.mapa[self.personaje_fila][self.personaje_columna] = 4
                    self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
                    self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
                    self.personaje_fila += 1

            # Movmiento [4][5] -> [0][2]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 4:
                    self.mapa[self.personaje_fila][self.personaje_columna] = 2
                    self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
                    self.personaje_fila += 1

            # Movimiento [2][5] -> [5][2]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 2:
                    self.mapa[self.personaje_fila][self.personaje_columna] = 2
                    self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
                    self.personaje_fila += 1

            # Movmiento [4][1][5] -> [1][0][2]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4:
                    self.mapa[self.personaje_fila][self.personaje_columna] = 2
                    self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
                    self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
                    self.personaje_fila += 1

            # Movimiento [2][1][5] -> [6][0][2]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 2:
                    self.mapa[self.personaje_fila][self.personaje_columna] = 2
                    self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
                    self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
                    self.personaje_fila += 1

            # Movmiento [4][6][5] -> [1][5][2]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4:
                    self.mapa[self.personaje_fila][self.personaje_columna] = 2
                    self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
                    self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
                    self.personaje_fila += 1

            # Movmiento [2][6][5] -> [6][5][2]
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 2:
                    self.mapa[self.personaje_fila][self.personaje_columna] = 2
                    self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
                    self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
                    self.personaje_fila += 1
                
        def reiniciar_mapa(self):
            # Restaura el mapa a su estado inicial
            self.__init__()
    
                
        def jugar(self):
            while True:
                    # Imprime el mapa
                    self.imprimirMapa()
                    # Pide al usuario el movimiento
                    print ("a: Left")
                    print ("d: Right")
                    print ("w: Up")
                    print ("s: Down")
                    print ("r: Restart level")
                    movimiento = input()
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
                    # Reinicia el nivel
                    if movimiento == 'r':
                            self.reiniciar_mapa()
                        
soko = SokoGame_Retroversion()
soko.jugar()

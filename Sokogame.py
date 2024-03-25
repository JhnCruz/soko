import time
import sys

class SokoGame_Retroversion:

    mapa = [] # mapa del juego
    personaje_columna = 0
    personaje_fila = 0

    def __init__(self):
        # Define el mapa de jueg
        self.mapa =[
            [3,3,3,3,3,3,3,3,3],
            [3,4,4,4,4,4,2,4,3],
            [3,4,4,4,4,4,4,4,3],
            [3,4,4,4,4,4,4,4,3],
            [3,4,4,4,0,4,4,4,3],
            [3,4,4,4,4,4,4,4,3],
            [3,4,1,4,4,4,1,4,3],
            [3,4,4,4,4,4,4,4,3],
            [3,3,3,3,3,3,3,3,3]
        ]

        # Definimos la posicion inicial del personaje
        self.personaje_columna = 4
        self.personaje_fila = 4
  
    def imprimirMapa(self):
        # Limpiar la pantalla
        print("\033[H\033[J", end="")
        for fila in self.mapa:
            for numero in fila:
                if numero == 4:
                # Imprime un espacio en lugar del número 4
                    print("  ", end=" ")
                elif numero == 0:
                    print("😾", end=" ")  
                # Imprime un emoji de barrera en lugar del numero 0
                elif numero == 3:
                    print("🚧", end=" ")
                # Imprime un emoji de caja en lugar del numero 3
                elif numero == 1:
                    print("📦", end=" ")
                # Imprime un emoji de meta en lugar del numero 1
                elif numero == 2:
                    print("🏁", end=" ")
                # Imprime un emoji de meta roja en lugar de numero 2 
                elif numero == 6:
                    print("🚩", end=" ")
                # Imprime un numero en caso de no coincidir con alguna condicion 
                else:
                    print(numero, end=" ")
            print()  # Agrega un salto de línea después de cada fila

    def movimiento_derecha(self):
      # Comprobar si hay una pared (3) a la derecha
      if self.mapa[self.personaje_fila][self.personaje_columna + 1] != 3:
          # Si el siguiente elemento a la derecha es una caja (1) o caja_meta (6)
          if self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 or self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6:
              # Comprobar si hay espacio para mover la caja
              if (self.personaje_columna + 2) >= 0 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4:
                  # Mover la caja
                  self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
                  # Donde estaba la caja, pone al personaje
                  self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0 
                  # Si es siguiente espacio es una meta "2"
              elif self.mapa[self.personaje_fila][self.personaje_columna + 2] == 2:
                  # Convertir la meta en una caja-meta
                  self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
                  # Mover la caja a esa posición
                  self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0

          # Donde estaba el personaje pone un piso
          self.mapa[self.personaje_fila][self.personaje_columna] = 4
          # Donde estaba el piso pone al personaje
          self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
          # Actualiza la posicion del personaje
          self.personaje_columna += 1

    def movimiento_izquierda(self):
      # Comprobar si hay una pared (3) a la izquierda
      if self.mapa[self.personaje_fila][self.personaje_columna - 1] != 3:
          # Si el siguiente elemento a la derecha es una caja (1) o caja_meta (6)
          if self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 or self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6:
              # Comprobar si hay espacio para mover la caja
              if (self.personaje_columna - 2) >= 0 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4: 
                  # Mover la caja
                  self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
                  # Donde estaba la caja, pone al personaje
                  self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
                  # Si el siguiente espacio es una meta "2"
              elif self.mapa[self.personaje_fila][self.personaje_columna - 2] == 2:
                  # Convertir la meta en una caja-meta
                  self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
                  # Mover la caja a esa posición
                  self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0

          # Donde estaba el personaje pone un piso
          self.mapa[self.personaje_fila][self.personaje_columna] = 4
          # Donde estaba el piso pone al personaje
          self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
          # Actualiza la posicion del personaje
          self.personaje_columna -= 1

    def movimiento_arriba(self):
      # Comprobar si hay una pared (3) arriba
      if self.mapa[self.personaje_fila - 1][self.personaje_columna] != 3:
          # Si el siguiente elemento a la derecha es una caja (1) o caja_meta (6)
          if self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 or self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6:
              # Comprobar si hay espacio para mover la caja
              if (self.personaje_fila - 2) >= 0 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4:
                  # Mover la caja
                  self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
                  # Donde estaba la caja, pone al personaje
                  self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
                  # Si el siguiente espacio es una meta "2"
              elif self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2:
                  # Convertir la meta en una caja-meta
                  self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
                  # Mover la caja a esa posición
                  self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0

          # Donde estaba el personaje pone un piso
          self.mapa[self.personaje_fila][self.personaje_columna] = 4
          # Donde estaba el piso pone al personaje
          self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
          # Actualiza la posicion del personaje
          self.personaje_fila -= 1

    def movimiento_abajo(self):
      # Comprobar si hay una pared (3) abajo
      if self.mapa[self.personaje_fila + 1][self.personaje_columna] != 3:
          # Si el siguiente elemento a la derecha es una caja (1) o caja_meta (6)
          if self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 or self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6:
              # Comprobar si hay espacio para mover la caja
              if (self.personaje_fila + 2) < len(self.mapa) and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4:
                  # Mover la caja
                  self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
                  # Donde estaba la caja, pone al personaje
                  self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
                  # Si el siguiente espacio es una meta "2"
              elif self.mapa[self.personaje_fila + 2][self.personaje_columna] == 2:
                  # Convertir la meta en una caja-meta
                  self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
                  # Mover la caja a esa posición
                  self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5

          # Donde estaba el personaje pone un piso o meta
          self.mapa[self.personaje_fila][self.personaje_columna] = 4 
          # Donde estaba el piso pone al personaje
          self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
          # Actualiza la posicion del personaje
          self.personaje_fila += 1
    
    def jugar(self):
      while True:
          # Imprime el mapa
          self.imprimirMapa()
          # Pide al usuario el movimiento
          movimiento = input("Move to (a: Left, d: Right, w: Up, s: Down): ")
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

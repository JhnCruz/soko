class Soko:

    mapa = [] # mapa del juego
    personaje_columna = 0
    personaje_fila = 0

    def __init__(self):
        # Define el mapa de juego
        self.mapa =[
            [3,3,3,3,3],
            [3,4,4,4,3],
            [3,4,0,4,3],
            [3,4,4,4,3],
            [3,3,3,3,3]
        ]

        # Definimos la posicion inicial del personaje
        self.personaje_columna = 2
        self.personaje_fila = 2

    def imprimirMapa(self):
        for filas in self.mapa:
            print(filas)

    def movimiento_derecha(self):
        # Donde estaba el personaje pone un piso
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        # Donde estaba el piso pone al personaje
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
        # Actualiza la posicion del personaje
        self.personaje_columna += 1

    def movimiento_izquierda(self):
        # Donde estaba el personaje pone un piso
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        # Donde estaba el piso pone al personaje
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
        # Actualiza la posicion del personaje
        self.personaje_columna -= 1

    def movimiento_abajo(self):
        # Donde estaba el personaje pone un piso
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        # Donde estaba el piso pone al personaje
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
        # Actualiza la posicion del personaje
        self.personaje_fila += 1

    def movimiento_arriba(self):
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
            movimiento = input("Selecciona el movimiento (a: izquierda, d: derecha, w: arriba, s: abajo): ")
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


soko = Soko()
soko.jugar()

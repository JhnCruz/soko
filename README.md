# SOKO

### 1.- OBJETIVO
**Implementación de un codigo Python para la creación de un sokoban versión retro consola.**
___
### 2.- ¿Que es?

*El Sokoban es un juego de rompecabezas que pone a prueba la lógica y la planificación estratégica del jugador. El objetivo principal del juego es empujar cajas o bloques dentro de un almacén, con el fin de colocar cada una de ellas en una posición específica. A primera vista, puede parecer sencillo, pero a medida que avanzas en los niveles, se presentan desafíos cada vez más complejos que requieren de una cuidadosa planificación de movimientos para evitar quedarse atascado o bloquear el camino hacia la meta. Sokoban es un juego que combina la simplicidad de sus reglas con la profundidad de su jugabilidad, proporcionando horas de entretenimiento para aquellos que disfrutan de desafíos mentales.*

### 3.- Reglas y mecanica del juego.

- Moverse hacia arriba sobre el piso.
- Moverse hacia abajo sobre el piso.
- Moverse hacia la derecha sobre el piso.
- Moverse hacia la izquierda sobre el piso.
- Reiniciar nivel.
- Empujar una 1 caja hacia arriba y que delante este un piso.
- Empujar una 1 caja hacia abajo y que delante este un piso.
- Empujar una 1 caja hacia la derecha y que delante este un piso.
- Empujar una 1 caja hacia la izquierda y que delante este un piso.

### Elementos
- 0 - Personaje
- 1 - Cajas
- 2 - Metas
- 3 - Paredes
- 4 - Piso
- 5 - Pesonaje_meta
- 6 - Caja_meta

#### Mapa
````code
mapa = [
            [3,3,3,3,3],
            [3,4,4,4,3],
            [3,4,0,4,3],
            [3,4,4,4,3],
            [3,3,3,3,3]
        ]
````
<br>
<br>
|3, &nbsp;3, &nbsp;3, &nbsp;3, &nbsp;3, &nbsp;3, &nbsp;3| <br>
|3, &nbsp;4, &nbsp;4, &nbsp;4, &nbsp;4, &nbsp;4, &nbsp;3| <br>
|3, &nbsp;4, &nbsp;4, &nbsp;4, &nbsp;4, &nbsp;4, &nbsp;3| <br>
|3, &nbsp;4, &nbsp;4, &nbsp;0, &nbsp;4, &nbsp;4, &nbsp;3| <br>
|3, &nbsp;4, &nbsp;4, &nbsp;4, &nbsp;4, &nbsp;4, &nbsp;3| <br>
|3, &nbsp;4, &nbsp;4, &nbsp;4, &nbsp;4, &nbsp;4, &nbsp;3| <br>
|3, &nbsp;3, &nbsp;3, &nbsp;3, &nbsp;3, &nbsp;3, &nbsp;3| <br>
### NIveles del juego
 - De 1 a "n" niveles.
____
# El final de juego se obtendra hasta terminar el numero maximo de niveles.
___
### Record goblal __user_09898__ 

| Intentos por nivel | Tiempo promedio | Niveles superados |
|:--------:|:---------------:|:-----------------:|
|1|3:00min|3|

# Redes sociales
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Instagram_logo_2022.svg/1200px-Instagram_logo_2022.svg.png" alt="Imagen 1" style="width:70px;height:70px;"> <img src="https://www.facebook.com/images/fb_icon_325x325.png" alt="Imagen 2" style="width:70px;height:70px;">

[Instagram](https://www.instagram.com/accounts/login/?next=https%3A%2F%2Fwww.instagram.com%2F) [Facebook](https://www.facebook.com/?locale=es_LA)


## 4. Controles

Para moverse en el juego el usuario utilizará alguna de las siguientes letras para indicar hacia adonde se quiere mover:

- a -> Izquierda
- s -> Derecha
- w -> Arriba
- s -> Abajo

Nota: El proceso es que se muestra el mapa y se solicita al usuario que escriba la letra hacia donde se quiere mover, despúes de colocar la letra se preciona enter y se actualiza el mapa, este proceso se repite de forma infinita.


## 5. Función a implementar

Para llevar un mejor control del avance del desarrollo llenar Kanban con los siguientes elementos (ToDo, Doing y Done).

| No. |Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 0. | Cargar el siguiente nivel. | - | - |
| 1. | Repetir el juego hasta terminar el nivel. | - | - |
| 2. | Imprimir mapa.| - | - |
| 3. | Leer el movimiento. | - | - |
| 4. | Evaluar el movimiento del usuario. | - | - |

## Derecha

Ejemplo de movimientos Inicio y Fin:

- Personaje, Espacio [0,4] -> Espacio, Personaje [4,0] |


| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 5. | Personaje, espacio  | Done | [ 0,4 ] | [ 4,0 ] | 12/04/2024 |
| 6. | Personaje, meta  | Done | [ 0,2 ] | [ 4,5 ] | 12/04/2024 |
| 7. | Personaje, caja, espacio | Done | [ 0,1,4 ] | [ 4,0,1 ] | 12/04/2024 |
| 8. | Personaje, caja,  meta | Done | [ 0,1,2 ] | [ 4,0,6 ] | 12/04/2024 |
| 9. | Personaje, caja_meta, espacio | Done | [ 0,6,4 ] | [ 4,5,1 ] | 12/04/2024 |
| 10. |Personaje, caja_meta, meta | Done | [ 0,6,2 ] | [ 4,5,6 ] | 12/04/2024 |
| 11. | Personaje_meta, espacio | Done | [ 5,4 ] | [ 2,0 ] | 12/04/2024 |
| 12. | Personaje_meta, meta | Done | [ 5,2 ] | [ 2,5 ] | 12/04/2024 |
| 13. | Personaje_meta, caja, espacio | Done | [ 5,1,4 ] | [ 2,0,1 ] | 12/04/2024 |
| 14. | Personaje_meta, caja, meta | Done | [ 5,1,2 ] | [ 2,0,6 ] | 12/04/2024 |
| 15. | Personaje_meta, caja_meta, espacio | Done | [ 5,6,4 ] | [ 2,5,1 ] | 12/04/2024 |
| 16. | Personaje_meta, caja_meta, meta | Done | [ 5,6,2 ] | [ 2,5,6 ] | 12/04/2024 |

## Izquierda

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 17. | Personaje, espacio | - | [       ] | [       ] | - |
| 18. | Personaje, meta | - | [       ] | [       ] | - |
| 19. | Personaje, caja, espacio | - | [       ] | [       ] | - |
| 20. | Personaje, caja, meta | - | [       ] | [       ] | - |
| 21. | Personaje, caja_meta, espacio | - | [       ] | [       ] | - |
| 22. | Personaje, caja_meta, meta | - | [       ] | [       ] | - |
| 23. | Personaje_meta, espacio | - | [       ] | [       ] | - |
| 24. | Personaje_meta, meta | - | [       ] | [       ] | - |
| 25. | Personaje_meta, caja, espacio | - | [       ] | [       ] | - |
| 26. | Personaje_meta, caja, meta | - | [       ] | [       ] | - |
| 27. | Personaje_meta, caja_meta, espacio | - | [       ] | [       ] | - |
| 28. | Personaje_meta, caja_meta, meta | - | [       ] | [       ] | - |

## Arriba

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 29. | Personaje, espacio | - | [][] | [][] | - |
| 30. | Personaje, meta | - | [][] | [][] | - |
| 31. | Personaje, caja, espacio | - | [][] | [][] | - |
| 32. | Personaje, caja, meta | - | [][] | [][] | - |
| 33. | Personaje, caja_meta, espacio | - | [][] | [][] | - |
| 34. | Personaje, caja_meta, meta | - | [][] | [][] | - |
| 35. | Personaje_meta, espacio | - | [][] | [][] | - |
| 36. | Personaje_meta, meta | - | [][] | [][] | - |
| 37. | Personaje_meta, caja, espacio | - | [][] | [][] | - |
| 38. | Personaje_meta, caja, meta | - | [][] | [][] | - |
| 39. | Personaje_meta, caja_meta, espacio | - | [][] | [][] | - |
| 40. | Personaje_meta, caja_meta, meta | - | [][] | [][] | - |

## Abajo

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 41. | Personaje, espacio | - | [][] | [][] | - |
| 42. | Personaje, meta | - | [][] | [][] | - |
| 43. | Personaje, caja, espacio | - | [][] | [][] | - |
| 44. | Personaje, caja, meta | - | [][] | [][] | - |
| 45. | Personaje, caja_meta, espacio | - | [][] | [][] | - |
| 46. | Personaje, caja_meta, meta | - | [][] | [][] | - |
| 47. | Personaje_meta, espacio | - | [][] | [][] | - |
| 48. | Personaje_meta, meta | - | [][] | [][] | - |
| 49. | Personaje_meta, caja, espacio | - | [][] | [][] | - |
| 50. | Personaje_meta, caja, meta | - | [][] | [][] | - |
| 51. | Personaje_meta, caja_meta, espacio | - | [][] | [][] | - |
| 52. | Personaje_meta, caja_meta, meta | - | [][] | [][] | - |

## Determina si se completo el nivel o no

| No. | Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 53. | Evaluar si el nivel esta terminado (Esto sucede cuando todas las cajas estan sobre las metas), SI el nivel esta terminado cargar el siguiente nivel (Los niveles de juego estarán en archivos de texto independiente). | - | - |
| 54. | Reiniciar el mapa (Con la letra r, se vuelve a cargar el nivel que se esta jugando) | - | - |

## Función extra

| No. | Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 55. | Función adicional o powerup (descripción). | - | - |

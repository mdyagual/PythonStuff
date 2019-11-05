"""
------------DESCRIPCION DEL PROBLEMA------------------
Usted elaborará una simulación del juego de
disparos de tiro al blanco con patos.
El jugador cuenta con 30 municiones para
realizar los disparos y cada pato tiene un nivel de
vida.
Para realizar esta simulación usted creará una
lista con 6 números aleatorios diferentes entre 1
y 6. Cada uno de los elementos de la lista
representa a un pato con su nivel de vida.
[3, 5, 4, 2, 1, 6]
El jugador deberá ingresar por teclado la posición
del pato al que va a disparar. El disparar a un pato
significa que debe reducir su nivel de vida de 1 en 1. Cuando el nivel de vida del pato esté en 0
significa que ese pato ha sido eliminado del juego. (Nota.- Validar que el jugador ingrese una
posición válida y que no le dispare a un pato que ya ha sido eliminado. SI esto ocurre, volver a
pedir la posición, hasta que la posición sea válida.)

**El programa debe mostrarle al jugador cuantos tiros restantes le quedan cada vez que haya
realizado un disparo.
La simulación del juego termina cuando el jugador ya no tiene municiones para disparar o
cuando haya eliminado todos los patos.
Al final del juego, el programa debe mostrarle al jugador cuantos patos eliminó en total.
"""

import random as r

municiones=30

patos=[]

while(len(patos)<6):
    patito=r.randint(1,6)
    if(patito not in patos):
        patos.append(patito)

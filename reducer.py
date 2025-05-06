#!/usr/bin/python3

import sys

# Variables para rastrear el género actual, el puntaje total y el conteo
current_genre = None
total_score = 0
count = 0

# Leer cada línea de la entrada estándar
for line in sys.stdin:
    # Dividir la línea en género y puntaje
    genre, score = line.strip().split("\t")
    score = float(score)

    # Si el género es el mismo que el género actual
    if genre == current_genre:
        # Acumular el puntaje y aumentar el conteo
        total_score += score
        count += 1
    else:
        # Si el género es diferente al género actual
        if current_genre:
            # Calcular el promedio del puntaje para el género anterior
            avg = total_score / count
            # Imprimir el género, el promedio del puntaje y el conteo
            print(f"{current_genre}\t{avg:.2f}\t{count}")
        # Actualizar el género actual, el puntaje total y el conteo
        current_genre = genre
        total_score = score
        count = 1

# Procesar la última línea
if current_genre:
    avg = total_score / count
    print(f"{current_genre}\t{avg:.2f}\t{count}")

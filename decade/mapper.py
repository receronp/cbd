#!/usr/bin/python3

import sys
import csv

# Columnas CSV:
# 0: Title, 1: Genre, 2: Tags, ..., 12: IMDb Score, ...
reader = csv.reader(sys.stdin)
next(reader)  # Saltar header

for row in reader:
    if len(row) < 19:  # Validar que hay suficientes columnas
        continue

    genre_str = row[1].strip()  # Genre (columna 1)
    score_str = row[12].strip()  # IMDb Score (columna 12)
    release_date_str = row[18].strip()  # Release Date (column 18)

    if not genre_str or not score_str:  # Saltar si hay campos vacíos
        continue

    try:
        score = float(score_str)  # Convertir a float
    except ValueError:  # Saltar valores inválidos (e.g., "N/A")
        continue

    # Extraer el año de la fecha de lanzamiento (columna 3)
    try:
        year = release_date_str.split()[-1]  # Extract the year (last part of the date string)
        decade = (int(year) // 10) * 10  # Calculate the decade
    except IndexError:
        continue

    # Separar géneros por comas y emitir cada uno con su puntaje
    # (e.g., "Action, Adventure" -> ["Action", "Adventure"])
    genres = [g.strip() for g in genre_str.split(",")]
    for genre in genres:
        if genre:  # Validar que el género no esté vacío
            print(f"{genre}_{decade}\t{score}")  # Emitir género y puntaje

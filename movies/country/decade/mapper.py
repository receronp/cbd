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
    kind_str = row[4].strip()  # Series or Movie (columna 4)
    country_str = row[6].strip()  # Country Availability (columna 6)
    score_str = row[12].strip()  # IMDb Score (columna 12)
    release_date_str = row[18].strip()  # Release Date (column 18)

    if not genre_str or not score_str or not kind_str:  # Saltar si hay campos vacíos
        continue

    if kind_str != "Movie":
        continue

    try:
        score = float(score_str)  # Convertir a float
    except ValueError:  # Saltar valores inválidos (e.g., "N/A")
        continue

    # Extraer el año de la fecha de lanzamiento (columna 18)
    try:
        year = release_date_str.split()[-1]  # Extract the year (last part of the date string)
        decade = (int(year) // 10) * 10  # Calculate the decade
        if decade < 2020:
            continue
    except IndexError:
        continue

    
    # Separar países por comas y validar que "Spain" esté presente
    # (e.g., "Spain, France" -> ["Spain", "France"])
    countries = [c.strip() for c in country_str.split(",")]
    if "Spain" in countries:
        # Separar géneros por comas y emitir cada uno con su puntaje
        # (e.g., "Action, Adventure" -> ["Action", "Adventure"])
        genres = [g.strip() for g in genre_str.split(",")]
        for genre in genres:
            if genre:  # Validar que el género no esté vacío
                print(f"{genre}\t{score}")  # Emitir género y puntaje

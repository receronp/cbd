#!/usr/bin/python3

import sys
import csv

# CSV Columns:
# 0: Title, 1: Genre, 2: Tags, ..., 12: IMDb Score, ..., 18: Release Date
reader = csv.reader(sys.stdin)
next(reader)  # Skip header

for row in reader:
    if len(row) < 19:  # Ensure row has enough columns
        continue

    genre_str = row[1].strip()  # Genre (column 1)
    kind_str = row[4].strip()  # Title (column 4)
    score_str = row[12].strip()  # IMDb Score (column 12)
    release_date_str = row[18].strip()  # Release Date (column 18)

    if not genre_str or not score_str or not kind_str or not release_date_str:  # Skip if empty
        continue

    if kind_str == "Movie":
        continue

    try:
        score = float(score_str)  # Convert score to float
    except ValueError:  # Skip invalid scores (e.g., "N/A")
        continue

    # Extract year from release date
    try:
        year = release_date_str.split()[-1]  # Extract the year (last part of the date string)
        decade = (int(year) // 10) * 10  # Calculate the decade
    except IndexError:
        continue

    # Split genres by comma and emit each one with the score and decade
    genres = [g.strip() for g in genre_str.split(",")]
    for genre in genres:
        if genre:  # Ensure genre is not empty
            print(f"{genre}\t{score}\t{decade}")  # Emit: <genre>\t<score>\t<decade>

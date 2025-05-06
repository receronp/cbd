#!/usr/bin/python3

import sys
from collections import defaultdict

# Structure: { (genre, decade): (total_score, count) }
genre_decade_stats = defaultdict(lambda: [0.0, 0])

for line in sys.stdin:
    try:
        genre, score, decade = line.strip().split("\t")
        score = float(score)
        genre_decade = (genre, decade)
        genre_decade_stats[genre_decade][0] += score
        genre_decade_stats[genre_decade][1] += 1
    except:
        continue  # Skip malformed lines

# Collect and sort results by genre and then by decade
sorted_results = sorted(
    genre_decade_stats.items(),
    key=lambda x: (x[0][0], int(x[0][1])),  # Sort by genre, then by decade
)

# Emit sorted results
for (genre, decade), (total_score, count) in sorted_results:
    avg_score = total_score / count
    print(f"{genre}\t{decade}\t{avg_score:.2f}\t{count}")

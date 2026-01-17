"""
Netflix Movies Analysis

This script analyzes Netflix movie data to investigate trends from the 1990s.
It focuses on identifying the most common movie duration and counting
short action movies released during that decade.

Author: David Steven H
Date: November 2025
"""

import pandas as pd

# Load the Netflix dataset
df = pd.read_csv('netflix_data.csv')

print("Dataset loaded successfully!")
print(f"Total records: {len(df)}")
print("-" * 50)

# ANALYSIS 1: Most Common Movie Duration

# Calculate the most frequent movie duration (mode)
duration = df['duration'].mode().iloc[0]

print(f"\n📊 Most common movie duration: {duration} minutes")
print("-" * 50)

# ANALYSIS 2: Short Action Movies (1990s)

# Filter movies from the 1990s (1990-1999)
year_movie = df[(df['release_year'] >= 1990) & (df['release_year'] < 2000)]

# Filter short action movies from the 1990s
# Criteria:
#   - Released between 1990-1999
#   - Genre is "Action" (case-insensitive)
#   - Duration less than 90 minutes
short_movies_action = df[
    (df['release_year'] >= 1990) &
    (df['release_year'] <= 1999) &
    (df['genre'].str.lower() == 'action') &
    (df['duration'] < 90)
]

# Count the number of short action movies
short_movie_count = short_movies_action.shape[0]

print(f"\n🎬 Short action movies (< 90 min) in the 1990s: {short_movie_count}")
print("-" * 50)

# SUMMARY

print("\n✅ Analysis complete!")
print(f"   • Most common duration: {duration} minutes")
print(f"   • 1990s short action movies: {short_movie_count}")
print("-" * 50)
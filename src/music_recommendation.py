import pandas as pd

# ─────────────────────────────────────────────
# 1. Load Datasets
# ─────────────────────────────────────────────

# Step 1: Read the main dataset
data = pd.read_csv('../data/data.csv')

# Step 2: Read the genre dataset
genre_data = pd.read_csv('../data/data_by_genres.csv')

# Step 3: Read the year dataset
year_data = pd.read_csv('../data/data_by_year.csv')

# Step 4: Read the artist dataset
artist_data = pd.read_csv('../data/data_by_artist.csv')

# ─────────────────────────────────────────────
# 5. Display First Two Rows of Each Dataset
# ─────────────────────────────────────────────

print("=" * 60)
print("First 2 rows of data:")
print("=" * 60)
print(data.head(2))

print("\n" + "=" * 60)
print("First 2 rows of genre_data:")
print("=" * 60)
print(genre_data.head(2))

print("\n" + "=" * 60)
print("First 2 rows of year_data:")
print("=" * 60)
print(year_data.head(2))

print("\n" + "=" * 60)
print("First 2 rows of artist_data:")
print("=" * 60)
print(artist_data.head(2))

# ─────────────────────────────────────────────
# 6. Dataset Info
# ─────────────────────────────────────────────

print("\n" + "=" * 60)
print("Info for data:")
print("=" * 60)
data.info()

print("\n" + "=" * 60)
print("Info for genre_data:")
print("=" * 60)
genre_data.info()

# ─────────────────────────────────────────────
# 7. Create a 'decade' Column in data
# ─────────────────────────────────────────────

# Extract the decade from the 'year' column using apply() and a lambda function
# e.g., year 1984 → decade 1980, year 2003 → decade 2000
data['decade'] = data['year'].apply(lambda year: (year // 10) * 10)

print("\n" + "=" * 60)
print("data with 'decade' column (first 5 rows):")
print("=" * 60)
print(data[['year', 'decade']].head())
print("\nUnique decades found:", sorted(data['decade'].unique()))

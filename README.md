# 🎵 Music Recommendation System

> **GoMyCode Data Science Bootcamp — Capstone Project**

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-3.0-150458?logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.x-F7931E?logo=scikit-learn&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-6.x-3F4F75?logo=plotly&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Project Overview

This project is a complete **Exploratory Data Analysis (EDA) and Clustering pipeline** built on a large Spotify music dataset. The goal is to understand patterns in music features across decades, genres, and artists — and to lay the groundwork for a content-based **Music Recommendation System**.

The project was completed as part of the **Data Science Bootcamp at [GoMyCode](https://gomycode.com/)**.

---

## 🗂️ Dataset

The project uses four CSV datasets derived from the Spotify API:

| File | Variable | Description |
|---|---|---|
| `data/data.csv` | `data` | 170,653 individual tracks with full audio features |
| `data/data_by_genres.csv` | `genre_data` | Aggregated audio features per genre (2,973 genres) |
| `data/data_by_year.csv` | `year_data` | Aggregated audio features per year |
| `data/data_by_artist.csv` | `artist_data` | Aggregated audio features per artist |

### Key Audio Features
`valence` · `acousticness` · `danceability` · `energy` · `instrumentalness` · `liveness` · `loudness` · `speechiness` · `tempo` · `popularity`

---

## 📁 Project Structure

```
musicrecommendationproject/
│
├── data/
│   ├── data.csv                  # Main track dataset
│   ├── data_by_genres.csv        # Genre-level aggregates
│   ├── data_by_year.csv          # Year-level aggregates
│   └── data_by_artist.csv        # Artist-level aggregates
│
├── src/
│   ├── music_recommendation.ipynb   # Main Jupyter Notebook (EDA + Clustering)
│   └── music_recommendation.py      # Equivalent Python script
│
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have **Python 3.9+** installed, then install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn plotly wordcloud scikit-learn
```

Or from inside the Jupyter notebook (first cell):

```python
import sys
!{sys.executable} -m pip install pandas numpy matplotlib seaborn plotly wordcloud scikit-learn -q
```

### Running the Notebook

```bash
cd src
jupyter notebook music_recommendation.ipynb
```

---

## 📊 Analysis Walkthrough

### Phase 1 — Data Loading & Inspection
- Loaded all four datasets using `pd.read_csv()`
- Previewed structure with `head()` and `info()`
- Confirmed no null values across all datasets

### Phase 2 — Feature Engineering
- Created a `decade` column from the `year` field:
  ```python
  data['decade'] = data['year'].apply(lambda year: (year // 10) * 10)
  ```

### Phase 3 — Exploratory Data Analysis
| Visualization | Tool | Insight |
|---|---|---|
| Track count per decade | `sns.countplot` | Exponential growth in modern tracks |
| Sound features over time | `px.line` | Acousticness ↓, Energy ↑ over decades |
| Loudness over time | `px.line` | The "Loudness War" clearly visible |
| Top 10 genres — audio features | `px.bar` | Pop/hip-hop genres dominate energy & danceability |
| Genre word cloud | `WordCloud` | Diversity of subgenres in the dataset |
| Artist word cloud | `WordCloud` | Prolific and popular artists visualized |
| Top 10 most prolific artists | `DataFrame` | Ranked by song count |
| Top 10 most popular artists | `DataFrame` | Ranked by popularity score |

### Phase 4 — Clustering

#### 🎸 Genre Clustering — K-Means (12 Clusters) + t-SNE
- Scaled 10 audio features with `StandardScaler`
- Applied `KMeans(n_clusters=12)` to group genres by sound profile
- Visualized clusters in 2D using **t-SNE** with interactive Plotly scatter (hover = genre name)

#### 🎵 Song Clustering — K-Means (25 Clusters) + PCA
- Scaled 15 audio + metadata features
- Applied `KMeans(n_clusters=25)` to group individual songs
- Visualized clusters using **PCA** (2 principal components) with hover showing song name, artist, year, and popularity

---

## 🔍 Key Findings

- 📈 **Tracks per decade** grew exponentially — 2010s and 2020s dominate the dataset
- 🎸 **Acousticness** declined steeply post-1960s; **Energy** rose steadily
- 🔊 **Loudness** increased consistently — reflecting the music industry's "Loudness War"
- 🎤 **Prolific ≠ Popular** — the most song-producing artists are not the highest-rated
- 🤖 **K-Means clustering** reveals natural groupings in both genres and songs based purely on audio DNA — the foundation for content-based recommendation

---

## 🛠️ Tech Stack

| Library | Purpose |
|---|---|
| `pandas` | Data loading and manipulation |
| `numpy` | Numerical operations |
| `matplotlib` | Base plot rendering |
| `seaborn` | Statistical visualizations |
| `plotly` | Interactive charts |
| `wordcloud` | Genre and artist word clouds |
| `scikit-learn` | KMeans, PCA, t-SNE, StandardScaler |

---

## 🎓 About GoMyCode

[GoMyCode](https://gomycode.com/) is a leading tech education platform across Africa and the Middle East, offering immersive bootcamps in Data Science, Web Development, AI, and more. This project was completed as part of their **Data Science track**.

---

## 👤 Author

**Yassine Gabsi**
- GitHub: [@yassinegab](https://github.com/yassinegab)
- Project Repository: [Music-Recommendation-System-](https://github.com/yassinegab/Music-Recommendation-System-)

---
## 👤 Instructor
**Oumaima Dridi**
- GitHub: [@yassinegab](https://github.com/yassinegab)
---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

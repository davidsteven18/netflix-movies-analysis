# Netflix Movies Analysis 🎬

A data analysis project investigating Netflix movie trends from the 1990s, focusing on movie durations and genre patterns.

## 📊 Project Overview

This project analyzes Netflix movie data to answer key questions about content from the 1990s:
- What is the most common movie duration?
- How many short action movies (under 90 minutes) were released in the 1990s?

## 🎯 Key Findings

The analysis reveals:
- **Most common movie duration**: Extracted using mode calculation
- **Short action movies count**: Number of action films under 90 minutes released between 1990-1999

## 🛠️ Technologies Used

- **Python 3.x**
- **pandas** - Data manipulation and analysis
- **CSV** - Data source format

## 📁 Project Structure

```
NetflixProject/
│
├── Investigating_Netflix_movies.py   # Main analysis script
├── netflix_data.csv                  # Dataset
├── notebook.ipynb                    # Jupyter notebook (optional)
├── requirements.txt                  # Python dependencies
└── README.md                         # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/netflix-project.git
   cd netflix-project
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate  # On Windows
   # or
   source .venv/bin/activate      # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Analysis

```bash
python Investigating_Netflix_movies.py
```

## 📈 Dataset

The dataset (`netflix_data.csv`) contains Netflix content information with the following columns:
- `show_id` - Unique identifier
- `type` - Movie or TV Show
- `title` - Content title
- `director` - Director name
- `cast` - Cast members
- `country` - Country of origin
- `date_added` - Date added to Netflix
- `release_year` - Year of release
- `duration` - Movie duration in minutes
- `description` - Content description
- `genre` - Content genre

## 🔍 Analysis Details

### 1. Most Common Movie Duration
```python
duration = df['duration'].mode().iloc[0]
```
Calculates the mode (most frequent value) of movie durations across the entire dataset.

### 2. Short Action Movies in the 1990s
```python
short_movies_action = df[
    (df['release_year'] >= 1990) &
    (df['release_year'] <= 1999) &
    (df['genre'].str.lower() == 'action') &
    (df['duration'] < 90)
]
```
Filters movies based on:
- Release year between 1990-1999
- Genre is "Action"
- Duration less than 90 minutes

## 📝 Future Improvements

- [ ] Add data visualizations (matplotlib/seaborn)
- [ ] Expand analysis to other decades
- [ ] Include TV shows analysis
- [ ] Add statistical tests
- [ ] Create interactive dashboard

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Dataset source: Netflix content data
- Inspired by data science learning projects

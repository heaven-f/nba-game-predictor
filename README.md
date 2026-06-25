# 🏀 NBA Game Outcome Predictor

A data analytics project that uses historical NBA game data to estimate game outcomes and explore factors that influence winning.

---

## 🎯 Project Goal

Use historical NBA game data to analyze factors that influence game outcomes and build a predictive model to estimate winners.

---

## 📊 Dataset

**Source:** [Kaggle](https://www.kaggle.com/datasets/eoinamoore/historical-nba-data-and-player-box-scores)

* Historical NBA games from 1946–2026
* Current modeling focuses on games from **2000–present**
* Approximately **36,000+ games** analyzed

---

## 🚧 Current Progress

### Completed

* [x] Dataset acquired
* [x] Exploratory Data Analysis
* [x] Data Cleaning
* [x] Team Strength Feature Engineering
* [x] Recent Form Feature Engineering
* [x] Prediction Function

### In Progress

* [ ] Machine Learning Model Training
* [ ] Model Evaluation
* [ ] Streamlit Application

---

## 🧠 Current Model

The current prediction system combines:

* Team Strength

  * Home win rate
  * Away win rate

* Recent Form

  * Rolling win percentage over the last 10 games

The model converts these metrics into win probabilities and predicts a winner for a given matchup.

### Example

```python
predict_game("Heat", "Bucks")
```

Example output:

```text
Heat: 52.4%
Bucks: 47.6%

Predicted Winner: Heat
```

---

## 🛠️ Tools Used

* Python
* Pandas
* NumPy
* Jupyter Notebook
* VS Code

---

## 🚀 Future Improvements

* Logistic Regression
* Elo Rating System
* Streamlit Web App
* Player Statistics
* Injury Data
* Advanced Team Metrics

---

## 👤 Author

Heaven Frazier

B.S. Computer Science
University of the District of Columbia

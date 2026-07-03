# 🏀 NBA Game Outcome Predictor

Predicting NBA game outcomes using historical game data and leakage-free machine learning feature engineering.

---

## 🎯 Project Goal

Build a machine learning pipeline that engineers features chronologically, ensuring predictions are based only on information available before each game.

---

## 📊 Dataset

**Source:** [Kaggle](https://www.kaggle.com/datasets/eoinamoore/historical-nba-data-and-player-box-scores)

- Historical NBA games from 1946–2026
- Current model trained using games from **2000–present**
- Approximately **36,000+ regular season and playoff games**

---

## 📁 Repository Structure

```
NBA-Game-Predictor/
│
├── data/
│   └── nba_games.csv
│
├── notebooks/
│   ├── 01_dataset_exploration.ipynb
│   └── 02_prediction_pipeline.ipynb
│
├── README.md
└── requirements.txt
```

---

## ✅ Current Progress

### Completed
- [x] Dataset acquisition and exploration
- [x] Data cleaning and preprocessing
- [x] Chronological team timeline construction
- [x] Leakage-free rolling feature engineering
- [x] Machine learning dataset construction

### In Progress
- [ ] Chronological train/test split
- [ ] Logistic Regression model
- [ ] Model evaluation

### Planned
- [ ] Streamlit web application
- [ ] Feature importance visualization
- [ ] Additional predictive features
- [ ] Model comparison

---

## 🧠 Features Engineered

All rolling statistics are shifted to ensure they only use games that occurred before the prediction target, preventing data leakage.

- Rolling 5-game win percentage
- Rolling 10-game win percentage
- Rolling 5-game average point differential
- Rolling 10-game average point differential

---

## ⚙️ Machine Learning Pipeline

1. Load and prepare data
2. Build chronological team timeline
3. Create leakage-free rolling features
4. Build machine learning dataset
5. Chronological train/test split
6. Train Logistic Regression model
7. Evaluate model performance
8. Predict new games

---

## 🛠️ Technologies

- Python
- Pandas
- NumPy
- scikit-learn
- Jupyter Notebook

---

## 🚀 Future Improvements

- Elo rating features
- Rest days between games
- Home court advantage metrics
- Head-to-head history
- Strength of schedule
- Player availability and injury reports
- Hyperparameter tuning
- Multiple model comparison (Random Forest, XGBoost, etc.)
- Streamlit deployment

---

## 👤 Author

Heaven Frazier
B.S. Computer Science — University of the District of Columbia
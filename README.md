# 🏀 NBA Game Outcome Predictor

Machine learning pipeline that predicts NBA game outcomes using chronological, leakage-free feature engineering and logistic regression.

---

## 🎯 Project Goal

Build a predictive model for NBA game outcomes using only information available before each game, ensuring strict chronological feature engineering and preventing data leakage.

---

## 📊 Dataset

**Source:** [Kaggle Dataset Link](https://www.kaggle.com/datasets/eoinamoore/historical-nba-data-and-player-box-scores)

* Historical NBA games from 1946–2026  
* Model focuses on games from **2000–present**
* ~36,000+ games (regular season + playoffs)

---

## 📁 Repository Structure

```text
NBA-Game-Predictor/
│
├── data/
│   └── nba_games.csv
│
├── notebooks/
│   ├── 01_exploration_and_draft.ipynb
│   └── 02_nba_game_prediction_pipeline.ipynb
│
├── README.md
└── requirements.txt

```

---

## ⚙️ Pipeline Overview

1. Load and clean dataset
2. Build chronological team-level timeline
3. Engineer leakage-free rolling features
4. Construct machine learning dataset (home vs away features)
5. Chronological train/test split (80/20)
6. Train Logistic Regression model
7. Evaluate model performance
8. Predict individual matchups

---

## 🧠 Feature Engineering

All features are strictly leakage-free using `.shift(1)` so that only past games influence predictions.

**Engineered features:**

* 5-game rolling win percentage
* 10-game rolling win percentage
* 5-game average point differential
* 10-game average point differential

---

## 📈 Model Performance

**Model:** Logistic Regression

* **Test Accuracy:** ~62.5%

### Key Signals (Feature Importance)

* Recent 10-game win form is the strongest predictor
* Point differential contributes moderate signal
* Home vs away advantage is captured indirectly through separate team features

---

## 🧪 Example Prediction

```python
games = [
    ("Lakers", "Celtics")
]

for home, away in games:
    print(predict_matchup(home, away))
```

**Output:**

```json
{
  "home_team": "Lakers",
  "away_team": "Celtics",
  "home_prob": 0.48,
  "away_prob": 0.52,
  "predicted_winner": "Celtics"
}
```

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* scikit-learn
* Jupyter Notebook

---

## 🚀 Future Improvements

* Elo rating system
* Player-level statistics integration
* Injury and rest-day features
* Strength of schedule adjustments
* Hyperparameter tuning
* Model comparison (Random Forest, XGBoost)
* Streamlit deployment for interactive predictions

---

## 👤 Author

**Heaven Frazier** *B.S. Computer Science — University of the District of Columbia*

---

## 📝 Notes for Reviewers

* All rolling features use `.shift(1)` to prevent leakage.
* Train/test split is chronological (not random).
* Model simulates real-world prediction conditions.

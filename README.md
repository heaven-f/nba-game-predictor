# NBA Game Outcome Predictor

## Project Goal

Use historical NBA game data to analyze factors that influence game outcomes and build a predictive model to estimate game winners.

## Dataset

- Source: [Kaggle](https://www.kaggle.com/datasets/eoinamoore/historical-nba-data-and-player-box-scores)
- Date Range Used: 2000–2026
- Games Analyzed: 36,167

## Current Progress

- [x] Dataset acquired
- [x] Exploratory Data Analysis
- [x] Data Cleaning
- [x] Team Strength Feature Engineering
- [x] Recent Form Feature Engineering
- [x] Prediction Function
- [ ] Machine Learning Model Training
- [ ] Model Evaluation
- [ ] Streamlit App

## Current Model

The current prediction system uses:

- Overall team strength
- Recent form (last 10 games)

to estimate win probabilities and predict a winner.

Example:

```python
predict_game("Heat", "Bucks")
```

## Tools Used

- Python
- Pandas
- Jupyter Notebook
- VS Code

## Future Improvements

- Logistic Regression
- Elo Ratings
- Streamlit Web App
- Player Statistics
- Injury Data
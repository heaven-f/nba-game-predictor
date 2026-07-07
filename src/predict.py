import joblib
import pandas as pd


MODEL_PATH = "artifacts/model.pkl"
TEAM_TIMELINE_PATH = "artifacts/team_timeline.pkl"
FEATURE_COLS_PATH = "artifacts/feature_cols.pkl"


model = joblib.load(MODEL_PATH)
team_timeline = joblib.load(TEAM_TIMELINE_PATH)
feature_cols = joblib.load(FEATURE_COLS_PATH)


current_teams = [
    "Hawks", "Celtics", "Nets", "Hornets", "Bulls",
    "Cavaliers", "Mavericks", "Nuggets", "Pistons",
    "Warriors", "Rockets", "Pacers", "Clippers",
    "Lakers", "Grizzlies", "Heat", "Bucks",
    "Timberwolves", "Pelicans", "Knicks", "Thunder",
    "Magic", "76ers", "Suns", "Trail Blazers",
    "Kings", "Spurs", "Raptors", "Jazz", "Wizards"
]


def get_team_latest(team_name):

    temp = (
        team_timeline[
            team_timeline["team"] == team_name
        ]
        .sort_values("gameDate")
    )

    if temp.empty:
        raise ValueError(
            f"No data found for team: {team_name}"
        )

    return temp.iloc[-1]


def predict_matchup(home_team, away_team):

    if home_team == away_team:
        return {
            "error": "Teams cannot be the same"
        }


    home = get_team_latest(home_team)
    away = get_team_latest(away_team)


    input_data = pd.DataFrame([{

        "home_win_5": home["win_5"],
        "away_win_5": away["win_5"],

        "home_win_10": home["win_10"],
        "away_win_10": away["win_10"],

        "home_pd_5": home["pd_5"],
        "away_pd_5": away["pd_5"],

        "home_pd_10": home["pd_10"],
        "away_pd_10": away["pd_10"]

    }])


    input_data = input_data[feature_cols]


    probabilities = model.predict_proba(input_data)[0]


    return {
        "home_team": home_team,
        "away_team": away_team,
        "home_prob": float(probabilities[1]),
        "away_prob": float(probabilities[0]),
        "predicted_winner": (
            home_team
            if probabilities[1] > probabilities[0]
            else away_team
        )
    }
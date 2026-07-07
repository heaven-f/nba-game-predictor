import streamlit as st
from src.predict import predict_matchup, current_teams


st.set_page_config(
    page_title="NBA Game Predictor",
    page_icon="🏀",
    layout="centered"
)


# Header
st.image(
    "assets/nba_logo.png",
    width=150
)

st.title("NBA Game Outcome Predictor")

st.write(
    """
    This application uses a machine learning model trained on historical NBA
    game data to predict matchup outcomes and win probabilities.
    """
)


st.divider()


# Team selection
col1, col2 = st.columns(2)

with col1:
    home_team = st.selectbox(
        "Home Team",
        current_teams
    )

with col2:
    away_team = st.selectbox(
        "Away Team",
        current_teams,
        index=1
    )


st.divider()


if st.button("Predict Game", use_container_width=True):

    result = predict_matchup(
        home_team,
        away_team
    )

    if "error" in result:
        st.error(result["error"])

    else:

        st.subheader(
            f"Prediction: {result['predicted_winner']}"
        )


        home_prob = result["home_prob"]
        away_prob = result["away_prob"]


        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                home_team,
                f"{home_prob:.1%}"
            )

        with col2:
            st.metric(
                away_team,
                f"{away_prob:.1%}"
            )


        st.progress(
            home_prob,
            text=f"{home_team} win probability"
        )


        st.progress(
            away_prob,
            text=f"{away_team} win probability"
        )


st.divider()

st.caption(
    "For educational purposes only. Predictions are generated using a "
    "machine learning model trained on historical NBA data and should not "
    "be considered betting advice."
)
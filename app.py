import streamlit as st
from src.predict import predict_matchup, current_teams

current_teams = sorted(current_teams)

st.set_page_config(
    page_title="NBA Game Predictor",
    page_icon="🏀",
    layout="centered"
)

st.markdown(
    """
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }

        p {
            margin-bottom: 0.2rem;
        }

        hr {
            margin-top: 0.5rem;
            margin-bottom: 0.5rem;
        }

        section[data-testid="stSidebar"] p {
            font-size: 13px;
        }

        section[data-testid="stSidebar"] h2 {
            font-size: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

TEAM_LOGOS = {
    "Hawks": "https://a.espncdn.com/i/teamlogos/nba/500/atl.png",
    "Celtics": "https://a.espncdn.com/i/teamlogos/nba/500/bos.png",
    "Nets": "https://a.espncdn.com/i/teamlogos/nba/500/bkn.png",
    "Hornets": "https://a.espncdn.com/i/teamlogos/nba/500/cha.png",
    "Bulls": "https://a.espncdn.com/i/teamlogos/nba/500/chi.png",
    "Cavaliers": "https://a.espncdn.com/i/teamlogos/nba/500/cle.png",
    "Mavericks": "https://a.espncdn.com/i/teamlogos/nba/500/dal.png",
    "Nuggets": "https://a.espncdn.com/i/teamlogos/nba/500/den.png",
    "Pistons": "https://a.espncdn.com/i/teamlogos/nba/500/det.png",
    "Warriors": "https://a.espncdn.com/i/teamlogos/nba/500/gs.png",
    "Rockets": "https://a.espncdn.com/i/teamlogos/nba/500/hou.png",
    "Pacers": "https://a.espncdn.com/i/teamlogos/nba/500/ind.png",
    "Clippers": "https://a.espncdn.com/i/teamlogos/nba/500/lac.png",
    "Lakers": "https://a.espncdn.com/i/teamlogos/nba/500/lal.png",
    "Grizzlies": "https://a.espncdn.com/i/teamlogos/nba/500/mem.png",
    "Heat": "https://a.espncdn.com/i/teamlogos/nba/500/mia.png",
    "Bucks": "https://a.espncdn.com/i/teamlogos/nba/500/mil.png",
    "Timberwolves": "https://a.espncdn.com/i/teamlogos/nba/500/min.png",
    "Pelicans": "https://a.espncdn.com/i/teamlogos/nba/500/no.png",
    "Knicks": "https://a.espncdn.com/i/teamlogos/nba/500/ny.png",
    "Thunder": "https://a.espncdn.com/i/teamlogos/nba/500/okc.png",
    "Magic": "https://a.espncdn.com/i/teamlogos/nba/500/orl.png",
    "76ers": "https://a.espncdn.com/i/teamlogos/nba/500/phi.png",
    "Suns": "https://a.espncdn.com/i/teamlogos/nba/500/phx.png",
    "Trail Blazers": "https://a.espncdn.com/i/teamlogos/nba/500/por.png",
    "Kings": "https://a.espncdn.com/i/teamlogos/nba/500/sac.png",
    "Spurs": "https://a.espncdn.com/i/teamlogos/nba/500/sa.png",
    "Raptors": "https://a.espncdn.com/i/teamlogos/nba/500/tor.png",
    "Jazz": "https://a.espncdn.com/i/teamlogos/nba/500/utah.png",
    "Wizards": "https://a.espncdn.com/i/teamlogos/nba/500/wsh.png",
}

st.markdown(
    "<h1 style='text-align:center; margin-top:0px;'>NBA Game Outcome Predictor</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>Machine learning powered NBA matchup predictions</p>",
    unsafe_allow_html=True
)

st.divider()


team_col1, team_col2 = st.columns(2)

with team_col1:
    home_team = st.selectbox(
        "Home Team",
        current_teams
    )

    st.markdown(
        f"""
        <div style="text-align:center;">
            <img src="{TEAM_LOGOS[home_team]}" width="50">
            <p style="margin:0;font-weight:bold;">{home_team}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


with team_col2:
    away_team = st.selectbox(
        "Away Team",
        current_teams,
        index=1
    )

    st.markdown(
        f"""
        <div style="text-align:center;">
            <img src="{TEAM_LOGOS[away_team]}" width="50">
            <p style="margin:0;font-weight:bold;">{away_team}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

if st.button(
    "Predict Game",
    use_container_width=True
):

    result = predict_matchup(
        home_team,
        away_team
    )

    if "error" in result:

        st.error(result["error"])

    else:

        home_prob = result["home_prob"]
        away_prob = result["away_prob"]

        st.markdown(
            f"""
            <h3 style="text-align:center; margin-bottom:5px;">
                Predicted Winner: {result['predicted_winner']}
            </h3>

            <div style="
                display:flex;
                justify-content:space-between;
                font-weight:bold;
                font-size:14px;
                margin-bottom:4px;
            ">
                <span>{home_team}: {home_prob:.1%}</span>
                <span>{away_team}: {away_prob:.1%}</span>
            </div>

            <div style="
                height:16px;
                width:100%;
                background:#e74c3c;
                border-radius:10px;
                overflow:hidden;
            ">
                <div style="
                    width:{home_prob * 100}%;
                    height:100%;
                    background:#3498db;
                ">
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


with st.sidebar:

    logo_col1, logo_col2, logo_col3 = st.columns([1, 2, 1])

    with logo_col2:
        st.image(
            "assets/nba_logo_transparent.png",
            width=80
        )

    st.header("Model Information")

    st.markdown(
        """
        **Model**  
        *Logistic Regression*

        **Data**  
        *NBA games since 2000*

        **Features**  
        *Rolling team performance metrics*

        **Validation**  
        *Chronological train/test split*

        **Approach**  
        *Leakage-free feature engineering*
        """
    )

    st.divider()

    st.metric(
        "Test Accuracy",
        "62.5%"
    )

    st.caption(
        "Predictions are generated from a machine learning model trained on "
        "historical NBA data. For educational purposes only."
    )
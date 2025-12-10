import streamlit as st
import pickle
import numpy as np
import pandas as pd

with open("knn_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("NBA Win Percentage Prediction App")

team_name = st.selectbox("Team Name", [
    "Wizards", "Cavaliers", "Heat", "Celtics", "Lakers"
])

team_city = st.selectbox("Team City", [
    "Washington", "Cleveland", "Miami", "Boston", "Los Angeles"
])

home_team = st.selectbox("Home Team", [
    "Wizards", "Cavaliers", "Heat", "Celtics", "Lakers"
])

fgm = int(st.number_input("FGM", value=0))
fga = int(st.number_input("FGA", value=0))
fg3m = int(st.number_input("FG3M", value=0))
fg3a = int(st.number_input("FG3A", value=0))
ftm = int(st.number_input("FTM", value=0))
fta = int(st.number_input("FTA", value=0))
REB = int(st.number_input("REB", value=0))
PTS = int(st.number_input("PTS", value=0))


if st.button("Predict WIN %"):

    input_df = pd.DataFrame([{
        "TEAM_NAME": team_name,
        "TEAM_CITY": team_city,
        "HOME_TEAM": home_team,
        "FGM": fgm,
        "FGA": fga,
        "FG3M": fg3m,
        "FG3A": fg3a,
        "FTM": ftm,
        "FTA": fta,
        "REB":REB,
        "PTS":PTS
    }])

    result = model.predict(input_df)[0]

    st.success(f"Predicted WIN % : {result:.2f}")
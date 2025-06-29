
import streamlit as st
from datetime import datetime
import requests

# === CONFIGURATION ===
API_KEY_FD = "e466a37640c044bfbeaceaef804ff773"
API_KEY_RAPIDAPI = "0053fc492dmsh0aa885662e3df2cp1fbaa2jsnde9ef0e4e8a2"

# Page d'accueil
st.set_page_config(page_title="SMART'bet ⚽", layout="centered")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Soccer_ball_animated.svg/240px-Soccer_ball_animated.svg.png", width=80)
st.markdown("<h1 style='text-align: center; color: #007acc;'>SMART'bet - Analyse Sportive</h1>", unsafe_allow_html=True)

with st.expander("ℹ️ À propos de cette application"):
    st.write("""
    **SMART'bet** est une application d'analyse de matchs pour t'aider à réussir tes paris sportifs.  
    Elle utilise une estimation de probabilité combinée à la méthode de mise *Kelly*.  
    Tu peux choisir :
    - Les **matchs du jour**
    - Les **matchs en direct** (à partir de 60 minutes)
    - Le ou les **types de paris** à analyser (1X2, Double Chance, Over/Under 2.5, BTTS)

    Tu recevras :
    - Une estimation de la **probabilité**
    - La **mise conseillée**
    - Des **alertes** en cas d'opportunité forte (🎯)

    👉 Commence ci-dessous 👇
    """)

if st.button("🚀 Commencer l’analyse"):
    st.switch_page("smartbet_app_complet.py")

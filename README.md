import streamlit as st
from datetime import datetime
import requests

# === CONFIGURATION ===
# Note: En production, utilisez st.secrets pour gérer les clés API
API_KEY_FD = st.secrets.get("API_KEY_FD", "e466a37640c044bfbeaceaef804ff773")
API_KEY_RAPIDAPI = st.secrets.get("API_KEY_RAPIDAPI", "0053fc492dmsh0aa885662e3df2cp1fbaa2jsnde9ef0e4e8a2")

# === STREAMLIT UI CONFIG ===
st.set_page_config(
    page_title="SMART'bet ⚽ - Analyse Sportive Intelligente",
    page_icon="⚽",
    layout="centered",
    initial_sidebar_state="expanded"
)

# === HEADER SECTION ===
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Soccer_ball_animated.svg/240px-Soccer_ball_animated.svg.png",
        width=100
    )
    st.markdown(
        """
        <h1 style='text-align: center; color: #007acc; margin-bottom: 0;'>
            SMART'bet <span style='font-size: 0.8em;'>⚽</span>
        </h1>
        <p style='text-align: center; color: #666; margin-top: 0;'>
            Analyse Sportive Intelligente pour Paris Gagnants
        </p>
        """,
        unsafe_allow_html=True
    )

# === ABOUT SECTION ===
with st.expander("ℹ️ À propos de SMART'bet", expanded=True):
    st.write("""
    **SMART'bet** est une application d'analyse avancée de matchs conçue pour optimiser tes paris sportifs.  
    Elle combine :
    
    - 📊 **Analyse statistique** des performances des équipes
    - 🧮 **Modèles prédictifs** basés sur des données historiques
    - 💰 **Gestion de bankroll** avec la méthode scientifique de Kelly
    
    ### Fonctionnalités :
    """)
    
    cols = st.columns(2)
    with cols[0]:
        st.markdown("""
        - 🗓️ **Matchs du jour** analysés
        - ⚡ **Matchs en direct** (60+ minutes)
        - 🔍 **Multiples types de paris** :
            - 1X2
            - Double Chance
            - Over/Under 2.5
            - BTTS (Buts des deux côtés)
        """)
    
    with cols[1]:
        st.markdown("""
        - 📈 **Probabilités estimées**
        - 💡 **Mise optimale conseillée**
        - 🎯 **Alertes opportunités** (valeur détectée)
        - 🛡️ **Gestion des risques**
        """)
    
    st.markdown("""
    ### Comment ça marche ?
    1. Sélectionnez les matchs à analyser
    2. Choisissez vos types de paris préférés
    3. Recevez les analyses et recommandations
    4. Appliquez la stratégie de mise conseillée
    
    👇 **Commencez dès maintenant ci-dessous** 👇
    """)

# === MAIN ACTION ===
primary_color = "#007acc"
st.markdown(f"""
    <style>
        div.stButton > button:first-child {{
            background-color: {primary_color};
            color: white;
            font-weight: bold;
            border: none;
            width: 100%;
            padding: 0.5rem;
            border-radius: 0.5rem;
            transition: all 0.3s ease;
        }}
        div.stButton > button:first-child:hover {{
            background-color: #005f99;
            transform: scale(1.02);
        }}
    </style>
""", unsafe_allow_html=True)

if st.button("🚀 Commencer l'analyse SMART", use_container_width=True):
    st.switch_page("pages/smartbet_app_complet.py")

# === FOOTER ===
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.9em;'>
    <p>ℹ️ Les paris sportifs comportent des risques. Jouez de manière responsable.</p>
    <p>© 2023 SMART'bet - Tous droits réservés - Version 1.1.0</p>
</div>
""", unsafe_allow_html=True)

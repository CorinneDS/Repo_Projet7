import pandas as pd
import numpy as np
from joblib import load
import streamlit as st

st.set_page_config(page_title="Dashboard", page_icon=":bar_chart:",layout="wide")
st.title(":bar_chart: Dashboard")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

# Charger les données
data = pd.read_csv('/Users/corinnedumairir/Documents/Data Scientist/PYTHON/API_Projet_7/X_test50_withIndex.csv')

# Convertir les valeurs en entiers
data['SK_ID_CURR'] = data['SK_ID_CURR'].astype(int)

# Charger le meilleur modele sauvergarde
best_model = load('/Users/corinnedumairir/Documents/Data Scientist/PYTHON/API_Projet_7/model_best_LGBM.sav')

# Selection du client sur la gauche
st.sidebar.header("Sélection :")
candidat = st.sidebar.selectbox("Choisir le candicat au prêt :", data['SK_ID_CURR'].unique())

# Calcul de la prediction de non remboursement
row_to_send = data[data['SK_ID_CURR']==candidat]

df = row_to_send.drop(columns=['SK_ID_CURR'])

prediction = best_model.predict_proba(df)[:,1]*100
prediction = np.round(prediction, 2)

prediction_value = prediction[0]

st.metric(label="Probabilité de non remboursement :", value=f"{prediction_value} %")
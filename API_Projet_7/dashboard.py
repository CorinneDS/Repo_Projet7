#import pandas as pd
#from joblib import load
import streamlit as st

#st.set_page_config(page_title="Dashboard!!!", page_icon=":bar_chart:",layout="wide")
st.title("Corinne")

# Charger les données
#data = pd.read_csv('/Users/corinnedumairir/Documents/Data Scientist/PYTHON/API_Projet_7/X_test50_withIndex.csv')
#data_woIndex = data.drop(columns=['SK_ID_CURR'])

# Charger le meilleur modele sauvergarde
#best_model = load('/Users/corinnedumairir/Documents/Data Scientist/PYTHON/API_Projet_7/model_best_LGBM.sav')

#row_to_send = data_woIndex.iloc[20].to_dict()
#df = pd.DataFrame([row_to_send])

#prediction = best_model.predict_proba(df)[:,1]

#print(prediction)
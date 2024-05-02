import pandas as pd
import numpy as np
import json
from joblib import load
import requests
import shap
import streamlit as st
import matplotlib.pyplot as plt

# Titres et logo
def render_title() -> None:
    st.set_page_config(page_title="Dashboard : scoring des candidats à un prêt", page_icon=":bar_chart:",layout="wide")

    col1, col2, col3 = st.columns((3))
    with col1:
        st.title(":bar_chart: Dashboard")

    with col3:
        st.image('Logo_projet7.jpg', width=150)

# Texte de presentation
def text_pres() -> None:
    st.text('Texte de presentation du dashboard à rediger une fois celui-ci terminé.')

# Chargement les données
def load_data():
    data = pd.read_csv('/Users/corinnedumairir/Documents/Data Scientist/PYTHON/API_Projet_7/X_test50_withIndex.csv')

    # Convertir les ID clients en entiers
    data['SK_ID_CURR'] = data['SK_ID_CURR'].astype(int)
    return data

# Selection du candidat dans liste deroulante et formattage attendu par API
def select_candidat():
    st.sidebar.header("Sélection :")
    candidat = st.sidebar.selectbox("Choisir le candidat au prêt :", data['SK_ID_CURR'].unique())
    df = data.loc[data['SK_ID_CURR']==candidat]
    df = df.drop(columns=['SK_ID_CURR'])
    df_dict = df.to_dict(orient='records')[0]
    return df_dict

# Appel a l'API pour obtenir la prédiction
def prediction(row):
    prediction_url = 'http://127.0.0.1:5000/prediction'
    # Envoyer une requête POST à l'API avec les données JSON dans le corps de la requête
    response = requests.post(prediction_url, json=row)
    response_data = json.loads(response.text)
    prediction_values = response_data["prediction"]
    return prediction_values

# Affichage de la probabilite de remboursement
def affich_predict_proba(response):
    prediction = np.round(response[0][0]*100, 2)
    st.metric(label="Probabilité de remboursement :", value=f"{prediction} %")

# Affichage d'un pie chart
def pie_chart(response):
    labels = 'Remboursement', 'Non-remboursement'
    sizes = [response[0][0],response[0][1]]

    fig1, ax1 = plt.subplots(figsize=(10, 10))
    pie_wedge_collection, text_props, autotexts = ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                                   startangle=90, textprops={'fontsize': 20}) 
    ax1.axis('equal')  # Assure un rapport d'aspect égal pour dessiner un cercle.
    ax1.set_title('Répartition des prédictions', fontsize=22)  # Ajoute un titre et ajuste la taille
    legend = ax1.legend(fontsize=20, bbox_to_anchor=(1, 0.5))  # Déplace la légende à l'extérieur et ajuste la taille
    legend.set_title('Légende', prop={'size': 20}) #title='Légende',

    # Ajuste la taille des labels
    for label in ax1.get_xticklabels() + ax1.get_yticklabels():
        label.set_fontsize(22)

    st.pyplot(fig1)

if __name__ == "__main__":
    render_title()
    text_pres()
    data = load_data()
    row_to_send = select_candidat()
    response = prediction(row_to_send)
    #st.write("Response pour 0:" , response[0][0])
    #st.write("Response pour 1:" , response[0][1])
    #st.write("Response finale:" , response[1])
    col1, col2, col3, col4 = st.columns((4))
    with col1:
        pie_chart(response)

    with col2:
        affich_predict_proba(response)











#prediction = best_model.predict_proba(row_to_send)[:,1]*100
#prediction = np.round(prediction, 2)

#prediction_value = prediction[0]

#st.metric(label="Probabilité de non remboursement :", value=f"{prediction_value} %")

# Expliquez les prédictions du meilleur modele
#explainer = shap.Explainer(best_model)
#data_woIndex = data.drop(columns=['SK_ID_CURR'])
#shap_values = explainer(data_woIndex)

# Calculer la moyenne absolue des SHAP values pour chaque variable
#mean_shap_values = np.abs(shap_values.values).mean(axis=0)

# Recuperer les noms des variables
#feature_names = data_woIndex.columns

# Trier par valeur de SHAP values
#sorted_indices = np.argsort(-mean_shap_values)
#sorted_indices = sorted_indices[::-1]  # Invert the order to have the largest values first
#sorted_feature_names = feature_names[sorted_indices]
#sorted_mean_shap_values = mean_shap_values[sorted_indices]

# Preparer le bar chart horizontal
#plt.figure(figsize=(4, 2))
#plt.barh(sorted_feature_names[len(sorted_feature_names)-20:], sorted_mean_shap_values[len(sorted_feature_names)-20:], height=0.7, edgecolor='black', linewidth=0.1)

# Ajuster la largeur de la bordure autour du graphique
#for spine in plt.gca().spines.values():
#    spine.set_linewidth(0.5)

#plt.xlabel('Valeur absolue des SHAP Values', fontsize=5)  # Ajuster la taille de la police pour l'axe des x
#plt.ylabel('Variables', fontsize=5)  # Ajuster la taille de la police pour l'axe des y
#plt.title('Importance des variables basée sur la SHAP value', fontsize=6)  # Ajuster la taille de la police pour le titre
#plt.yticks(fontsize=4)
#plt.xticks(fontsize=4)
#plt.tight_layout(pad=0.1)

# Afficher le bar chart horizontal
#col1, col2 = st.columns((1,2))
#st.set_option('deprecation.showPyplotGlobalUse', False)
#with col1:
#    st.pyplot()

#with col2:
#    st.write(df)

# Créer un graphique shap.force_plot
#shap.initjs()
#force_plot_html = shap.force_plot(shap_values.base_values[0], shap_values.values[0], df).html()

# Convertir le graphique en HTML
#force_plot_html = force_plot.html()

# Afficher le HTML dans Streamlit

    #st.write(force_plot_html, unsafe_allow_html=True)  # Pour HTML


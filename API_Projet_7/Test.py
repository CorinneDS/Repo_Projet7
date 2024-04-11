import requests
import pandas as pd
import json

# Charger les données
data = pd.read_csv('/Users/corinnedumairir/Documents/Data Scientist/PYTHON/API_Projet_7/X_test_first50.csv')

# Sélectionner une seule ligne à envoyer à l'API (par exemple, la première ligne)
row_to_send = data.iloc[24].to_dict()

# URL de l'API
api_url = 'http://127.0.0.1:5000/display_row'

# Envoyer la ligne à l'API avec l'en-tête Content-Type défini sur 'application/json'
response = requests.post(api_url, json=json.dumps(row_to_send), headers={'Content-Type': 'application/json'})

# Afficher la réponse de l'API
print("Réponse de l'API :", response.json())

# URL de l'API pour la prédiction
prediction_url = 'http://127.0.0.1:5000/prediction'

# Envoyer une requête POST à l'API avec les données JSON dans le corps de la requête
response = requests.post(prediction_url, json=row_to_send)

# Afficher la réponse de l'API
print("Réponse de l'API pour la prédiction :", response.text)

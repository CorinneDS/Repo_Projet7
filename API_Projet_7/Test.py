import requests
import pandas as pd

# Charger les données
data = pd.read_csv('/Users/corinnedumairir/Documents/Data Scientist/PYTHON/API_Projet_7/X_test50.csv')

# Sélectionner une seule ligne à envoyer à l'API (par exemple, la première ligne)
row_to_send = data.iloc[0].to_dict()

# URL de l'API
api_url = 'http://127.0.0.1:5000/display_row'

# Envoyer la ligne à l'API
response = requests.post(api_url, json=row_to_send)

# Afficher la réponse de l'API
print("Réponse de l'API :", response.json())

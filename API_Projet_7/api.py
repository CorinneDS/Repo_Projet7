from flask import Flask, request, jsonify
from joblib import load
import pandas as pd

app = Flask(__name__)

# Route pour afficher la dernière ligne reçue dans le navigateur
@app.route('/test', methods=['POST'])
def index():

    last_row_received = request.get_json()

    print("TYPE: ",type(last_row_received))

    # Construire une chaîne de caractères représentant la dernière ligne
    last_row_str = ' // '.join([f"{key}: {value}" for key, value in last_row_received.items()])

    print(last_row_str)

    # Afficher la dernière ligne dans le navigateur
    return jsonify(f"<h1>Dernière ligne reçue :</h1><p>{last_row_str}</p>")

# Route pour afficher le resultat de la prediction
@app.route('/prediction', methods=['POST'])
def prediction():
    # Récupérer la ligne envoyée par le client depuis la requête JSON
    row_data = request.get_json()

    # Charger le modèle depuis le fichier Joblib
    best_model = load('/Users/corinnedumairir/Documents/Data Scientist/PYTHON/API_Projet_7/model_best_LGBM.sav')

    # Vérifier si row_data est un dictionnaire
    if isinstance(row_data, dict):
        # Convertir le dictionnaire en DataFrame Pandas
        df = pd.DataFrame([row_data])
    
        prediction = best_model.predict(df)

        # Retourner le résultat de la prédiction
        return jsonify({'prediction': prediction.tolist()})
    else:
        # Retourner un message d'erreur si le format n'est pas correct
        return jsonify({'error': 'Le format des données envoyées est incorrect. Assurez-vous d\'envoyer un objet JSON contenant les données de la ligne à prédire.'}), 400

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Initialiser la variable globale pour stocker la dernière ligne reçue
last_row_received = {}

# Route pour afficher une ligne spécifique reçue du client
@app.route('/display_row', methods=['POST'])
def display_row():
    # Récupérer la ligne envoyée par le client depuis la requête JSON
    row_data = request.get_json()

    # Stocker la dernière ligne reçue dans la variable globale
    global last_row_received
    last_row_received = row_data

    # Retourner la même ligne au client
    return jsonify(row_data)

# Route pour afficher la dernière ligne reçue dans le navigateur
@app.route('/')
def index():
    global last_row_received

    # Construire une chaîne de caractères représentant la dernière ligne
    last_row_str = ' // '.join([f"{key}: {value}" for key, value in last_row_received.items()])

    # Afficher la dernière ligne dans le navigateur
    return f"<h1>Dernière ligne reçue :</h1><p>{last_row_str}</p>"

if __name__ == '__main__':
    app.run(debug=True)

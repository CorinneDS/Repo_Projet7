from flask import Flask, request, jsonify

app = Flask(__name__)

# Route pour afficher une ligne spécifique reçue du client
@app.route('/display_row', methods=['POST'])
def display_row():
    # Récupérer la ligne envoyée par le client depuis la requête JSON
    row_data = request.get_json()

    # Retourner la même ligne au client
    return jsonify(row_data)

if __name__ == '__main__':
    app.run(debug=True)
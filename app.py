import os
from flask import Flask, send_from_directory, jsonify, request

app = Flask(__name__, static_folder='.')

# Route pour afficher ton interface (index.html)
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Route pour tester ton algorithme
@app.route('/generate', methods=['POST'])
def generate():
    return jsonify({"status": "Success", "message": "L'algorithme OmniScribe est prêt !"})

if __name__ == "__main__":
    # Render utilise la variable d'environnement PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

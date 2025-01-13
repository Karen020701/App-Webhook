from flask import Flask, jsonify
from flask_cors import CORS  # Importa CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

@app.route('/AppWebhook', methods=['GET'])
def webhook():
    return jsonify({"message": "Hola Mundo con Webhook en lenguaje Python"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
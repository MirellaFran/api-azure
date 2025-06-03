import os
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

@app.route('/incidencia', methods=['POST'])
def recibir_incidencia():
    data = request.get_json()
    app.logger.info(f"📩 Datos recibidos: {data}")
    print(f"📩 Datos recibidos (print): {data}")  # Para debug extra
    return jsonify({"mensaje": "Correo recibido correctamente"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

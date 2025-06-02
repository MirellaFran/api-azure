import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/incidencia', methods=['POST'])
def recibir_incidencia():
    app.logger.info("🔔 Recibí un POST")
    app.logger.info(f"🔥 Raw data: {request.data}")
    app.logger.info(f"📬 Headers: {dict(request.headers)}")
    data = request.get_json(silent=True)
    app.logger.info(f"📩 Datos JSON: {data}")
    return jsonify({"mensaje": "Correo recibido correctamente"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

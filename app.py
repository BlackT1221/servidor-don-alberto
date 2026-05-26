from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route('/api/repuestos')
def get_repuestos():
	return jsonify({
	  "status": "online",
	  "servidor": "Ubuntu de Martinez:",
	  "hora_servidor": str(datetime.datetime.now()),
	  "inventario": ["Bujias de Iridio", "Filtro de aceite", "Aceite motul 7100"]
	})

if __name__ == "__main__":
	app.run()

from flask import Flask, request, render_template, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# Cargar el modelo
model = joblib.load('modelo.pkl')

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener datos del formulario
        data = request.form.to_dict(flat=True)
        high = float(data['high'])
        low = float(data['low'])
        gdx_open = float(data['gdx_open'])
        close = float(data['close'])
        eg_low = float(data['eg_low'])

        # Crear un array numpy con los datos
        input_data = np.array([[high, low, gdx_open, close, eg_low]])

        # Realizar la predicción
        prediction = model.predict(input_data)

        # Convertir la predicción a una respuesta legible
        result = prediction[0]

        return jsonify({'prediction': result})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

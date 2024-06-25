from flask import Flask, request, render_template, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# Cargar el modelo y el scaler
model = joblib.load('modelo.pkl')

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener datos del formulario
        data = request.form.to_dict(flat=True)
        age = float(data['age'])
        cement = float(data['cement'])
        superplasticizer = float(data['superplasticizer'])
        fineaggregate = float(data['fineaggregate'])
        flyash = float(data['flyash'])

        # Crear un array numpy con los datos
        input_data = np.array([[age, cement, superplasticizer, fineaggregate, flyash]])

        # Estandarizar los datos

        # Realizar la predicción
        prediction = model.predict(input_data)

        # Convertir la predicción a una respuesta legible
        result = prediction[0]

        return jsonify({'prediction': result})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

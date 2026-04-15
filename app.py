from flask import Flask,request, url_for, redirect, render_template, jsonify
from pycaret.regression import load_model, predict_model
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

model = load_model('deployment_20260410')
cols = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/health', methods=["GET"])
def health():
    return "HEALTH OK"

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns = cols)
    prediction = predict_model(model, data=data_unseen, round = 0)
    print(prediction)
    prediction = int(prediction.loc[0, 'prediction_label'])
    return render_template('home.html',pred='Expected Bill will be ${} anually'.format(prediction))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    data_unseen = pd.DataFrame([data])
    prediction = predict_model(model, data=data_unseen)
    prediction = int(prediction.loc[0, 'prediction_label'])
    return jsonify({'output': prediction})

# Al poner el host en 0.0.0.0, le estás permitiendo a Flask "escuchar" las peticiones que vienen desde fuera del contenedor
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)

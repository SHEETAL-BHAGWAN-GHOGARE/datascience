from flask import Flask,render_template,request,jsonify
import pickle
import numpy as np
import pandas as pd
import db


with open('model.pkl','rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('iris_data.html')

@app.route('/iris',methods=['POST'])
def predict():
    SepalLengthCm = float(request.form['sl'])
    SepalWidthCm = float(request.form['sw'])
    PetalLengthCm = float(request.form['pl'])
    PetalWidthCm = float(request.form['pw'])

    data = np.array([SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm],ndmin=2)


    result = model.predict(data)

    print(result)


    if result[0] == 0:
        pred = 'Iris-setosa'

    if result[0] == 1:
        pred = 'Iris-versicolor'

    if result[0] == 2:
        pred = 'Iris-virginica'
       
    return jsonify(pred)


    # 5.1	3.5	1.4	0.2	
@app.route('/login')
def login():
    """ Login logic"""
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
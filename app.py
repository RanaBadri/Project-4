from flask import Flask, render_template, request, jsonify, make_response
import os
import pandas as pd
import json
import requests
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import pickle

app = Flask(__name__)



engine = create_engine(f'postgresql://postgres:postgres@localhost:5432/whitewine_db')
data= pd.read_sql("select * FROM whitewine", con=engine) 

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/analysis")
def actors():
    return render_template("analysis.html")

@app.route("/model" , methods=["POST"])
def model():

    volatile_acidity = float(request.form["volatile_acidity"])
    #alcohol = float(request.form["alcohol"])

    alcohol = request.form["alcohol"]
    if alcohol == "":
        alcohol = 68000
    alcohol = float(alcohol)

    chlorides = request.form["chlorides"]
    if chlorides == "":
        chlorides = 6
    chlorides = float(chlorides)

    total_sulfur_dioxide = request.form["total_sulfur_dioxide"]
    if total_sulfur_dioxide == "":
        total_sulfur_dioxide = 36000

    residual_sugar = request.form["residual_sugar"]
    if residual_sugar == "":
        residual_sugar = 36000
        
    # prediction = 0

    X = [[volatile_acidity, residual_sugar, chlorides, total_sulfur_dioxide, alcohol]]

    print(X)

    filename = 'static/winequality.sav'
    loaded_model = pickle.load(open(filename, 'rb'))

    filename1 = 'static/Scaler.sav'
    loaded_scaler = pickle.load(open(filename1, 'rb'))
    
    X=loaded_scaler.transform(X)

    prediction = loaded_model.predict(X)[0]

    #prediction = "{0:,.2f}".format(prediction)

    print(prediction)
    
    if prediction==0:
        prediction="bad"
    
    if prediction==1:
        prediction="good"
    print(prediction)
    
    return render_template("analysis.html", prediction = prediction)


@app.route('/table')
def maketable():
    table = data.to_html() 
    return render_template('table.html', table = table)
  


if __name__ == '__main__':
    app.run(debug = True)

    model = pickle.load("Resources/winequality.pkl")
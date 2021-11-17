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

# @app.route("/")
# def bubble():
#     return render_template()


# @app.route('/plot')
# def getData():
    
#     return yeargroupedcrime.to_json()


# @app.route('/plot2')
# def getData2():
#     return regiongrouped.to_json()

# @app.route('/plot3')
# @app.route('/plot3/<year>')
# def getData3(year=None):
    
#     return newDF.tail(50).to_json(orient='values')

@app.route('/table')
def maketable():
    table = data.to_html() 
    return render_template('table.html', table = table)
  


if __name__ == '__main__':
    app.run(debug = True)

    model = pickle.load("Resources/winequality.pkl")
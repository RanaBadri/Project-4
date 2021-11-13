from flask import Flask, render_template, request, jsonify, make_response
import os
import pandas as pd
import json
import requests


app = Flask(__name__)



filepath = os.path.join("Resources", "Violent_and_Property_Crimes_Over_Time_data.csv")
data = pd.read_csv(filepath)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/bubble")
def bubble():
    return render_template('googleChart.html')


@app.route('/plot')
def getData():
    yeargroupedcrime = data.groupby("Year")[["Property crime rate", "Violent Crime rate"]].mean()
    #yeargroupedcrime = yeargroupedcrime.reset_index()
    return yeargroupedcrime.to_json()


@app.route('/plot2')
def getData2():
    regiongrouped = data.groupby("Region")["Violent Crime rate"].mean()
    return regiongrouped.to_json()

@app.route('/plot3')
@app.route('/plot3/<year>')
def getData3(year=None):
    if year:
        yeardata = data.loc[data["Year"] == int(year)]
    else:
        yeardata = data
    newDF = pd.DataFrame({"ID":yeardata["State"] + "-" + yeardata["Year"].astype(str), "Violent Crime":yeardata["Violent Crime rate"], "Property Crime": yeardata["Property crime rate"], "Region":yeardata["Region"], "Population":yeardata["Population"]})
    return newDF.tail(50).to_json(orient='values')

@app.route('/table')
def maketable():
    table = data.to_html() 
    return render_template('table.html', table = table)
  


if __name__ == '__main__':
    app.run(debug = True)
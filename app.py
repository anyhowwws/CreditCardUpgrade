#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 14:59:06 2022

@author: hows
"""
from flask import Flask, request, render_template

app = Flask(__name__)

from joblib import load

# model = joblib.load("/Users/hows/Documents/CART.joblib")
# pred = model.predict([[20,1]])

# model2 = joblib.load("/Users/hows/Documents/RandomForest.joblib")
# pred2 = model2.predict([[20,1]])

# model3 = joblib.load("/Users/hows/Documents/GB.joblib")
# pred3 = model3.predict([[20,1]])

@app.route("/", methods=["GET","POST"])
def index():
    if request.method =="POST":
        
        purchase= request.form.get("Purchases")
        card = request.form.get("Supplementary card")
        # model = load("/Users/hows/Documents/CART.joblib")
        # pred = model.predict([[float(rates)]])
        # PRED="$"+str(round(pred[0][0],2))
        
        model1 = joblib.load("CART.joblib")
        model2 = joblib.load("RandomForest.joblib")
        model3 = joblib.load("GB.joblib")
        
        pred1 = model1.predict([[purchase,card]])
        pred2 = model2.predict([[purchase,card]])
        pred3 = model3.predict([[purchase,card]])

        # return(render_template("/Users/hows/Documents/week2/templates/index.html",result="1",result2="2",result3="3"))
        return(render_template("index.html",result=pred1,result2=pred2,result3=pred3))
            
    else:
        # defaultRate=""
        # defaultResults = ""
        # defaultResponse = "Enter an amount above for an estimation!"
        # return(render_template("/Users/hows/Documents/week2/templates/index.html",result="1",result2="2",result3="3"))
        return(render_template("index.html",result="-",result2="-",result3="-"))


if __name__=="__main__": #required if not in DEV env
    # app.run(host="127.0.0.1",port=int("1415"))
    app.run()

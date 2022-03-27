#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 14:59:06 2022

@author: hows
"""
from flask import Flask, request, render_template

app = Flask(__name__)

import joblib
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
        Purchase=request.form.get("Purchases")
        Card=request.form.get("Supplementary card")
        purchase = float(Purchase)
        card = float(Card)
        
        model1 = load("CART")
        model2 = load("RandomForest")
        model3 = load("GB")
        
        pred1 = model1.predict([[purchase,card]])
        pred2 = model2.predict([[purchase,card]])
        pred3 = model3.predict([[purchase,card]])
        Result1=str(pred1[0][0])
        Results2=str(pred2[0][0])
        Result3=str(pred3[0][0])

        # return(render_template("/Users/hows/Documents/week2/templates/index.html",result="1",result2="2",result3="3"))
        return(render_template("index.html",result=Result1,result2=Result2,result3=Result3))
            
    else:
        # defaultRate=""
        # defaultResults = ""
        # defaultResponse = "Enter an amount above for an estimation!"
        # return(render_template("/Users/hows/Documents/week2/templates/index.html",result="1",result2="2",result3="3"))
        return(render_template("index.html",result="Enter your values above to start!",result2="",result3=""))


if __name__=="__main__": #required if not in DEV env
    # app.run(host="127.0.0.1",port=int("1415"))
    app.run()

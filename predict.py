# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 22:30:00 2021

@author: VISHAL
"""



#%%

#importing libraries:
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

#%%

app=Flask(__name__)

#%%

model=pickle.load(open('decision_tree.pkl','rb'))

#%%

@app.route('/')
def home():
    return render_template('predict.html')
#%%
rain_or_snow={0:"Rain",1:"Snow"} 

condensation={0:"Dry",1:"Fog",2:"Frost",3:"Mist"}
                
output={0:"Breezy",1:"Breezy and Dry",2:"Breezy and Foggy",3:"Breezy and Mostly Cloudy",4:"Breezy and Overcast",
           5:"Breezy and Partly Cloudy",6:"Clear",7:"Dangerously Windy and Partly Cloudy",8:"Drizzle",9:"Dry",
           10:"Dry and Mostly Cloudy",11:"Dry and Partly Cloudy",12:"Foggy",13:"Humid and Mostly Cloudy",
           14:"Humid and Overcast",15:"Humid and Partly Cloudy",16:"Light Rain",17:"Mostly Cloudy",18:"Overcast",
           19:"Partly Cloudy",20:"Windy",21:"Windy and Dry",22:"Windy and Foggy",23:"Windy and Mostly Cloudy",
           24:"Windy and Overcast",25:"Windy and Partly Cloudy"}


#%%
    
@app.route("/Predict", methods=['POST'])
def Predict():
    int_features=[x for x in request.form.values()]
    final_features=[np.array(int_features)]
    prediction=model.predict(final_features)
        
    data2=request.form["Rain_OR_SNOW"]
    data3=request.form["Temperature (C)"]
    data4=request.form["Apparent Temperature (C)"]
    data5=request.form["Humidity"]
    data6=request.form["Wind Speed (km/h)"]
    data7=request.form["Wind Bearing (degrees)"]
    data8=request.form["Visibility (km)"]
    data9=request.form["Pressure (millibars)"]
    data10=request.form["Condensation"]
    data11=request.form["Solar irradiance intensity"]
        
    #create original output dict
    output_dict= dict()
    output_dict['Rain_OR_SNOW']=rain_or_snow[int(data2)]
    output_dict['Temperature (C)']=data3
    output_dict['Apparent Temperature (C)']=data4
    output_dict['Humidity']=data5
    output_dict['Wind Speed (km/h)']=data6
    output_dict['Wind Bearing (degrees)']=data7
    output_dict['Visibility (km)']=data8
    output_dict['Pressure (millibars)']=data9
    output_dict['Condensation']=condensation[int(data10)]
    output_dict['Solar irradiance intensity']=data11
        
    
    return render_template('predictresult.html',original_input=output_dict,prediction_text=output[int(prediction)])
#%%
        
if __name__=='__main__':
    app.run(debug=True)
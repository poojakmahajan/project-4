from flask import Flask, render_template, Response
from flask import Flask,render_template,request
from sklearn.preprocessing import StandardScaler 
import sys
import joblib
import numpy as np
import requests
import pandas as pd
from sqlalchemy import create_engine
import logging
app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)



@app.route('/')
def home():
    return render_template('index.html',text="Hi")


@app.route('/predictweather', methods = ['POST'])
def predictweather():

    if request.method == 'POST':
        loaded_rf = joblib.load("./random_forest.joblib")
        form_data = request.form
        l0 = list(form_data.values())
        l_data = l0
        selectlist = [l0[1],l0[2],l0[3]]
        print(selectlist)
        l0 = [float(i) for i in selectlist]
        l1 = np.array(l0)
        l1 = np.reshape(l1,(1 ,-1))
        #scaler = StandardScaler().fit(l1)
        scaler = joblib.load("./standardScaler.joblib")
        X_scaled = scaler.transform(l1)
        print(X_scaled)
        #predictedweather = 0 
        predictedweather = loaded_rf.predict(X_scaled)

        print(predictedweather)
        value ='NA'
        if predictedweather == 0:
            value = 'The weather in Valencia is clear. It is good day for outdoor activities!'
        elif predictedweather== 1:
            value = 'The weather in Valencia is cloudy. Plan accordingly.'
        elif predictedweather== 2:
            value = 'The weather in Valencia is going to drizzle. Carry an umbrella!'
        elif predictedweather== 3:
            value = 'The weather in Valencia is foggy. Drive carefully!'
        elif predictedweather== 4:
            value = 'The weather in Valencia is hazy. Drive carefully!'
        elif predictedweather== 5:
            value = 'The weather in Valencia is misty. Carry an umbrella!'
        elif predictedweather== 6:
            value = 'The weather in Valencia is rainy.Carry an umbrella!'
        elif predictedweather== 7:
            value = 'The weather in Valencia is smokey. Wear a mask!'
        elif predictedweather== 8:
            value = 'The weather in Valencia has thunderstorm. Stay indoors!'
        else : 'NA'
        return render_template('index.html',form_data = value,Tdate = l_data[0] ,temp = l_data[1] ,pressure = l_data[2],humidity = l_data[3] ,windspeed = l_data[4],winddeg = l_data[5]  )
       # return render_template('index.html',form_data = form_data)
                
 
if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from WaterQualityPredictor.pipeline.prediction import PredictionPipeline

app = Flask(__name__) # Initializing a flask app

@app.route('/', methods=['GET']) # route to display the home page
def homepage():
    return render_template("index.html")

@app.route('/train', methods=['GET']) # ROute to train the pipeline
def training():
    os.system('python main.py') # Excute this command
    return 'Training Sucessful!'

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            ph =float(request.form['ph'])
            Hardness =float(request.form['Hardness'])
            Solids =float(request.form['Solids'])
            Chloramines =float(request.form['Chloramines'])
            Sulfate =float(request.form['Sulfate'])
            Conductivity =float(request.form['Conductivity'])
            Organic_carbon =float(request.form['Organic_carbon'])
            Trihalomethanes =float(request.form['Trihalomethanes'])
            Turbidity =float(request.form['Turbidity'])
       
         
            data = [ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity]
            data = np.array(data).reshape(1, 9)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)

            if predict == 0:
                predict = 'This water sample is Potable'
            elif predict == 1:
                predict = 'This water sample is not Potable'

            return render_template('results.html', prediction = str(predict))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

# data = [3,3,3,3,3,3,3,3,3]
# data = np.array(data).reshape(1, 9)

# obj = PredictionPipeline()
# predict = obj.predict(data)
# print(predict)
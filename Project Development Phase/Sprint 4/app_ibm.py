import numpy as np
import pickle
from flask import request, render_template, Flask, redirect, url_for
from flask_cors import CORS
import joblib

import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "hFbVladB5RNf9ALFwRjY2oZYq_pUHVoXLKUuNIfEm811"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

app = Flask(__name__, static_url_path='')
CORS(app)

@app.route('/')
def sendHomePage():
    return render_template('index.html')
 
@app.route('/predict')
def predictSpecies():
    return render_template('predict.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    Have_IP = int(request.form['Have_IP'])
    Have_At = int(request.form['Have_At'])
    URL_Length = int(request.form['URL_Length'])
    URL_Depth = int(request.form['URL_Depth'])
    Redirection = int(request.form['Redirection'])
    https_Domain = int(request.form['https_Domain'])
    TinyURL = int(request.form['TinyURL'])
    Prefix_Suffix = int(request.form['Prefix_Suffix'])
    DNS_Record = int(request.form['DNS_Record'])
    Web_Traffic = int(request.form['Web_Traffic'])
    Domain_Age = int(request.form['Domain_Age'])
    Domain_End = int(request.form['Domain_End'])
    iFrame = int(request.form['iFrame'])
    Mouse_Over = int(request.form['Mouse_Over'])
    Right_Click = int(request.form['Right_Click'])
    Web_Forwards = int(request.form['Web_Forwards'])
    x = [[Have_IP, Have_At, URL_Length, URL_Depth, Redirection, https_Domain, TinyURL, Prefix_Suffix, DNS_Record, Web_Traffic, Domain_Age, Domain_End, iFrame, Mouse_Over, Right_Click, Web_Forwards]]
    
    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"fields": ["Have_IP","Have_At","URL_Length","URL_Depth","Redirection","https_Domain","TinyURL","Prefix/Suffix","DNS_Record","Web_Traffic","Domain_Age","Domain_End","iFrame","Mouse_Over","Right_Click","Web_Forwards"], "values":x}]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/140d5064-1fe6-40bf-b13c-1ecddb9a0d79/predictions?version=2022-11-18', json=payload_scoring,headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    print(response_scoring.json())
    prediction = response_scoring.json()
    predict = prediction['predictions'][0]['values'][0][0]
    if predict == 1:
    	return render_template('neg.html')
    else:
    	return render_template('pos.html')


if __name__ == "__main__":
    app.run(debug=True)

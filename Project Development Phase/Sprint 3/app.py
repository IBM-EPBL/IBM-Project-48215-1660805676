import numpy as np
import pickle
from flask import request, render_template, Flask, redirect, url_for
from flask_cors import CORS
import joblib


app = Flask(__name__, static_url_path='')
CORS(app)
model = pickle.load(open('model.pkl', 'rb'))

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
    va = [[Have_IP, Have_At, URL_Length, URL_Depth, Redirection, https_Domain, TinyURL, Prefix_Suffix, DNS_Record, Web_Traffic, Domain_Age, Domain_End, iFrame, Mouse_Over, Right_Click, Web_Forwards]]
    prediction = model.predict(va)[0]
    if prediction == 1:
    	return render_template('neg.html')
    else:
    	return render_template('pos.html')


if __name__ == "__main__":
    app.run(debug=True)

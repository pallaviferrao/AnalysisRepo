from flask import Flask, render_template, request, jsonify
import pickle
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    dR = [[ 0.14814815,  1.        ,  0.56692913, -1.26153846, -0.125     ,
         1.        ,  1.        ,  1.        ,  0.        ,  0.        ,
         0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
         0.        ,  0.        ,  1.        ,  0.        ,  1.        ,
         0.        ,  0.        ]]

    # file = open('modelTr.pkl', 'rb')

    # dump information to that file
    data  = pickle.load(open('modelTr4.pkl', 'rb'))
    valR = data.predict(dR)
    return jsonify({'prediction': 'What is Inkita doing?', 'value': str(valR[0])})

@app.route("/getSvmAnalysis",methods=['POST'])
def hanalysisSvm():
    print(request)
    print(request.headers)
    print( request.headers.get('Content-Type'))
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        print("Inside if")
        json = request.form.get('body')
        print(json)
        age = json['age']
        restingBp = json['restingBp']
        cholestrol = json['cholestrol']
        minHeartRate = json['minHeartRate']
        prevPeak = json['prevPeak']
        sex = json['sex']
        isExcerciseInduceAngina =json['isExcerciseInduceAngina']
        isTypicalAngina = json['isTypicalAngina']
        isAtypicalAngina = json['isAtypicalAngina']
        isNonAnginalPain = json['isNonAnginalPain']
        majorVessel = json['majorVessel']
        fastingBpGt120 = json['fastingBpGt120']
        restecg  = json['restecg']
        slope = json['slope']
        if(majorVessel == 1):
            caa1 =1
        if(majorVessel == 2):
            caa2 =1
        if(majorVessel == 3):
            caa3 =1
        if(majorVessel == 4):
            caa4 =1
        if(restecg == 1):
            restecg1 =1
        if(restecg == 2):
            restecg2 =1
  

        dR = [age, restingBp, cholestrol, minHeartRate, prevPeak, sex, isExcerciseInduceAngina,
        caa1, caa2, caa3, caa4, isTypicalAngina, isAtypicalAngina, isNonAnginalPain, fastingBpGt120,
        restecg1, restecg2, 0, 1,  1.  ,0 ,  0]
        data  = pickle.load(open('modelTr4.pkl', 'rb'))
        valR = data.predict(dR)
        return jsonify({'prediction': 'What is Inkita doing?', 'value': str(valR[0])})
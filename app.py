from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

@app.route("/")
def home():
    dR = [[ 0.14814815,  1.        ,  0.56692913, -1.26153846, -0.125     ,
         1.        ,  1.        ,  1.        ,  0.        ,  0.        ,
         0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
         0.        ,  0.        ,  1.        ,  0.        ,  1.        ,
         0.        ,  0.        ]]

    # file = open('modelTr.pkl', 'rb')

    # dump information to that file
    data  = pickle.load(open('modelTr.pkl', 'rb'))
    valR = data.predict(dR)
    return jsonify({'prediction': 'What is Inkita doing?', 'value': valR[0]})
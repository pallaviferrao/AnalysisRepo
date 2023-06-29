from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({'prediction': 'What is Inkita doing?', 'value': 'She will let me know?'})
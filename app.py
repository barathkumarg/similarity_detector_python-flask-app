from flask import Flask, render_template, request, redirect, url_for, session, Response, flash, jsonify
from difflib import SequenceMatcher
from werkzeug.utils import secure_filename
app = Flask(__name__)
import os

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template('index.html')

@app.route("/check_similarity", methods=["POST", "GET"])
def home():
    sim=''
    sim2=''
    if request.method == 'POST' and 'text1' in request.form and 'text2' in request.form:
        text1=request.form['text1']
        text2=request.form['text2']
        similarity=SequenceMatcher(None,text1,text2).ratio()
        similarity=similarity*100
        similarity=round(similarity, 2)

        return render_template('index.html',sim="It has {0} % Similarity Between them".format(similarity))

    elif request.method == 'POST':
        f1 = request.files['myfile1']
        f2= request.files['myfile2']
        filename1 = secure_filename(f1.filename)
        f1.save(secure_filename(f1.filename))

        filename2 = secure_filename(f2.filename)
        f2.save(secure_filename(f2.filename))

        with open(filename1,'rb') as file1, open(filename2,'rb') as file2:
            file1data=file1.read()
            file2data=file2.read()
            similarity = SequenceMatcher(None, file1data, file2data).ratio()
            similarity = similarity * 100
            similarity = round(similarity, 2)

        return render_template('index.html', sim2="It has {0} % Similarity Between them".format(similarity))
    else:

        return render_template('index.html',sim=sim,sim2=sim2)



if __name__ == '__main__':
    app.run(debug=True)
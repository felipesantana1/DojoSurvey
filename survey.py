from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')

def displaySurvey():
    return render_template('survey.html')

@app.route('/result', methods=['POST'])

def showResult():
    y = request.form['name']
    x = request.form['location']
    z = request.form['language']
    n = request.form['comment']
    return render_template('result.html', name = y, location = x, fl = z, text = n)

app.run(debug=True)
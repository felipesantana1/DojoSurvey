from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')

def displaySurvey():
    return render_template('survey.html')

@app.route('/result', methods=['POST'])

def showResult():
    y = request.form['name']
    x = request.form['location']
    z = request.form['language']
    n = request.form['comment']
    if len(request.form['name']) < 1:
        flash('Must fill out al text areas!')
        return render_template('error.html')
    elif len(request.form['comment']) < 1:
        flash('Must fill out al text areas!')
        return render_template('error.html')
    else:
        return render_template('result.html', name = y, location = x, fl = z, text = n)

app.run(debug=True)
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/first')
def hello_world():
    return render_template('first.html')

@app.route('/login')
def hello_world():
    return render_template('login.html')

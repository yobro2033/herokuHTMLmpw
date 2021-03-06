from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('mainpage.html')

@app.route('/first')
def first():
    return render_template('first.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/newsletter')
def newsletter():
    return render_template('newsletter.html')

@app.route('/test')
def testapp():
    return render_template('test.html')

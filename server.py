from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/blindTest')
def blindTestPage():
    return render_template('blindTest.html')

@app.route('/connect')
def connectAccPage():
    return render_template('connect.html')

@app.route('/createAcc')
def createAccPage():
    return render_template('createAcc.html')

@app.route('/connected')
def connectedPage():
    return render_template('connected.html')

# @app.route('/test')
# def hello():
#     return render_template('test.html')

app.run()
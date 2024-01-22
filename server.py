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

@app.route('/connected')
def connectedPage():
    return render_template('connected.html')

@app.route('/signup')
def signupPage():
    return render_template('signup.html')

@app.route('/login')
def loginPage():
    return render_template('login.html')

# @app.route('/test')
# def hello():
#     return render_template('test.html')

app.run()
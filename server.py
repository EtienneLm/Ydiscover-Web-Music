from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

# @app.route('/test')
# def hello():
#     return render_template('test.html')

app.run()
from flask import Flask, render_template, request, redirect, make_response
from static.src.sql import insertData, getData
from static.src.api import getToken, getTracks, getAllEmbebs
import hashlib

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/home')
def home():
    token = request.cookies.get('token')
    urls = getTracks(token, "rock", 6)
    embeds = getAllEmbebs(urls)
    return render_template('home.html', embeds=embeds)

@app.route('/blindTest')
def blindTestPage():
    return render_template('blindTest.html')

@app.route('/login' , methods=["GET", "POST"])
def connectAccPage():
    if request.method == "POST":
        email = request.form["email"]  
        password = request.form["password"] 
        print(email, password)
        hashPassword = hashlib.md5(password.encode()).hexdigest() #to verify the hashword, you make the password a hash and check if it corresponds to the hash
        verifAccount = getData(f"""SELECT * FROM User WHERE email='{email}' AND hashword='{hashPassword}'""")  
        if len(verifAccount) >= 1:
            token = getToken()
            if token != None :
                resp = make_response(redirect("/connected"))
                resp.set_cookie('token', token)
                return resp

    return render_template('login.html')

@app.route('/signup', methods=["GET", "POST"])
def createAccPage():
    if request.method == "POST":
        email = request.form["email"]  
        password = request.form["password"] # get the name="xxxx" from the html
        password_confirm = request.form["passwordConfirm"]
        if password_confirm == password:
            verifEmail = getData(f"""SELECT * FROM User WHERE email='{email}'""") # 
            if len(verifEmail) == 0:  
                insertData(email, password) # if there is nothing in email and password, then instert the data
                redirect('/connect') # redirects to the login page after registering
            
    return render_template('signup.html')
    

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
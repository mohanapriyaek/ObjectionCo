from flask import Flask,render_template,request,redirect, json, Response, jsonify

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
   #Call the method that runs the application server. 
    app.run()


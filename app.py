from flask import Flask, redirect, url_for, render_template, request, jsonify
from datetime import datetime
from chat import get_response

app = Flask(__name__)

# from datetime import datetime
# from flask import render_template
# from FlaskChat import app

# @app.route('/')
# def index():
#     return 'Hello, World!'

@app.route('/index')
def index():
    """Renders the home page."""
    return render_template(
        'home.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.post('/enter')
def enter():
    text= request.get_json().get("message")
    return text
    

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/predict', methods=['POST'])
def predict():
    # text = request.get_json().get("message")
        
    request_data = request.get_json()
    text = request_data['message']
    response = get_response(text)
    message = {"answer":response}
    
    print(message)
    
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)
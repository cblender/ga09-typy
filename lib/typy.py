import requests

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))

from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, world!"
    print("Hello, world!")

@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}!'

@app.route('/endpoint', methods=['GET', 'PUT', 'POST', 'DELETE'])
def endpoint():
    if request.method == 'GET':
        return 'GET request'
    
    if request.method == 'PUT':
        return 'PUT request'

    if request.method == 'POST':
        return 'POST request'

    if request.method == 'DELETE':
        return 'DELETE request'

# PLANNING!
# FUNCTIONALITY WILL BE INSTANTIATED VIA ROUTING.
# CREATE ----- @app.route('/new/<name>')
# READ ------- @app.route('/list/<name>')  ---- NOTE: "READ" MEANS READ OUT THE LIST OF NOTES
# UPDATE ----- @app.route('/open/<name>') ----- NOTE: "UPDATE" MEANS OPEN A PREEXISTING NOTE, WITH THE ABILITY TO MODIFY IT
# DESTROY ---- @app.route('/delete/<name>')
# 
# 



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# NOTHING ELSE GOES BELOW THIS LINE!!!

app.run()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END

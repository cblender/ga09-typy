import requests

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))

from flask import Flask
from flask import request
from flask import jsonify
from peewee import *

# POSTGRESQL SETUP
db = PostgresqlDatabase('typy', user='postgres', password='', host='localhost', port=5423)

class BaseModel(Model):
  class Meta:
    database = db

class Note(BaseModel):
  id = IntegerField()
  name = CharField()
  author = CharField()
  date = CharField()

db.connect()
db.drop_tables([Note])
db.create_tables([Note])

Note(id=1, name='README 2: ELECTRIC BOOGALOO', author='Person McPersonface', date='4/20/1969').save()
Note(id=2, name='REVENGE OF THE NOTES', author='Literally Jesus', date='12/25/ZERO').save()

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, world!"
    print("Hello, world!")

@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}!'

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# THIS CODE IS *** C O N D E M N E D ***
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
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



# PLANNING!
# FUNCTIONALITY WILL BE INSTANTIATED VIA ROUTING.

# CREATE ----- @app.route('/new/<name>')



# READ ------- @app.route('/list/<name>')  ---- NOTE: "READ" MEANS READ OUT THE LIST OF NOTES



# UPDATE ----- @app.route('/open/<name>') ----- NOTE: "UPDATE" MEANS OPEN A PREEXISTING NOTE, WITH THE ABILITY TO MODIFY IT



# DESTROY ---- @app.route('/delete/<name>')





# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# NOTHING ELSE GOES BELOW THIS LINE!!!

app.run(debug=True)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END

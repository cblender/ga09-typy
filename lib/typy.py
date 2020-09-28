import requests

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))

from flask import Flask
from flask import request
from flask import jsonify
from peewee import *
import logging
import sys

# # POSTGRESQL SETUP
db = PostgresqlDatabase('typy', user='cblender', password='', host='localhost', port=5000)

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
# @app.route('/endpoint', methods=['GET', 'PUT', 'POST', 'DELETE'])
# def endpoint():
#     if request.method == 'GET':
#         return 'GET request'
    
#     if request.method == 'PUT':
#         return 'PUT request'

#     if request.method == 'POST':
#         return 'POST request'

#     if request.method == 'DELETE':
#         return 'DELETE request'
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



# PLANNING!
# FUNCTIONALITY WILL BE INSTANTIATED VIA ROUTING.

# CREATE ----- @app.route('/new/<name>')
@app.route('/new/<name>', methods=['GET', 'PUT', 'POST'])
def note_create(name):
    return f'CREATE NOTE NAMED {name}'



# READ ------- @app.route('/list/<name>')  ---- NOTE: "READ" MEANS READ OUT THE LIST OF NOTES
@app.route('/list/', methods=['GET'])
def note_list():
    return f'LIST ALL NOTES'



# UPDATE ----- @app.route('/open/<name>') ----- NOTE: "UPDATE" MEANS OPEN A PREEXISTING NOTE, WITH THE ABILITY TO MODIFY IT
@app.route('/open/<name>', methods=['GET', 'PUT', 'POST'])
def note_open(name):
    return f'OPEN {name} FOR EDITING'


# DESTROY ---- @app.route('/delete/<name>')
@app.route('/delete/<name>', methods=['GET', 'POST', 'DELETE'])
def note_delete(name):
    return f'DELETE {name} - ARE YOU SURE?'




# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# NOTHING ELSE GOES BELOW THIS LINE!!!

app.run(debug=True)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END

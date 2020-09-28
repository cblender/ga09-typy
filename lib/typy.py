from flask import Flask
from flask import request
from flask import jsonify
from peewee import *
import logging
import psycopg2
import requests
import sys

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))


# # POSTGRESQL SETUP
db = PostgresqlDatabase('typy', user='cblender', password='', host='localhost', port=5423)

class BaseModel(Model):
  class Meta:
    database = db

class Note(BaseModel):
  id = IntegerField()
  name = CharField()
  author = CharField()
  date = CharField()

class Line(BaseModel):
    id = IntegerField()
    content = CharField()


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



# PLANNING!
# FUNCTIONALITY WILL BE INSTANTIATED VIA ROUTING.



# ——————————————————————————————————————————————————————————————————————————————————————————————————
#      .aMMMb  dMMMMb  dMMMMMP .aMMMb dMMMMMMP dMMMMMP 
#     dMP"VMP dMP.dMP dMP     dMP"dMP   dMP   dMP      
#    dMP     dMMMMK" dMMMP   dMMMMMP   dMP   dMMMP     
#   dMP.aMP dMP"AMF dMP     dMP dMP   dMP   dMP        
#   VMMMP" dMP dMP dMMMMMP dMP dMP   dMP   dMMMMMP 

# CREATE ----- @app.route('/new/<name>')
@app.route('/new/<name>', methods=['GET', 'PUT', 'POST', 'DELETE'])
def note_create(name):

    author = input("Who is the author? ")
    date = input("What is the date? ")
    
    # NOTE TO SELF: REPLACE WITH PROPER ID - EITHER RANDOM OR SEQUENTIAL
    id = 1

    Note.create(id=f'{id}', name=f'{name}', author=f'{author}', date=f'{date}')

    db.create_tables([Note])

    return f'CREATE NOTE NAMED {name}'



# ——————————————————————————————————————————————————————————————————————————————————————————————————
#       .aMMMb  dMMMMb  dMMMMMP dMMMMb 
#      dMP"dMP dMP.dMP dMP     dMP dMP 
#     dMP dMP dMMMMP" dMMMP   dMP dMP  
#    dMP.aMP dMP     dMP     dMP dMP   
#    VMMMP" dMP     dMMMMMP dMP dMP 

# UPDATE ----- @app.route('/open/<name>') ----- NOTE: "UPDATE" MEANS OPEN A PREEXISTING NOTE, WITH THE ABILITY TO MODIFY IT
@app.route('/open/<name>', methods=['GET', 'PUT', 'POST', 'DELETE'])
def note_open(name):

    return f'OPEN {name} FOR EDITING'



# ——————————————————————————————————————————————————————————————————————————————————————————————————
#    dMMMMMMP dMMMMb  .aMMMb  .dMMMb  dMP dMP 
#      dMP   dMP.dMP dMP"dMP dMP" VP dMP dMP  
#     dMP   dMMMMK" dMMMMMP  VMMMb  dMMMMMP   
#    dMP   dMP"AMF dMP dMP dP .dMP dMP dMP    
#   dMP   dMP dMP dMP dMP  VMMMP" dMP dMP  

# DESTROY ---- @app.route('/delete/<name>')
@app.route('/delete/<name>', methods=['GET', 'PUT', 'POST', 'DELETE'])
def note_delete(name):

    return f'DELETE {name} - ARE YOU SURE?'



# ——————————————————————————————————————————————————————————————————————————————————————————————————
#       dMP     dMP .dMMMb dMMMMMMP 
#      dMP     amr dMP" VP   dMP    
#     dMP     dMP  VMMMb    dMP     
#    dMP     dMP dP .dMP   dMP      
#   dMMMMMP dMP  VMMMP"   dMP 

# READ ------- @app.route('/list/<name>')  ---- NOTE: "READ" MEANS READ OUT THE LIST OF NOTES
@app.route('/list/', methods=['GET', 'PUT', 'POST', 'DELETE'])
def note_list():

    return f'LIST ALL NOTES'

# ——————————————————————————————————————————————————————————————————————————————————————————————————


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# NOTHING ELSE GOES BELOW THIS LINE!!!

app.run(debug=True)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END

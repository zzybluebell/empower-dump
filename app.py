from flask import Flask
from flask import request, jsonify

import pymongo
import datetime

# standard flask application
app = Flask(__name__)
app.secret_key = "secretkey"
app.config['MONGO_URI'] = 'mongodb://localhost:27017/empower-auth'
app.config['MONGO_DBNAME'] = 'empower-auth'

client = pymongo.MongoClient('localhost', 27017)
db = client['empower-auth']



#db.books.find().sort({title:1}) 1 is accending order, -1 is dendening order
# .limit
# find(person: ["Jack","Zhang"]) is find exatcly these 2 identies, no [ ] means 'contains'


@app.route("/login", methods=['POST'])
def login():
    data = []
    if request.form:
        username = request.form['username']
        password = request.form['password']
        data = list()

    

# @app.route("/summary", methods=['POST','GET'])
# def summary():

# @app.route("/rank", methods=['POST'])
# def rank():

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 5000, debug = False )
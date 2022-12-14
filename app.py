from flask import Flask, session
from flask import request, jsonify
from bson.objectid import ObjectId
import pymongo
import datetime

# standard flask application
app = Flask(__name__)
app.secret_key = "secretkey"
app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/empower-auth'
app.config['MONGO_DBNAME'] = 'empower-auth'

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client['empower-auth']

#db.books.find().sort({title:1}) 1 is accending order, -1 is dendening order
# .limit
# find(person: ["Jack","Zhang"]) is find exatcly these 2 identies, no [ ] means 'contains'

@app.route("/login", methods=['POST'])
def login():
    
    data = []
    #from:the key/value pairs in the body, from a HTML post form, or JavaScript request that isn't JSON encoded
    if request.form:
        username = request.form['username']
        password = request.form['password']
        data = list(db.patient.find({
            'username': username,
            'password': password
        }).limit(1))
    if len(data) > 0:
        session['userid'] = str(data[0]['_id'])
        return jsonify('successful')
    else:
        res = jsonify('fail')
        res.status_code = 300
        return res
    
@app.route("/summary", methods=['POST','GET'])
def summary():
    userid = session.get('userid') # based on login user _id
    if userid == None:
        res = jsonify('logout')
        res.status_code = 300
        return res
    else:
        date = request.values.get('date')
        if date == None:
            res = jsonify('Missing date parameter')
            res.status_code = 300
        else:
            try:
                # dt = datetime.time()
                date = datetime.datetime.strptime(date, '%Y-%m-%d')
                activity = list(db.daily_activity_summary.find({
                    "patient": ObjectId(userid),
                    "date": date
                }))
                if len(activity) > 0:
                    choosen_activity = activity[0]
                    data = {
                        'steps': choosen_activity['steps'],
                        'distance': choosen_activity['distance'],
                        'calories': choosen_activity['calories'],
                        'active_minutes': choosen_activity['duration']
                    }
                    res = jsonify(data)
                else:
                    res = jsonify("")
            except Exception as e:
                res = jsonify("invalid date format, please enter date format as YY-MM-D")
                res.status_code = 300
        return res


@app.route("/rank", methods=['POST','GET'])
def rank():
    rank_list = db.daily_activity_summary.aggregate([
        {
            "$lookup":{
                "from": "patient",
                "localField": "patient",
                "foreignField": "_id",
                "as": "patients"
            }
        },
        {
            "$group":{
                "_id":"$patient",
                "total_steps": { "$sum": "$steps" },
                "username": {
                    "$max": {
                        "$arrayElemAt": ["$patients.username", 0]
                    }
                }
            }
        },
        {
            "$sort": {
                "total_steps": -1
            }
        },
        {
            "$project":{
                "_id": 0,
                "username": 1
            }
        },
    ]);
    username_list  = []
    for patient in list(rank_list):
        username_list.append(patient['username'])
    return jsonify(username_list)

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 5000, debug = True )

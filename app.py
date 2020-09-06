from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo
from flask_cors import CORS

MEDICIONES = [
    {
        "timestamp": "12/15/2014 01:40:00 AM",
        "mac": "0013a20040b4b755",
        "boardtype": 1,
        "boardid": 508,
        "temp_max": 21.6,
        "temp_min": 21.6,
        "temp_avg": 21.6,
        "light_max": 96.4,
        "light_min": 96.4,
        "light_avg": 96.4,
        "humidity_min": 41.2,
        "humidity_max": 41.2,
        "humidity_avg": 41.2,
        "model": "ENV",
        "latitude": -37.8134078,
        "longitude": 144.9794923,
        "elevation": 30.1,
        "location": "Fitzroy Gardens",
        "rowid": "508-20141215014000",
        "Position": ""
    },
    {
        "timestamp": "12/15/2014 01:40:00 AM",
        "mac": "0013a20040b516ed",
        "boardtype": 1,
        "boardid": 505,
        "temp_max": 23.2,
        "temp_min": 23.2,
        "temp_avg": 23.2,
        "light_max": 93.5,
        "light_min": 93.5,
        "light_avg": 93.5,
        "humidity_min": 48.3,
        "humidity_max": 48.3,
        "humidity_avg": 48.3,
        "model": "ENV",
        "latitude": -37.813073,
        "longitude": 144.9804061,
        "elevation": 29.91,
        "location": "Fitzroy Gardens",
        "rowid": "505-20141215014000",
        "Position": ""
    },
    {
        "timestamp": "12/15/2014 01:45:00 AM",
        "mac": "0013a20040b516f6",
        "boardtype": 1,
        "boardid": 507,
        "temp_max": 21.6,
        "temp_min": 21.6,
        "temp_avg": 21.6,
        "light_max": 97.2,
        "light_min": 97.2,
        "light_avg": 97.2,
        "humidity_min": 44.8,
        "humidity_max": 44.8,
        "humidity_avg": 44.8,
        "model": "ENV",
        "latitude": -37.8149218,
        "longitude": 144.9822582,
        "elevation": 38.79,
        "location": "Fitzroy Gardens",
        "rowid": "507-20141215014500",
        "Position": ""
    }
]

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'temperatura'
app.config["MONGO_URI"] = "mongodb://localhost:27017/temperatura"
mongo = PyMongo(app)
print(mongo)
# app.config.from_object(__name__)

"""
connection = Connection()
db = connection['temperatura']
units = db['temperaturas']
"""

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
# @app.route("/temperaturas", methods=['GET'])
# def home_page():
#     temperaturas = mongo.db.temperaturas.find({"online": True})
#     response = json_util.dump(temperaturas)
#     return Response(response, mimetype='application/json')

@app.route('/temperaturas', methods=['GET'])
def get_all_stars():
    temperatura = mongo.db.temperaturas
    output = []
    for s in temperatura.find():
        output.append({'location': s['location']})
    return jsonify({'result': output[0:10]})


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/mediciones', methods=['GET'])
def all_mediciones():
    return jsonify({
        'status': 'success',
        'medicion': MEDICIONES
    })


if __name__ == '__main__':
    app.run()

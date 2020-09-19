import json
import pymongo
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from pymongo import MongoClient
import pandas as pd
from datapreprocessing import preprocessdata

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
# app.config.from_object(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# app = Flask(__name__)
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

cluster = MongoClient('mongodb+srv://jihwan:1234@intelportfolio.kqupw.gcp.mongodb.net/test?retryWrites=true&w=majority')
db = cluster['test']

## BACKEND and ML
collection_preprocessed_data = db['preprocessed_data']

@app.route('/processed_data', methods=['GET'])
def get_data_processed():
    documents = collection_preprocessed_data.find()
    response = []
    for document in documents:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response)

@app.route("/processed_data", methods=['POST'])
def insert_document_data_processed():
    req_data = request.get_json()
    # stock_input = (req_data)
    preprocessdata(req_data)
    data = pd.read_csv('processed_data.csv')
    data_json = json.loads(data.to_json(orient='records'))
    collection_preprocessed_data.remove()
    collection_preprocessed_data.insert(data_json)
    return ('', 204)

## FRONTEND and CHARTJS

# Bubble
collection_bubble = db['bubble']
# Scatter
collection_scatter = db['scatter']
# PolarArea
collection_polararea = db['polararea']
# Radar
collection_radar= db['radar']
# Pie
collection_pie= db['pie']
# Doughnut
collection_doughnut= db['doughnut']
# Bar
collection_bar= db['bar']
# Line
collection_line= db['line']

# SCATTER
@app.route("/scatter", methods=['POST'])
def insert_document_scatter():
    req_data = request.get_json()
    # Check if the data from the website already exists in the database. If so,
    # delete it, if not, add it.
    if collection_scatter.count_documents(req_data, limit = 1):
        collection_scatter.delete_one(req_data)
    else:
        collection_scatter.insert_one(req_data)
    return ('', 204)
         
@app.route('/scatter', methods=['GET'])
def get_data_scatter():
    documents = collection_scatter.find()
    response = []
    for document in documents:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response)


# BUBBLE
@app.route("/bubble", methods=['POST'])
def insert_document_bubble():
    req_data = request.get_json()
    if collection_bubble.count_documents(req_data, limit = 1):
        collection_bubble.delete_one(req_data)
    else:
        collection_bubble.insert_one(req_data)
    return ('', 204)
         
@app.route('/bubble', methods=['GET'])
def get_data_bubble():
    documents = collection_bubble.find()
    response = []
    for document in documents:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response)


# POLAR AREA
@app.route("/polararea", methods=['POST'])
def insert_document_polararea():
    req_data = request.get_json()
    if collection_polararea.count_documents(req_data, limit = 1):
        collection_polararea.delete_one(req_data)
    else:
        collection_polararea.insert_one(req_data)
    return ('', 204)

# @app.route('/polararea', methods=['POST'])
# def delete_data_polararea():
    # req_data = request.get_json()
    # if collection_polararea.count_documents(req_data, limit = 1):
    #     collection_polararea.delete_one(req_data)
    # else:
    #     collection_polararea.insert_one(req_data)
#     # collection_polararea.remove()
#     # collection_polararea.delete_one(req_data)
#     # collection_polararea.delete_one({"x": "Seoul","y": "100"})
#     return ('', 204)       

@app.route('/polararea', methods=['GET'])
def get_data_polararea():
    documents = collection_polararea.find()
    response = []
    for document in documents:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response)

# curl --request POST \
#   --url http://localhost:5000/polararea \
#   --header 'content-type: application/json' \
#   --data '{
#  "x":"Jakarta",
#  "y":"1500"
# }'

# curl --request DELETE \
#   --url http://localhost:5000/polararea \
#   --header 'content-type: application/json' \
#   --data '{
#  "x":"Seoul",
#  "y":"100"
# }'

# RADAR
@app.route("/radar", methods=['POST'])
def insert_document_radar():
    req_data = request.get_json()
    if collection_radar.count_documents(req_data, limit = 1):
        collection_radar.delete_one(req_data)
    else:
        collection_radar.insert_one(req_data)
    return ('', 204)
         
@app.route('/radar', methods=['GET'])
def get_data_radar():
    documents = collection_radar.find()
    response = []
    for document in documents:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response)


# PIE
@app.route("/pie", methods=['POST'])
def insert_document_pie():
    req_data = request.get_json()
    if collection_pie.count_documents(req_data, limit = 1):
        collection_pie.delete_one(req_data)
    else:
        collection_pie.insert_one(req_data)
    return ('', 204)
         
@app.route('/pie', methods=['GET'])
def get_data_pie():
    documents = collection_pie.find()
    response = []
    for document in documents:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response)


# DOUGHNUT
@app.route("/doughnut", methods=['POST'])
def insert_document_doughnut():
    req_data = request.get_json()
    if collection_doughnut.count_documents(req_data, limit = 1):
        collection_doughnut.delete_one(req_data)
    else:
        collection_doughnut.insert_one(req_data)
    return ('', 204)
         
@app.route('/doughnut', methods=['GET'])
def get_data_doughnut():
    documents = collection_doughnut.find()
    response = []
    for document in documents:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response)


# BAR
@app.route("/bar", methods=['POST'])
def insert_document_bar():
    req_data = request.get_json()
    if collection_bar.count_documents(req_data, limit = 1):
        collection_bar.delete_one(req_data)
    else:
        collection_bar.insert_one(req_data)
    return ('', 204)
         
@app.route('/bar', methods=['GET'])
def get_data_bar():
    documents = collection_bar.find()
    response = []
    for document in documents:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response)


# LINE
@app.route("/line", methods=['POST'])
def insert_document_line():
    req_data = request.get_json()
    if collection_line.count_documents(req_data, limit = 1):
        collection_line.delete_one(req_data)
    else:
        collection_line.insert_one(req_data)
    return ('', 204)
         
@app.route('/line', methods=['GET'])
def get_data_line():
    documents = collection_line.find()
    response = []
    for document in documents:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response)



if __name__ == '__main__':
    app.run()


from flask import Flask, send_from_directory, render_template, request, jsonify, make_response
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS, cross_origin #comment on deployment
from backend.brains import Brains
import boto3
import os

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
cors = CORS(app) #comment on deployment
api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

api.add_resource(Brains, '/flask/hello')
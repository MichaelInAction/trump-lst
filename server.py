from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

class Tweet(Resource):
    def get(self):
        return jsonify({'employees': {'message': 'hi'}})

api.add_resource(Tweet, '/tweet')

if __name__ == '__main__':
    app.run(port='5002')

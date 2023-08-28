from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask import Flask, jsonify, request


filename = "profile_info"
description = "get profile infomation"

# GENERAL API INFIO
class Info(Resource):
    def post(self):
        data = filename + " API POST"
        info = description
        return{
            'information': data,
            'Description': description

        }, 200

    def get(self):
       data = filename + " API GET"
       return {'info': data}, 200

class Check(Resource):
    def post(self):
        data = "working"
        return{
            'status': data
        }, 200

    def get(self):
       data = "working"
       return {'status': data}, 200


app = Flask(__name__)
api = Api(app)
# api = Api(app, prefix="/api/v1")

api.add_resource(Info, '/')
api.add_resource(Check, '/health')

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0',port=8080) 

from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask import Flask, jsonify, request

# GENERAL API INFIO
class Info(Resource):
    def post(self):
        data = "Info  API POST"
        return{
            'status': data
        }, 200

    def get(self):
       data = "Info  API GET"
       return {'status': data}, 200

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
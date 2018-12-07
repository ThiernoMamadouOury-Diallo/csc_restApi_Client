from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
import requests

class WebsocketRequest(Resource):
    def get(self, id):
        response = requests.get("http://localhost:8888/ws/" + str(id))
        if response.status_code == 200:
            return response.json()
        else:
            return "websocket not created or found"

app = Flask(__name__)
api = Api(app)
api.add_resource(WebsocketRequest, "/ws/<int:id>")
app.run(host='0.0.0.0')
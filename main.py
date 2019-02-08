import json
import unittest

from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
import requests

class WebsocketRequest(Resource):
    def get(self, id):
        response = requests.get("http://localhost:5001/ws/" + str(id))
        if response.status_code == 200:
            return response.json()
        else:
            return "websocket not created or found"

class NotificationFacture(Resource):
    def get(self, id):
        # retrieve from dfs
        urls = []

        response = {"id": id, "bills": [{"id": "test", "date": "test", "uri": "http://maven.apache.org/archives/maven-1.x/maven.pdf"}, {"id": "", "date": "", "uri": ""}]}
        return json.dumps(response)

class NotificationFactureTest(unittest.TestCase):
    def test_bills(self):
        res = NotificationFacture.get("1")
        self.assertIn({}, {})


app = Flask(__name__)
api = Api(app)
api.add_resource(NotificationFacture, "/bills/<int:id>")
api.add_resource(WebsocketRequest, "/ws/<int:id>")
app.run(host='0.0.0.0', port='5000')
import unittest

import requests
from flask import Flask, jsonify
from flask_restful import Api, Resource


class WebsocketRequest(Resource):
    def get(self, id):
        response = requests.get("http://localhost:5001/ws/" + str(id))
        if response.status_code == 200:
            return response.json()
        else:
            return "websocket not created or found"

class NotificationFacture(Resource):
    def get(self, userId):
        # retrieve from dfs
        urls = []

        response = {"userId": userId, "bills": [{"billId": "test", "date": "test", "uri": "http://maven.apache.org/archives/maven-1.x/maven.pdf"}, {"billId": "", "date": "", "uri": "https://www.cfasup2000.fr/media/20190123115038_jpo_2019-bd.pdf"}]}
        return jsonify(response)

class NotificationFactureTest(unittest.TestCase):
    def test_bills(self):
        res = NotificationFacture.get("1")
        self.assertIn({}, {})


app = Flask(__name__)
api = Api(app)
api.add_resource(NotificationFacture, "/bills/<int:userId>")
api.add_resource(WebsocketRequest, "/ws/<int:id>")
app.run(host='0.0.0.0', port='5000')
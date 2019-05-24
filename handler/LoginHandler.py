import json
import logging

from flask import request
from flask_restful import Resource

from model.User import UserEncoder
from service.LoggingService import LoggingService

class LoginHandler(Resource):
    def post(self):
        data = request.json
        if data is None:
            return json.dumps({'error': True}), 400, {'ContentType': 'application/json'}
        else:
            user = LoggingService().getUser(data['login'], data['password'])
            logging.info("New user connected : %s" % data['login'])
            return UserEncoder().encode(user), 200, {'ContentType': 'application/json'}
from flask import send_from_directory

from flask_restful import Resource

class JsLogic(Resource):
    def get(self, name):
        if name == 'index.js':
            return send_from_directory('public/js', "index.js")
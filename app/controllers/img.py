from flask import send_from_directory

from flask_restful import Resource

class Img(Resource):
    def get(self, name):
        if name == 'iss.png':
            return send_from_directory('public/img', "iss.png")
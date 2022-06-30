from flask import send_from_directory

from flask_restful import Resource

class Styles(Resource):
    def get(self):
        return send_from_directory('public/styles', "styles.css")
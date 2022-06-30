from flask import send_from_directory

from flask_restful import Resource

class Home(Resource):
    # def get(self):
    #     return send_from_directory('public', "index.html")
    def get(self):
        return {
            "message": "Welcome to the ISS Locator API"
        }
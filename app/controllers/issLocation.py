from flask_restful import Resource
import requests


class ISSLocation(Resource):
    def get(self):
         response = requests.get('http://api.open-notify.org/iss-now.json')
         return {
            "lat": response.json()['iss_position']['latitude'],
            "lng": response.json()['iss_position']['longitude']
            }
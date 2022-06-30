from dotenv import load_dotenv
load_dotenv()
from flask import Flask, send_from_directory
from flask_restful import Api, Resource
from flask_cors import CORS
from app.controllers.issLocation import ISSLocation
from app.controllers.home import Home
from app.controllers.styles import Styles
from app.controllers.jslogic import JsLogic
from app.controllers.img import Img
import os

mode=os.environ.get('MODE')
print(mode)

app = Flask(__name__)

api = Api(app)

CORS(app, resources={r"/api/*": {"origins": "https://isslocatorpy.herokuapp.com/*"}})

class Favicon(Resource):
    def get(self):
         return send_from_directory('public/img', "iss.png")

api.add_resource(Home, '/')

# api.add_resource(Favicon, '/favicon.ico')

# api.add_resource(ISSLocation, '/iss/now')

# api.add_resource(Styles, '/styles/styles.css')

# api.add_resource(JsLogic, '/js/<string:name>')

# api.add_resource(Img, '/img/<string:name>')

if __name__ == "__main__":
    # start up api
    if mode == 'dev' or mode == 'development':  
        app.run("localhost",port=5000, debug=False)
    elif mode == 'prod' or mode == 'production':
        from waitress import serve
        serve(app, host="0.0.0.0", port=5000)
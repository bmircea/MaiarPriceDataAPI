from flask import Flask
from flask_restful import Api
from Endpoints import Current, Historical

app = Flask(__name__)
api = Api(app)
api.add_resource(Current, '/current')
api.add_resource(Historical, '/historical')
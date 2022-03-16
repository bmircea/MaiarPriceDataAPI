from flask import Flask
from flask_restful import Api
from Endpoints import Historical, Snapshot

app = Flask(__name__)
api = Api(app)
api.add_resource(Snapshot, '/snapshot/<string:base>')
api.add_resource(Historical, '/historical/<string:ticker>/<int:span>/<string:startTime>/<string:stopTime>')

app.run()
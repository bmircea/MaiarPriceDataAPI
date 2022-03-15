from click import Argument
from flask_restful import Resource, reqparse

class Current(Resource):
    # '/current/{base}/{quote}' endpoint
    def get(self):
        # Parse arguments
        parser = reqparse.RequestParser(trim=True)
        parser.add_argument('base', required=True)
        parser.add_argument('quote', required=False)
        args = parser.parse_args()
        
        # Query DB
        pass

        #return {resp_dict}, code
        #return {dict}, 200


class Historical(Resource):
    # '/historical/' endpoint
    def get(self):
        pass

    #return {resp_dict}, code
        #return {dict}, 200
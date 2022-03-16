from flask_restful import Resource, reqparse

class Snapshot(Resource):
    # '/snapshot/{base}' endpoint
    def get(self, base):
        # Parse arguments
        # parser = reqparse.RequestParser(trim=True)
        # parser.add_argument('base', required=True)
        # parser.add_argument('quote', required=False)
        # args = parser.parse_args()
        


        # Query DB
        # pass
        return {base:'a'}, 200
        #return {resp_dict}, code
        #return {dict}, 200


class Historical(Resource):
    # '/historical/{ticker}/{span}/{startTime}/{stopTime}' endpoint
    def get(self, ticker, span, startTime, stopTime):
        return {ticker:span,
                startTime:stopTime}, 200



    #return {resp_dict}, code
        #return {dict}, 200
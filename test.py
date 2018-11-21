from flask import Flask
from flask_restful import Resource, Api
 
app = Flask(__name__)
api = Api(app)
 
class CreateUser(Resource):
    def post(self):
        return {'status': 'success'}
 
api.add_resource(CreateUser, '/scio')
 
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
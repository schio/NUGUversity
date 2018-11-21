from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
 
app = Flask(__name__)
api = Api(app)
 
class CreateUser(Resource):
    def post(self):
        try:
            parser = reqparser.RequestParser()
            parser.add_argument('email', type=str)
            parser.add_argument('user_name', type=str)
            parser.add_argument('password', type=str)
            args = parser.parse_args()

            return {
                'Email': args['email'],
                'UserName': args['user_name'],
                'Password': args['password']
            }
        except Exception as e:
            return {'error': str(e)}
 
api.add_resource(CreateUser, '/scio')
 
if __name__ == '__main__':
    app.run(debug=True)
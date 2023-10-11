from flask import Flask
from flask_restful import Resource, Api
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

class HelloWorld(Resource):
    def get(self):
        """
        Exemplo de endpoint de saudação.
        ---
        tags:
          - saudação
        responses:
          200:
            description: Mensagem de saudação
        """
        return {'message': 'Olá, mundo!'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
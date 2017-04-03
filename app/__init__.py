from flask import Flask
from flask_restful import Api
from app.resources.tic_tac_toe import Tic_Tac_Toe

app = Flask(__name__, instance_relative_config=True)
api = Api(app)
app.config.from_object('config')

api.add_resource(Tic_Tac_Toe, "/Tic-Tac-Toe/<string:board>")
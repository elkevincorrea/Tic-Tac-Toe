from flask_restful import Resource
from app.minimax import Minimax_State

class Tic_Tac_Toe(Resource):
    def get(self, board):
        return {'hello': 'Hello World!'}

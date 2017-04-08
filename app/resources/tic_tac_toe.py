import re
from flask_restful import Resource, reqparse
from app import minimax, models
import json

def board(board_str):
    match = re.match(r'[012]{9}', board_str)
    if match:
        return board_str
    else:
        raise ValueError('{} is not a valid board for tic-tac-toe. use 1 player 1, 2 for player 2, and 0 not played'.format(board_str))

def player(player_str):
    match = re.match(r'[12]{1}', player_str)
    if match:
        return int(player_str)
    else:
        raise ValueError('{} is not a valid player ')

parser = reqparse.RequestParser()
parser.add_argument('board', location='args', required=True, type=board)
parser.add_argument('player', location='args', required=True, type=player)

def str_board_to_matrix(str_board):
    board = []
    count = 0
    for i in range(3):
        board.append([])
        for j in range(3):
            board[i].append(int(str_board[count]))
            count += 1
    return board

class Tic_Tac_Toe_Res(Resource):
    def get(self):
        args = parser.parse_args()
        matrix = str_board_to_matrix(args.board)
        tic_tac = models.Tic_Tac_Toe(matrix, args.player)
        succesors = tic_tac.sucessors()
        return {'board': [[0, 0, 0], [0, 0, 0]], \
        'succesors': json.dumps([ob.__dict__ for ob in succesors])}

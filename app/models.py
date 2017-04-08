from app.minimax import Minimax_State
from copy import deepcopy

class Tic_Tac_Toe(Minimax_State):
    PLAYER_O = 1
    PLAYER_X = 2
    def __init__(self, board, player):
        self.board = board
        self.player = player

    def full_board(self):
        for row in self.board:
            for n in self.board[row]:
                if n == 0:
                    return False
        return True

    def winner(self):
        for row in self.board:
            if (row[0] == Tic_Tac_Toe.PLAYER_O and \
                    row[1] == Tic_Tac_Toe.PLAYER_O and row[2] == Tic_Tac_Toe.PLAYER_O) or \
                    (row[0] == Tic_Tac_Toe.PLAYER_X and row[1] == Tic_Tac_Toe.PLAYER_X and \
                     row[2] == Tic_Tac_Toe.PLAYER_X):
                return row[0]
        for j in range(len(self.board[0])):
            if (self.board[0][j] == Tic_Tac_Toe.PLAYER_O and \
                    self.board[1][j] == Tic_Tac_Toe.PLAYER_O and \
                    self.board[2][j] == Tic_Tac_Toe.PLAYER_O) or \
                    (self.board[0][j] == Tic_Tac_Toe.PLAYER_O and \
                    self.board[1][j] == Tic_Tac_Toe.PLAYER_O and \
                    self.board[2][j] == Tic_Tac_Toe.PLAYER_O):
                return self.board[0][j]
        player_o_count = 0
        player_x_count = 0
        for i in range(len(self.board)):
            if self.board[i][i] == Tic_Tac_Toe.PLAYER_O:
                player_o_count += 1
            elif self.board[i][i] == Tic_Tac_Toe.PLAYER_X:
                player_x_count += 1
        if player_o_count == 3:
            return Tic_Tac_Toe.PLAYER_O
        elif player_x_count == 3:
            return Tic_Tac_Toe.PLAYER_X

        for i in range(len(self.board)):
            if self.board[i][2 - i] == Tic_Tac_Toe.PLAYER_O:
                player_o_count += 1
            elif self.board[i][2 - i] == Tic_Tac_Toe.PLAYER_X:
                player_x_count += 1
        if player_o_count == 3:
            return Tic_Tac_Toe.PLAYER_O
        elif player_x_count == 3:
            return Tic_Tac_Toe.PLAYER_X
        return 0

    def utility(self):
        player_winner = self.winner()
        if player_winner:
            if player_winner == self.player:
                return 1
            else:
                return -1
        if self.full_board():
            return 0
        return None

    def is_finished(self):
        return self.utility() != None

    def sucessors(self):
        sucessors = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    new_board = deepcopy(self.board)
                    new_board[i][j] = self.player
                    new_player = 0
                    if self.player == Tic_Tac_Toe.PLAYER_X:
                        new_player = Tic_Tac_Toe.PLAYER_O
                    else:
                        new_player = Tic_Tac_Toe.PLAYER_X
                    new_tic = Tic_Tac_Toe(new_board, new_player)
                    sucessors.append(new_tic)
        return sucessors

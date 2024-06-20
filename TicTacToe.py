from game import *

class TicTacToe(Game):
    def __init__(self, board=['-','-','-','-','-','-', '-','-','-']):
         moves = []
         for i in range( len(board) ) :
            if board[i] == '-' :
                moves.append((i, 'O' ))        
         self.initial = GameState(to_move = 'O', utility= 0,  board = board, moves=moves)
    
    def actions(self, state):
         return state.moves

    def result(self, state, move):
       board = list(state.board)
       board[move[0]] = move[1]
       to_move = 'X' if state.to_move == 'O' else 'O'
       moves = []
       for i in range( len(board) ) :
                if board[i] == '-' :
                    moves.append((i, to_move ))
       new_state = GameState(to_move, state.utility, board, moves)
       util = self.utility(new_state, state.to_move) 
       return GameState(to_move, util, board, moves)

    def utility(self, state, player):
        if self.terminal_test(state) :
            board = state.board
            current = []
            for row in range(0,3) :
                for column in range(0, 3) :
                    current.append(board[column +  3*row])
                if all(i == current[0] for i in current)  and '-' not in current  :
                    return 1 if current[0] == 'X' else -1
                current.clear()
            for column in range(0, 3) :
                for row in range(0,3)  :
                    current.append(board[column  + 3*row])   
                if all(i == current[0] for i in current)  and '-' not in current  :
                     return 1 if current[0] == 'X' else -1
                current.clear()
            current = [board[0], board[4], board[8]]
            if all(i == current[0] for i in current)  and '-' not in current  : 
                 return 1 if current[0] == 'X' else -1
            current = [board[2], board[4], board[6]]
            if all(i == current[0] for i in current)  and '-' not in current  : 
                 return 1 if current[0] == 'X' else -1
        return 0

    def terminal_test(self, state):
        """A state is terminal if there are no objects left"""
        board = state.board
        current = []
        for row in range(0,3) :
            for column in range(0, 3) :
                current.append(board[column +  3*row])
            if all(i == current[0] for i in current)  and '-' not in current  :
                return True
            current.clear()
        for column in range(0, 3) :
            for row in range(0,3)  :
              current.append(board[column  + 3*row])   
            if all(i == current[0] for i in current)  and '-' not in current  :
                return True
            current.clear()
        current = [board[0], board[4], board[8]]
        if all(i == current[0] for i in current)  and '-' not in current  : 
            return True
        current = [board[2], board[4], board[6]]
        if all(i == current[0] for i in current)  and '-' not in current  : 
            return True
        return len(state.moves) == 0

    def display(self, state):
        board = state.board
        print("board: ")
        print(board[0] + "|" + board[1] + "|" + board[2])
        print(board[3] + "|" + board[4] + "|" + board[5])
        print(board[6] + "|" + board[7] + "|" + board[8])

 
if __name__ == "__main__":
   game = TicTacToe()
   game.play_game(query_player, alpha_beta_player)
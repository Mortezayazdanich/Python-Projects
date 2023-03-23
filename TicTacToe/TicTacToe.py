import random

class Game:
    def __init__(self):
        self.board = []
    
    def create_board(self):
        for i in range(0,3):
            row = []
            for j in range(0,3):
                row.append("_")
            self.board.append(row)
    
    def is_filled(self):
        for row in self.board:
            for item in row:
                if item == "_":
                    return False
        return True
    
    def player_select(self):
        return random.randint(0, 1)

    def draw(self, player, row, col):
        self.board[row][col] = player

    
    def is_valid(self, row, col):
        if (row < 0 or row >= 3) and (col < 0 or col >= 3):
            return False
        elif self.board[row][col] != "_":
            return False
        else:
            return True

    def swap_player(self, player):
        if player == "O":
            self.player_select() == 1
            return "X"
        else:
            self.player_select() == 0
            return "O"
        

    def player_won(self, player):
        #Checking Rows:
        for i in range(0,3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
        #Checking cols:
        for i in range(0,3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True
        #Checking Diagonal:
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True

    def show_board(self):
        for i in range(0,3):
            for j in range(0,3):
                print(self.board[i][j], end=" ")
            print("")

    def start(self):
        self.create_board()
        print("Welcome to the game of Tic Tac Toe!")
        print("")
        player = 'X' if self.player_select() == 1 else 'O'
        while True:
            self.show_board()
            if self.is_filled():
                print("Game over! Tie game!")
                break

            row, col = input("please enter row and column:").split()
            while not self.is_valid(int(row)-1, int(col)-1):
                print("Wrong Input!")
                row, col = input("please enter row and column:").split()

            self.draw(player, int(row)-1, int(col)-1)
            

            if self.player_won(player):
                print("Player " + player + " has won!")
                self.show_board()
                break

            player = self.swap_player(player)


game = Game()
game.start()

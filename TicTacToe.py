#
# CHRISTIAN RIVA
# EWA GIERLACH
#
#
import numpy as np

class TicTacToe:
    board = [[" " for i in range(3)] for j in range(3)]
    player1_name = "Player1"
    player2_name = "Player2"
    player1_symbol = "X"
    player2_symbol = "O"
    next_player=0 #0:player1/player2, 1:player1, 2:player2

    def ask_for_name(self, name1, name2):
            self.player1_name = name1
            self.player2_name = name2

    def set_position(self,symbol):
        print("Where to put your symbol?")
        x = int(input(""))
        y = int(input(""))
        if x > 2 or x < 0 or y > 2 or y < 0:
            print("Give the number in range (0,2) and press Enter! Try again\n")
            self.set_position(symbol)
            return 0
        if self.board[x][y] == " ":
            self.board[x][y] = symbol
            return 1
        else:
            print("Wrong position! Try again\n")
            self.set_position(symbol)
            return 0

    def print_board(self):
        for i in self.board:
            for j in i:
                print('|'+j, end='', flush=True)
            print('|\n')

    def the_end(self):
        a = self.board
        tab = np.reshape(a, 9)
        if " " not in tab:
            print("The match ended in a tie!")
            return 0
        if a[0][0] == 'O' and a[1][1] == 'O' and a[2][2] == 'O':
            print("Congratulations " + self.player2_name + "! You won!")
            return 0
        if a[2][0] == 'O' and a[1][1] == 'O' and a[0][2] == 'O':
            print("Congratulations " + self.player2_name + "! You won!")
            return 0
        if a[0][0] == 'X' and a[1][1] == 'X' and a[2][2] == 'X':
            print("Congratulations " + self.player1_name + "! You won!")
            return 0
        if a[2][0] == 'X' and a[1][1] == 'X' and a[0][2] == 'X':
            print("Congratulations " + self.player1_name + "! You won!")
            return 0
        for i in range(0, 3):
            if a[0][i] == 'X' and a[1][i] == 'X' and a[2][i] == 'X':
                print("Congratulations "+self.player1_name+"! You won!")
                return 0
            if a[i][0] == 'X' and a[i][1] == 'X' and a[i][2] == 'X':
                print("Congratulations " + self.player1_name + "! You won!")
                return 0
            if a[0][i] == 'O' and a[1][i] == 'O' and a[2][i] == 'O':
                print("Congratulations " + self.player2_name + "! You won!")
                return 0
            if a[i][0] == 'O' and a[i][1] == 'O' and a[i][2] == 'O':
                print("Congratulations " + self.player2_name + "! You won!")
                return 0
        return 1

    def game(self):
        text1 = "Welcome first player! What's your name?\n"
        text2 = "Welcome second player! What's your name?\n"
        self.ask_for_name(input(text1), input(text2))
        print(self.player1_name + " your turn!")
        self.set_position(self.player1_symbol)
        self.print_board()
        while self.the_end():
            print(self.player2_name + " your turn!")
            self.set_position(self.player2_symbol)
            self.print_board()
            if self.the_end():
                print(self.player1_name+ " your turn!")
                self.set_position(self.player1_symbol)
                self.print_board()


if __name__ == '__main__':
    game1 = TicTacToe()
    game1.game()

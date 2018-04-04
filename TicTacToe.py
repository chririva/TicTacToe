#
# CHRISTIAN RIVA
# EWA GIERLACH
#
#
from tabulate import tabulate

class TicTacToe:
    def __init__(self, ):
        self.player1_name = "Player1"
        self.player2_name = "Player2"
        self.player1_symbol = 'X'
        self.player2_symbol = 'O'
        self.next_player=0; #0:player1/player2, 1:player1, 2:player2
        self.battlefield=[["","",""],["","",""],["","",""]]
       
    def set_name_player1(self,name):
        self.player1_name = name

    def set_name_player2(self,name):
        self.player2_name = name

    def get_name_player1(self):
        return self.player1_name

    def get_name_player2(self):
        return self.player2_name

    def get_symbol_player1(self):
        return self.player1_symbol

    def get_symbol_player2(self):
        return self.player2_symbol

    def set_symbol1(self,symbol):
        changed = True
        if symbol != self.player2_symbol:
            self.player1_symbol = symbol
        else:
            changed = False
        return changed
    def set_symbol2(self,symbol):
        changed = True
        if symbol != self.player1_symbol:
            self.player2_symbol = symbol
        else:
            changed = False
        return changed
    def print_battlefield(self):
        print(tabulate(self.battlefield,tablefmt="grid"))

    def is_free(self,location):
        free = True
        if location == 1 and self.battlefield[0][0] != "":
            free = False
        elif location == 2 and self.battlefield[0][1] != "":
            free = False
        elif location == 3 and self.battlefield[0][2] != "":
            free = False
        elif location == 4 and self.battlefield[1][0] != "":
            free = False
        elif location == 5 and self.battlefield[1][1] != "":
            free = False
        elif location == 6 and self.battlefield[1][2] != "":
            free = False
        elif location == 7 and self.battlefield[2][0] != "":
            free = False
        elif location == 8 and self.battlefield[2][1] != "":
            free = False
        elif location == 9 and self.battlefield[2][1] != "":
            free = False
        return free


    def put_choice(self,player,location):
        symbol_of_the_player=self.player1_symbol
        if player == 2:
            symbol_of_the_player = self.player2_symbol
        if player == self.next_player or self.next_player == 0:
            if self.is_free(location):
                if location == 1:
                    self.battlefield[0][0] = symbol_of_the_player
                elif location == 2:
                    self.battlefield[0][1] = symbol_of_the_player
                elif location == 3:
                    self.battlefield[0][2] = symbol_of_the_player
                elif location == 4:
                    self.battlefield[1][0] = symbol_of_the_player
                elif location == 5:
                    self.battlefield[1][1] = symbol_of_the_player
                elif location == 6:
                    self.battlefield[1][2] = symbol_of_the_player
                elif location == 7:
                    self.battlefield[2][0] = symbol_of_the_player
                elif location == 8:
                    self.battlefield[2][1] = symbol_of_the_player
                elif location == 9:
                    self.battlefield[2][2] = symbol_of_the_player

    #def status_of_the_match(self):
        #0
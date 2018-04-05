#
# CHRISTIAN RIVA
# EWA GIERLACH
#
#
from TicTacToe import TicTacToe
from tabulate import tabulate
import time

print("TIC TAC TOE GAME")

game=TicTacToe()


#NUMBER OF PLAYERS
while True:
    num_players = int(input("How many players?"))
    if num_players == 1 or num_players == 2:
        break
    print("You can chose only 1 or 2 players.")


if num_players == 1:
    print("NOT IMPLEMENTED YET")
elif num_players == 2:
    game.set_name_player1(input("Player1, what's your name?"))
    game.set_name_player2(input("Player2, what's your name?"))
    print(game.get_name_player1()+" is playing with sign: " + game.get_symbol_player1())
    print(game.get_name_player2() + " is playing with sign: " + game.get_symbol_player2())
    #time.sleep(1)




game.print_battlefield()
game.put_choice(2,4)
game.put_choice(1,5)
game.put_choice(1,6)
game.put_choice(1,1)
game.put_choice(2,2)
game.put_choice(2,3)
game.put_choice(1,7)
game.put_choice(2,8)
game.put_choice(2,9)
game.print_battlefield()

print(game.status_of_the_match())
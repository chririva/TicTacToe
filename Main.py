#
# CHRISTIAN RIVA
# EWA GIERLACH
#
#
from TicTacToe import TicTacToe
print("\n ***** TIC TAC TOE GAME *****\n")

game = TicTacToe()
game.set_name_player1(input("Player1, what's your name?"))
game.set_name_player2(input("Player2, what's your name?"))
print(game.get_name_player1()+" is playing with sign: " + game.get_symbol_player1())
print(game.get_name_player2() + " is playing with sign: " + game.get_symbol_player2())

while True:
    game.print_battlefield()
    if game.get_next() == 1:
        while True:
            choice = int(input(game.get_name_player1() + " it's your turn. put your choice (1-9): "))
            if game.is_free(choice):
                game.put_choice(1, choice)
                break
            print("That position is already taken")
    else:
        while True:
            choice = int(input(game.get_name_player2() + " it's your turn. put your choice (1-9): "))
            if game.is_free(choice):
                game.put_choice(2, choice)
                break
            print("That position is already taken")

    if game.status_of_the_match() != 0:
        break

game.print_battlefield()

if game.status_of_the_match() == 1:
    print(game.get_name_player1()+" won this match.")
elif game.status_of_the_match() == 2:
    print(game.get_name_player2() + " won this match.")
elif game.status_of_the_match() == 3:
    print("Nobody won this match ¯\_(ツ)_/¯ ")


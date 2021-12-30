"""
EVERY USER SUPPOSE TO CHOOSE AS A 1,2 OR 0,1
"""

def choose_side():
    while True:
        player1 = input("Player1, please choose your side (either X or O): ")
        if player1 == "X" or player1 == "O":
            return player1

def display_enviroment(field):
    timerr = 0
    for i in field:
        timer = -1
        for j in i:
            timer+=1
            if timer == 2:
                print(j,end="\n")
            else:
                print(j, end="|")
        if timerr <= 1:
            timerr += 1
            print("-+-+-")

def makechoice(choose):
    if choose == "1":
        player1_choice = input(f"Player{choose}, please make your choice: ").split(",")
        return player1_choice

    else:
        player2_choice = input(f"Player{choose}, please make your choice: ").split(",")
        return player2_choice

def implychoices(field,player_choice,player):
    player_choice = [int(x) for x in player_choice]
    chooseMap = field[player_choice[0]][player_choice[1]]
    if player == "X":
        if chooseMap == "O":
            while True:
                print(f"{player} is already in the location {player_choice[0]},{player_choice[1]}. Skipping this turn.")
                choose = makechoice(player)
                if field[int(choose[0])][int(choose[1])] == " ":
                    field[int(choose[0])][int(choose[1])] = "X"
                    return field
        else:
            field[player_choice[0]][player_choice[1]] = "X"
            return field

    elif player == "O":
        if chooseMap == "X":
            while True:
                print(f"{player} is already in the location {player_choice[0]},{player_choice[1]}. Skipping this turn.")
                choose = makechoice(player)
                if field[int(choose[0])][int(choose[1])] == " ":
                    field[int(choose[0])][int(choose[1])] = "O"
                    return field
        else:
            field[player_choice[0]][player_choice[1]] = "O"
            return field

def is_winner(field):
    if field[0][0] == field[0][1] and field[0][1] == field[0][2]:
        if field[0][0] == player1:
            return player1
        elif field[0][0] == player2:
            return player2
    elif field[1][0] == field[1][1] and field[1][0] == field[1][2]:
        if field[1][0] == player1:
            return player1
        elif field[1][0] == player2:
            return player2
    elif field[2][0] == field[2][1] and field[2][1] == field[2][2]:
        if field[2][0] == player1:
            return player1
        elif field[2][0] == player2:
            return player2
    elif field[0][0] == field[1][0] and field[1][0] == field[2][0]:
        if field[0][0] == player1:
            return player1
        elif field[0][0] == player2:
            return player2
    elif field[0][1] == field[1][1] and field[1][1] == field[2][1]:
        if field[0][1] == player1:
            return player1
        elif field[0][1] == player2:
            return player2
    elif field[0][2] == field[1][2] and field[1][2] == field[2][2]:
        if field[0][2] == player1:
            return player1
        elif field[0][2] == player2:
            return player2
    elif field[0][0] == field[1][1] and field[1][1] == field[2][2]:
        if field[0][0] == player1:
            return player1
        elif field[0][0] == player2:
            return player2
    elif field[0][2] == field[1][1] and field[1][1] == field[2][0]:
        if field[0][2] == player1:
            return player1
        elif field[0][2] == player2:
            return player2
    else:
        return False
def checkboard(field):
    for i in field :
        for j in i :
            if j == " ":
                return True
    return False
print("Welcome to the Tic-Tac-Toe Game!")
print("every player chooses should be 1,2 OR 0,1 \nFirst one ROW\nSecond one is Column")
player1 = choose_side()

if player1 == "X":
    player2 = "O"
else:
    player2 = "X"

field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
display_enviroment(field)

while True:
    player1_choice = makechoice("1")
    field = implychoices(field, player1_choice, player1)
    display_enviroment(field)
    if is_winner(field) == player1 or checkboard(field) == False:
        break

    player2_choice = makechoice("2")
    field = implychoices(field, player2_choice, player2)
    display_enviroment(field)
    if is_winner(field) == player2 or checkboard(field) == False:
        break

if checkboard(field) == False:
    print("The game is finished! It is a tie.")

else:
    if player1 == is_winner(field):
        print("Player1 has won the game!")

    else:
        print("Player2 has won the game!")

from random import choice



def computer_choice():
    selection_list = ['rock','paper','scissor']
    computer_select = choice(selection_list)
    print(computer_select)
    return computer_select

#print(pc)

def player_choice():
    player_select = input('Please choose from the selection: rock, paper, scissor\n')
    return player_select

def rock_paper_scissor():
    player = player_choice()
    pc = computer_choice()


    if (player == 'rock' and pc == 'scissor') or (player == 'paper' and pc == 'rock') or (player == 'scissor' and pc == 'paper'):
        print('Player is winner!')
    elif (player == 'scissor' and pc == 'scissor') or (player == 'rock' and pc == 'rock') or (player == 'paper' and pc == 'paper'):
        print('Outcome is a draw')
    else:
        print('Pc is winner!')




start = input('Welcome to my rock, paper, and scissor game. When you are ready enter start, to begin.\n')

while True:
    if start == 'start' or start == 'yes' or start == 'Yes':
        rock_paper_scissor()
        start = input('Do you wish to play again? Yes or No\n')
    elif start == 'No' or start == 'no':
        break
    else:
        break








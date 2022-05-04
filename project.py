import random

def win():
    print('You win.')

def lost():
    print('You lost.')

def draw():
    print('Its a draw.')

def the_game():
    
    moves = ['rock', 'paper', 'scissors']

    print('rock, paper, scissors?')
    while True:

        player = input('Player: ')
        if player not in moves:
            print('Invalid Option.')
        else:
            computer = random.choice(moves)
            print(f'Computer: {computer}')

            if player == computer:
                draw()
            elif player == 'rock' and computer == 'scissors':
                win()
            elif player == 'rock' and computer == 'paper':
                lost()
            elif player == 'paper' and computer == 'rock':
                win()
            elif player == 'paper' and computer == 'scissors':
                lost()
            elif player == 'scissors' and computer == 'paper':
                win()
            elif player == 'scissors' and computer == 'rock':
                lost()
            else:
                pass

            play_again = input('Retry? (y/n): ')
            if play_again == 'y':
                the_game()
            elif play_again == 'n':
                print('Game Over.')
            else:
                print('Invalid Option.')

the_game()
import random

user_wins=0
comp_wins=0
options=['rock', 'paper', 'scissors']

while True:

    user_pick = input('pick rock/paper/scissors or quit: ').lower()
    comp_pick = options[random.randint(0,2)]

    if user_pick == 'quit':
        print('you won: ', user_wins,  ' times')
        print('computer won: ', comp_wins, ' times')
        break
    if user_pick not in options:
        print('Enter a valid option')
        continue
    
    print(comp_pick)

    if user_pick=='rock' and comp_pick=='scissors':
        print('You win!')
        user_wins+=1
    elif user_pick=='paper' and comp_pick=='rock':
        print('You win!')
        user_wins+=1
    elif user_pick=='scissors' and comp_pick=='paper':
        print('You win!')
        user_wins+=1
    elif user_pick == comp_pick:
        print('Draw.')
    else:
        print('You lost!')
        comp_wins+=1



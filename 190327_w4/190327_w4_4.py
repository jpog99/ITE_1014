import random

def com():
    
    
    if com_choose == 0:
        return 'rock'
    elif com_choose == 1:
        return 'paper'
    else:
        return 'scissors'
    
def game():
    
    if p_choose == com():
        print("Draw!")
        global draw
        draw +=1
    
    elif p_choose == 'rock':
        if com() == 'paper':
            print('Lose!')
            global lose
            lose +=1
        else:
            print('Win!')
            global win
            win +=1
    
    elif p_choose == 'paper':
        if com() == 'rock':
            print('Win!')
            win +=1
        else:
            print('Lose!')
            lose +=1
        
    elif p_choose == 'scissors':
        if com() == 'rock':
            print('Lose!')
            lose +=1
        else:
            print('Win!')
            win +=1
            
playAgain = 'yes'
win = 0
lose = 0
draw = 0
rounds = 0

while playAgain == 'yes' or playAgain == 'y':
    rounds += 1
    com_choose  = random.randint(0,2)
    com()
    p_choose = input('Rock, Paper, Scissors?')
    
    game()
    playAgain = input('Again? (y/n)')

win = int(win)
rounds = int(rounds)
rate = win*100/rounds
print()
print('Results: '+str(win)+' wins, '+str(lose)+' lose,'+str(draw)+' draws.')
print('Winning rate: '+str(rate)+'%')
    
    

import random

inPlay = True
while inPlay:
    guessed = False
    haveDuplicate = True
    while haveDuplicate:
        secNumber = random.randint(000,999)
        secNumber = str(secNumber)
        secNumberarray = []
        for digit in secNumber:
            secNumberarray.append(digit)
        seen = []
        truSecNumber = []
        
        for idx in secNumberarray:
            if idx not in seen:
                truSecNumber.append(idx)
                seen.append(idx)
                haveDuplicate = False
            else:
                haveDuplicate = True
                break
        
    while not guessed:
        strike = 0
        ball = 0
        print('=======================')
        print(secNumber)
        playerNum = input('Guess numbers (000~999)\n')
        
        playerNum = str(playerNum)
        
        playerNumarray = []
        for digit in playerNum:
            playerNumarray.append(digit)
            
        for i in range (0,3):
            if truSecNumber[i] == playerNumarray[i]:
                strike += 1

            elif playerNumarray[i] in truSecNumber:
                ball +=1
        
        if strike == 3:
            guessed = True
            print ('Yes! the secret number is ' + secNumber)
        else:
            print('Ball: ', ball , '\tStrike: ' , strike)  
    
    restart = input('Wanna play again?')
    if restart != 'y':
        inPlay = False
        


        
    


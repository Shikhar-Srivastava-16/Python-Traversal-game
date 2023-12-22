'''
Gameplay:
    -Here, PlayerCode is accepted as argument
    -if PlayerCode goes to 36, it must be reset to 0, excess is added (DONE)
    -for corner tiles, consequences happen
    -for all other tiles, points change
'''

player1=0
player2=0
player3=0
player4=0
player5=0
player6=0

#for dice rolls:
import random

#for documentation of result
import csv

#Disadvantages on corner tiles
listConsBad={1:'Go to Start',
2:'cut down points by 1/5',
3:'Jump to tile 34',
4:'cut down points by 1/2'}

#advantages on corner tiles
listConsGood={1:'Jump to tile 10',
2:'Jump to tile 20',
3:'Jump to tile 30',
4:'Double Points'}


#Function for advantages on corner points
def gamePlay_cornerGood():
    global player
    
    print("Congratulations!")
    print("You will be gaining an advantage!")
    a=random.randint(1,4)
    print(listConsGood[a])            
    if a==1:
        player=10
        points_players[counter]+=10

    elif a==2:
        player=20
        points_players[counter]+=20

    elif a==3:
        player=30
        points_players[counter]+=30

    elif a==4:
        points_players[counter]*=2


#Function for disadvantages on corner points
def gamePlay_cornerBad():
    global player
    
    print("Boo Hoo!")
    print("You will be given a handicap...")
    print("Better Luck next time!")
    a=random.randint(1,4)        
    print(listConsBad[a])
    if a==1:
        player=0
        points_players[counter]+=10
    elif a==2:
        points_players[counter]=0.20*points_players[counter]              
    elif a==3:
        player=34
        points_players[counter]-=15
    elif a==4:
        points_players[counter]=0.50*points_players[counter]

    
#Reset Code on Passing start
def gamePlay_resetCode(player):       
    print("Congratulations on passing start!")
    player=player-36
    return(player)


#checks for dice, then stores roll, then adds roll to player
def gamePlay_changePos(player):     
#Format
    print("If you have a dice, enter 'Yes' and use a dice and enter the roll.")
    print("If not, enter 'No' to use the randomiser in the game.")

#Checking for dice
    while True:
        VarDice=input("Enter Yes/No for dice input: ")

        #Dice present
        if VarDice.lower()=="yes":                               
            print("Roll your dice, please.")
            VarMove=int(input("Enter Dice Roll Here, only enter an integer: "))
            break

        #Dice Absent
        elif VarDice.lower()=='no':                                            
            VarMove=random.randint(1,6)
            print("Your Random Roll is: ", VarMove)
            break
        else:
            print("You Must Enter 'yes' or 'no' here.")
            continue
    print("Now the move will begin.")
    player+=VarMove
    return(player)


#Changing points
def gamePlay_Selector(player,a=0):

    '''
    a=0 indicates that corners consequences are to be implemented from this function
    a=1 indicates that consequences here should be ignored
    by default, a=0
    '''           

    global points_players
    global position_Players
    
    '''
    -enacts consequences based on pos number
    -then changes points
    '''
    dictPointChange={1:7,
    2:1,
    3:2,
    4:-2,
    5:3,
    6:1,
    7:1,
    8:1,
    9:None,
    10:10,
    11:-9,
    12:2,
    13:-5,
    14:1,
    15:4,
    16:5,
    17:6,
    18:None,
    19:-2,
    20:20,
    21:4,
    22:5,
    23:-1,
    24:4,
    25:-6,
    26:3,
    27:None,
    28:5,
    29:-1,
    30:30,
    31:5,
    32:-2,
    33:10,
    34:-15,
    35:7}

    #To enact the consequences at tiles 9,18 and 27
    if player%9==0:
        if a==0: 
            print("Consequence time!")       
            VarConsA=random.randint(0,2)
            if VarConsA!=0:
                #run function for good corner
                gamePlay_cornerGood()

            else:
                gamePlay_cornerBad()

        elif a==1:
            pass

        else: 
            #Raises error for a value of a other than 1 or 0 
            raise SyntaxError
                
    else:
        print("Point Changes: ")
        print(dictPointChange[player],"is your point change.")
        pointChange=dictPointChange[player]             
        points_players[counter]+=pointChange
        

#function for saving the file at the end of the game
def save(filename): 
    global counter
    global position_Player 
    global points_players
    
    with open(filename,'w',newline='') as f:
        writer=csv.writer(f)      
        for i in range(counter):
            print('For Player',i+1)
            name=input("Enter first name: ")
            surname=input("Enter last name: ")
            points= points_players[i]
            rec=[name,surname,points]
            writer.writerow(rec)
    print("data saved")
      


'''
In case of the entire program being run independently: 
    1) the conditional construct below checks if the file is used independently
    2) if the construct returns true, the code for the game is run individually
    3) if the construct returns false, the code for the game is used as a module
    4) if if is used as a module, the logic for the minigame does not run    
'''


if __name__=="__main__":
    while True:
        try:
            numPlayers=int(input("Enter no of Players, between 2 & 6: "))
            if not numPlayers in (2,3,4,5,6):
                print("invalid input")
                continue

        except:
            print("invalid input")
            continue
        
        break
    if numPlayers==2:
        position_Players=[player1,player2]
        points_players=[0,0]

    elif numPlayers==3:
        position_Players=[player1,player2,player3]
        points_players=[0,0,0]

    elif numPlayers==4:
        position_Players=[player1,player2,player3,player4]
        points_players=[0,0,0,0]

    elif numPlayers==5:
        position_Players=[player1,player2,player3,player4,player5]
        points_players=[0,0,0,0,0]

    elif numPlayers==6:
        position_Players=[player1,player2,player3,player4,player5,player6]
        points_players=[0,0,0,0,0,0]
        
    else:
        pass


    while True:
        counter=0
        for player in position_Players:       
            player=gamePlay_changePos(player)
            if player>=36:
                player=gamePlay_resetCode(player)
            print('Tile Number: ',player)
            gamePlay_Selector(player)
            #ammend record
            counter+=1
        try:        
            interrupt=input("hit any key to continue, hit ctrl+d to exit")
        except:
            f_name= input("Enter filename: ")
            save(f_name)
            print("Thank You For Playing!")
            break


#If imported into another program as a module
else:
    pass
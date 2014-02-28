"""
write and play music for diferent scenarios / have sound effects
-Game title
    new game
        creating a new character
        creating a new text file to save to
    load game
        making sure the file exists
        opening and reading the file
        saving to the file
    About section
        explaining what the game is, who made it, how to play
        returns to game tile after you are done

Save game file:

    Character Class
        with Name
             Department
             Hand
             Stats(Power, spin, Accuracy, Defense, Term, Level, EXP)
    Locations completed / people defeated
    current location
        building
        floor
        room#/lab/lobby/hallway

battle
    ADTRAN employee class
        work experience colected from beating him
        things they say
    make ping pontable drawings that have the ball moving accros them
    have stats return to normal afterward
    exploding large words for battle effects

level up
    accumulate experiance points
    get stat boosts
Changes terms
    new department, new location


have different enemies of increasing dificulty
have options inbetween battles like which halls to go down or which rooms to enter
concer different sections of adtran
    start in either north or south and change buildings each term
challange techs - engineers - scrum masters- managers - department heads - VP's
eventualy challange tom stanton to ping pong
Adtrantum as a hall roaming boss
ghost-ops
Rival like pokemon

Save file template:
Name
Deparment
Stats: Power Spin Accuracy Defense Term Level EXP
Locations completed
Current location
"""
import os
import time
import random
from DrawTable import *

def main():
    
##    x = Character("Spencer", "Hardware", "left", [100,100,100,100,1,1,0])
##    y = Character("Tom", "CEO","right", [100,100,100,100,1,1,0])
##    Battle(x,y,2)
##    input(">")

    Save_file = GameTitle()
    Player, Rival = LoadCharacters(Save_file)
    input("this is how far you have gotten")
    
    
    #make a room , floor, building, class
    #make a ADTRAN class that knows where you are
    #make a loadSetting() function that makes an adtran object


##################################################################################################################################################################################################
##################################################################################################################################################################################################
##################################################################################################################################################################################################
##################################################################################################################################################################################################
##################################################################################################################################################################################################
##################################################################################################################################################################################################
##################################################################################################################################################################################################
##################################################################################################################################################################################################
##################################################################################################################################################################################################
##################################################################################################################################################################################################

    
#Takes two character objects and plays a ping pong match but calls it a battle
#in order to be more like pokemon
#Returns True if you win and False if you lose
def Battle(Player, Opponent, Game_to):
    myScore = 0
    oppScore = 0
    myHand = Player.getHand()
    oppHand = Opponent.getHand()

    # better intro
    os.system('cls')
    print(Player.getName(), "has been introduced to", Opponent.getName())
    print('It\'s time for the ping pong match of the century')
    input(">") 

    PlayerServe = PING(Player.getAccuracy(),Opponent.getAccuracy())

    #regurlar play
    while myScore < Game_to-1 and oppScore < Game_to-1:
              
        if PlayerServe:
            if UserServe(Player, Opponent):
               myScore += 1
            else:
                oppScore +=1
        else:
            if ComputerServe(Player, Opponent):
               myScore += 1
            else:
                oppScore +=1

        if (myScore + oppScore) % 5 == 0:
            PlayerServe = not PlayerServe

        os.system('cls')
        DrawTable()
        print("Score:","\t",Player.getName(),myScore,"\t", Opponent.getName(),oppScore)
        input(">") 

    #Game point and beyond
    os.system('cls')
    DrawTable()
    print("Game Point")
    input(">") 
    if myScore > oppScore:
        PlayerServe = False
        #ComputerServe(Player, Opponent)
    else:
        PlayerServe = True
        #UserServe(Player, Opponent)

    if PlayerServe:
        if UserServe(Player, Opponent):
            myScore += 1
        else:
            oppScore +=1
    else:
        if ComputerServe(Player, Opponent):
            myScore += 1
        else:
            oppScore +=1

        os.system('cls')
        DrawTable()
        print("Score:","\t",Player.getName(),myScore,"\t", Opponent.getName(),oppScore)
        input(">") 
    
    while myScore -2 < oppScore and oppScore -2 < myScore:
        if myScore == oppScore:
            os.system('cls')
            DrawTable()
            print("Duce!")
            input(">") 
            PlayerServe = not PlayerServe
                
        elif myScore -1 == oppScore:
            os.system('cls')
            DrawTable()
            print("Advantage",Player.getName())
            input(">") 
            PlayerServe = False
                
        elif oppScore -1 == myScore:
            os.system('cls')
            DrawTable()
            print("Advantage",Opponent.getName())
            input(">") 
            PlayerServe = True


        if PlayerServe:
            if UserServe(Player, Opponent):
                myScore += 1
            else:
                oppScore +=1
        else:
            if ComputerServe(Player, Opponent):
                 myScore += 1
            else:
                oppScore +=1

    if myScore > oppScore:
        os.system('cls')
        DrawTable()
        print("Score:","\t",Player.getName(),myScore,"\t", Opponent.getName(),oppScore)
        print()
        print(Player.getName(), "Wins the Match!")
        input(">") 
        return True
    else:
        os.system('cls')
        DrawTable()
        print("Score:","\t",Player.getName(),myScore,"\t", Opponent.getName(),oppScore)
        print()
        print("sucks to suck")
        print(Opponent.getName(), "Wins the Match :(")
        input(">")
        return False
        
           
    # incorporate stats into chance hit reults and chance defense
    # make side of the table / fore hand or back hand matter
    # make computer opponent do reandom or starigic stat changes
    #DrawTable()    have different shots for it it's high power or high spin
    #un-comment PrintPing()
   


    #Exicutes a user serve and returns a bool to indicate if the user got the point
    #recursivly calls itself or oppHit() to continue the point
def UserServe(Player, Opponent):
    random.seed()
    os.system('cls')
    DrawTable()
    print(Player.getName(),"Serves")
    input(">") 
    #Power Spin Accuracy Defense Term Level EXP
    myStats = Player.getStats()
    oppStats = Opponent.getStats()

    os.system('cls')
    DrawTable()
    print("Power")
    userPower = input(">")

    if userPower == "":
        userPower = 0
    
    flag = True
    while flag:
        try:
            userPower = int(userPower)
        except Exception as ex:
            os.system('cls')
            DrawTable()
            print("Value must be an integer")
            print("Re-enter Power")
            userPower = input(">")

            if userPower == "":
                userPower = 0
            
        else:
            flag = False

            if userPower < round(myStats[2]*(-1/3)) or userPower > round(myStats[2]*(1/3)):
                flag = True

                os.system('cls')
                DrawTable()
                print("Value out of bounds")
                print("Re-enter Power between",round(myStats[2]*(-1/3)),"and", round(myStats[2]*(1/3)))
                userPower = input(">")
                if userPower == "":
                    userPower = 0

    os.system('cls')
    DrawTable()
    print("Spin")
    userSpin = input(">")
    
    if userSpin == "":
        userSpin = 0
    
    flag = True
    while flag:
        try:
            userSpin = int(userSpin)
        except Exception as ex:
            os.system('cls')
            DrawTable()
            print("Value must be an integer")
            print("Re-enter Spin")
            userSpin = input(">")

            if userSpin == "":
                userSpin = 0
            
        else:
            flag = False

            if userSpin < round(myStats[2]*(-1/3)) or userSpin > round(myStats[2]*(1/3)):
                flag = True

                os.system('cls')
                DrawTable()
                print("Value out of bounds")
                print("Re-enter Spin between", round(myStats[2]*(-1/3)),"and", round(myStats[2]*(1/3)))
                userSpin = input(">")

                if userSpin == "":
                    userSpin = 0

    os.system('cls')
    DrawTable()
    print("Side of the Table")
    userSide = input(">")

    while userSide != "right" and userSide != "left":
        #userSide = input(">")

        if userSide == "Left" or userSide == "l" or userSide == "L":
            userSide = "left"
        elif userSide == "Right" or userSide == "r" or userSide == "R":
            userSide = "right"

        if userSide != "right" and userSide != "left":
            os.system('cls')
            DrawTable()
            print("invalid direction slilly goose, type right or left")
            userSide = input(">")


          #your input boosts power and spin the cost of accuracy
          #you don't get the full benefit from the boosts. some fraction
    myStats[0] = myStats[0] + (userPower*3/4)
    myStats[1] = myStats[1] + (userSpin*3/4)
    myStats[2] = myStats[2] - userPower - userSpin

    #bassed on accuracy, go short, long, let, hit
    chance = random.random()*1000
    if chance < 800:
        if Player.getHand() == "right" and userSide == 'right':
            DrawShot('User','rsr')
        elif Player.getHand() == "right" and userSide == 'left':
            DrawShot('User','rsl')
        elif Player.getHand() == "left" and userSide == 'right':
            DrawShot('User','lsr')
        elif Player.getHand() == "left" and userSide == 'left':
            DrawShot('User','lsl')
        else:
            print('error talk to spencer')

        print(Player.getName(),"serves to the",userSide,"side of the table")
        input(">")
        return ComputerHit(Player, Opponent, myStats[0], myStats[1], userSide)

    elif chance < 900:
        if Player.getHand() == "right" and userSide == 'right':
            DrawShot('User','rsr')
        elif Player.getHand() == "right" and userSide == 'left':
            DrawShot('User','rsl')
        elif Player.getHand() == "left" and userSide == 'right':
            DrawShot('User','lsr')
        elif Player.getHand() == "left" and userSide == 'left':
            DrawShot('User','lsl')
        else:
            print('error talk to spencer')
        print("Let, re-serve")
        input(">") 
        return UserServe(Player, Opponent)

    elif chance < 950:
        os.system('cls')
##        if Player.getHand() == "right" and userSide == 'right':
##            DrawShot('User','rsrn')
##        elif Player.getHand() == "right" and userSide == 'left':
##            DrawShot('User','rsln')
##        elif Player.getHand() == "left" and userSide == 'right':
##            DrawShot('User','lsrn')
##        elif Player.getHand() == "left" and userSide == 'left':
##            DrawShot('User','lsln')
##        else:
##            print('error talk to spencer')
        print("You missed and hit the ball into the net")
        input(">") 
        return False
    
    else:
        os.system('cls')
##        if Player.getHand() == "right" and userSide == 'right':
##            DrawShot('User','rsrm')
##        elif Player.getHand() == "right" and userSide == 'left':
##            DrawShot('User','rslm')
##        elif Player.getHand() == "left" and userSide == 'right':
##            DrawShot('User','lsrm')
##        elif Player.getHand() == "left" and userSide == 'left':
##            DrawShot('User','lslm')
##        else:
##            print('error talk to spencer')
        print("You missed the table long")
        input(">") 
        return False
    


    #Exicutes a computer serve and returns a bool to indicate if the user got the point
    # recursivly calls itself or PlayerHit() to continue the point
def ComputerServe(Player, Opponent):
    random.seed()
    os.system('cls')
    DrawTable()
    print(Opponent.getName(),"Serves")
    input(">") 
    #Power Spin Accuracy Defense Term Level EXP
    myStats = Player.getStats()
    oppStats = Opponent.getStats()

    if random.random() < .5:
        compSide = "left"
    else:
        compSide = "right"

    #bassed on accuracy, go short, long, let, hit                         
    chance = random.random()*1000
    if chance < 800:
        if Opponent.getHand() == "right" and compSide == 'right':
            DrawShot('Opp','rsr')
        elif Opponent.getHand() == "right" and compSide == 'left':
            DrawShot('Opp','rsl')
        elif Opponent.getHand() == "left" and compSide == 'right':
            DrawShot('Opp','lsr')
        elif Opponent.getHand() == "left" and compSide == 'left':
            DrawShot('Opp','lsl')
        else:
            print('erros talk to spencer') 
        print(Opponent.getName(),"serves to the",compSide,"side of the table")
        input(">") 
        return UserHit(Player, Opponent, oppStats[0], oppStats[1], compSide)

    elif chance < 900:
        if Opponent.getHand() == "right" and compSide == 'right':
            DrawShot('Opp','rsr')
        elif Opponent.getHand() == "right" and compSide == 'left':
            DrawShot('Opp','rsl')
        elif Opponent.getHand() == "left" and compSide == 'right':
            DrawShot('Opp','lsr')
        elif Opponent.getHand() == "left" and compSide == 'left':
            DrawShot('Opp','lsl')
        else:
            print('erros talk to spencer')
        print("Let, re-serve")
        input(">") 
        return ComputerServe(Player, Opponent)

    elif chance < 950:
        os.system('cls')
##        if Opponent.getHand() == "right" and compSide == 'right':
##            DrawShot('Opp','rsrn')
##        elif Opponent.getHand() == "right" and compSide == 'left':
##            DrawShot('Opp','rsln')
##        elif Opponent.getHand() == "left" and compSide == 'right':
##            DrawShot('Opp','lsrn')
##        elif Opponent.getHand() == "left" and compSide == 'left':
##            DrawShot('Opp','lsln')
##        else:
##            print('erros talk to spencer')
        print(Opponent.getName(),"hit the ball into the the net")
        input(">") 
        return True
    else:
        os.system('cls')
##        if Opponent.getHand() == "right" and compSide == 'right':
##            DrawShot('Opp','rsrm')
##        elif Opponent.getHand() == "right" and compSide == 'left':
##            DrawShot('Opp','rslm')
##        elif Opponent.getHand() == "left" and compSide == 'right':
##            DrawShot('Opp','lsrm')
##        elif Opponent.getHand() == "left" and compSide == 'left':
##            DrawShot('Opp','lslm')
##        else:
##            print('erros talk to spencer')
        print(Opponent.getName(),"missed the table long")
        input(">") 
        return True
    
    

    #Recursivly workes with OpponentHit to play a point of ping pong
    #use player defense vs opponent power to see if you hit the shot back
    #opponent Spin reduces player accuracy
def UserHit(Player, Opponent, oppPower, oppSpin, oppSide):
    random.seed()
    #Power Spin Accuracy Defense Term Level EXP
    myStats = Player.getStats()
    oppStats = Opponent.getStats()

    if random.random() * 1000 < 100:
        os.system('cls')
        if oppSide == 'left':
            DrawTable('fl')
        else:
            DrawTable('fr')
        print("you weren't fast enough to return the shot")
        input(">") 
        return False

    os.system('cls')
    if oppSide == 'left':
        DrawTable('fl')
    else:
        DrawTable('fr')
    print("Power")
    userPower = input(">")

    if userPower == "":
        userPower = 0

    flag = True
    while flag:
        try:
            userPower = int(userPower)
        except Exception as ex:
            os.system('cls')
            if oppSide == 'left':
                DrawTable('fl')
            else:
                DrawTable('fr')
            print("Value must be an integer")
            print("Re-enter Power")
            userPower = input(">")

            if userPower == "":
                userPower = 0
            
        else:
            flag = False

            if userPower < round(myStats[2]*(-1/3)) or userPower > round(myStats[2]*(1/3)):
                flag = True

                os.system('cls')
                if oppSide == 'left':
                    DrawTable('fl')
                else:
                    DrawTable('fr')
                print("Value out of bounds")
                print("Re-enter Power between",round(myStats[2]*(-1/3)),"and", round(myStats[2]*(1/3)))
                userPower = input(">")
                if userPower == "":
                    userPower = 0

    os.system('cls')
    if oppSide == 'left':
        DrawTable('fl')
    else:
        DrawTable('fr')
    print("Spin")
    userSpin = input(">")

    if userSpin == "":
        userSpin = 0

    flag = True
    while flag:
        try:
            userSpin = int(userSpin)
        except Exception as ex:
            os.system('cls')
            if oppSide == 'left':
                DrawTable('fl')
            else:
                DrawTable('fr')
            print("Value must be an integer")
            print("Re-enter Spin")
            userSpin = input(">")

            if userSpin == "":
                userSpin = 0
            
        else:
            flag = False

            if userSpin < round(myStats[2]*(-1/3)) or userSpin > round(myStats[2]*(1/3)):
                flag = True
                os.system('cls')
                if oppSide == 'left':
                    DrawTable('fl')
                else:
                    DrawTable('fr')
                print("Value out of bounds")
                print("Re-enter Spin between",round(myStats[2]*(-1/3)),"and", round(myStats[2]*(1/3)))
                userSpin = input(">")

                if userSpin == "":
                    userSpin = 0

    os.system('cls')
    if oppSide == 'left':
        DrawTable('fl')
    else:
        DrawTable('fr')          
    print("Side of the Table")
    userSide = input(">")

    while userSide != "right" and userSide != "left":
        #userSide = input(">")

        if userSide == "Left" or userSide == "l" or userSide == "L":
            userSide = "left"
        elif userSide == "Right" or userSide == "r" or userSide == "R":
            userSide = "right"

        if userSide != "right" and userSide != "left":
            os.system('cls')
            if oppSide == 'left':
                DrawTable('fl')
            else:
                DrawTable('fr')
            print("invalid direction slilly goose, type right or left")
            userSide = input(">")
 
          #your input boosts power and spin the cost of accuracy
          #you don't get the full benefit from the boosts. some fraction
    
    myStats[0] = myStats[0] + (userPower*3/4)
    myStats[1] = myStats[1] + (userSpin*3/4)
    myStats[2] = myStats[2] - userPower - userSpin -(oppSpin*1/4)

     #bassed on accuracy, go short, long, let, hit
    chance = random.random()*1000
    if chance < 800:
        if oppSide == "right" and userSide == 'right':
            DrawShot('User','rhr')
        elif oppSide == "right" and userSide == 'left':
            DrawShot('User','rhl')
        elif oppSide == "left" and userSide == 'right':
            DrawShot('User','lhr')
        elif oppSide == "left" and userSide == 'left':
            DrawShot('User','lhl')
        else:
            print('error talk to spencer')
        print(Player.getName(),"returns the shot to the",userSide,"side of the table")
        input(">") 
        return ComputerHit(Player, Opponent, myStats[0], myStats[1], userSide)

    elif chance < 850:
        os.system('cls')
##        if oppSide == "right" and userSide == 'right':
##            DrawShot('User','rsr')
##        elif oppSide == "right" and userSide == 'left':
##            DrawShot('User','rsl')
##        elif oppSide == "left" and userSide == 'right':
##            DrawShot('User','lsr')
##        elif oppSide == "left" and userSide == 'left':
##            DrawShot('User','lsl')
##        else:
##            print('error talk to spencer')
        print("Skimed the edge of the table")
        input(">") 
        return True

    elif chance < 900:
        os.system('cls')
##        if oppSide == "right" and userSide == 'right':
##            DrawShot('User','rhrm')
##        elif oppSide == "right" and userSide == 'left':
##            DrawShot('User','rhlm')
##        elif oppSide == "left" and userSide == 'right':
##            DrawShot('User','lhrm')
##        elif oppSide == "left" and userSide == 'left':
##            DrawShot('User','lhlm')
##        else:
##            print('error talk to spencer')
        print("You missed the table long")
        input(">") 
        return False
    
    else:
        os.system('cls')
##        if oppSide == "right" and userSide == 'right':
##            DrawShot('User','rhrn')
##        elif oppSide == "right" and userSide == 'left':
##            DrawShot('User','rhln')
##        elif oppSide == "left" and userSide == 'right':
##            DrawShot('User','lhrn')
##        elif oppSide == "left" and userSide == 'left':
##            DrawShot('User','lhln')
##        else:
##            print('error talk to spencer')
        print("You missed and hit the ball into the net")
        input(">") 
        return False



    #recursivly works with PlayerHit to play a point of ping pong 
def ComputerHit(Player, Opponent, playerPower, playerSpin, playerSide):
    random.seed()
    #Power Spin Accuracy Defense Term Level EXP
    myStats = Player.getStats()
    oppStats = Opponent.getStats()

    if random.random() * 1000 < 100:
        os.system('cls')
        DrawTable()
        print(Opponent.getName(), "wasn't fast enough to return your shot")
        input(">") 
        return True

    if random.random() < .5:
        compSide = "left"
    else:
        compSide = "right"

    oppStats[2] -= playerSpin/4

    #bassed on accuracy, go short, long, let, hit
    chance = random.random()*1000
    if chance < 800:
        if playerSide == "right" and compSide == 'right':
            DrawShot('Opp','rhr')
        elif playerSide == "right" and compSide == 'left':
            DrawShot('Opp','rhl')
        elif playerSide == "left" and compSide == 'right':
            DrawShot('Opp','lhr')
        elif playerSide == "left" and compSide == 'left':
            DrawShot('Opp','lhl')
        else:
            print('erros talk to spencer')
        print(Opponent.getName(),"returns the shot to the",compSide,"side of the table")
        input(">") 
        return UserHit(Player, Opponent, oppStats[0], oppStats[1], compSide)

    elif chance < 850:
        os.system('cls')
##        if playerSide == "right" and compSide == 'right':
##            DrawShot('Opp','rhrs')
##        elif playerSide == "right" and compSide == 'left':
##            DrawShot('Opp','rhls')
##        elif playerSide == "left" and compSide == 'right':
##            DrawShot('Opp','lhrs')
##        elif playerSide == "left" and compSide == 'left':
##            DrawShot('Opp','lhls')
##        else:
##            print('erros talk to spencer')
        print("The ball scrapped the edge of the table")
        input(">") 
        return False
        
    elif chance+oppStats[2] < 900:
        os.system('cls')
##        if playerSide == "right" and compSide == 'right':
##            DrawShot('Opp','rhrn')
##        elif playerSide == "right" and compSide == 'left':
##            DrawShot('Opp','rhln')
##        elif playerSide == "left" and compSide == 'right':
##            DrawShot('Opp','lhrn')
##        elif playerSide == "left" and compSide == 'left':
##            DrawShot('Opp','lhln')
##        else:
##            print('erros talk to spencer')
        print(Opponent.getName(),"hit the ball into the the net")
        input(">") 
        return True
        
    else:
        os.system('cls')
##        if playerSide == "right" and compSide == 'right':
##            DrawShot('Opp','rhrm')
##        elif playerSide == "right" and compSide == 'left':
##            DrawShot('Opp','rhlm')
##        elif playerSide == "left" and compSide == 'right':
##            DrawShot('Opp','lhrm')
##        elif playerSide == "left" and compSide == 'left':
##            DrawShot('Opp','lhlm')
##        else:
##            print('erros talk to spencer')
        print(Opponent.getName(),"missed the table long")
        input(">") 
        return True

##################################################################################################################################################################################################
##################################################################################################################################################################################################
##################################################################################################################################################################################################
##################################################################################################################################################################################################
##################################################################################################################################################################################################
##################################################################################################################################################################################################
##################################################################################################################################################################################################
##################################################################################################################################################################################################
##################################################################################################################################################################################################
##################################################################################################################################################################################################



#uses player and oponent accuracy and random numbers to determin who serves first
#Returns true indicating Player serves or False indicating opponent serves.
def PING(playerAccuracy, oppAccuracy):
    random.seed()
    PingPrint()
    playerAccuracy = playerAccuracy * random.random()
    oppAccuracy = oppAccuracy * random.random()
    if playerAccuracy > oppAccuracy:
        return True
    else:
        return False
    


# opens the saved game file and returns a character object
def LoadCharacters(filename):
    try:
        file = open(filename,'r') 
    except IOError as ex:       
        print('Error in LoadCharacter(), save file did not open')
        input("")

    PlayerName = file.readline().strip("\n")
    PlayerDept = file.readline().strip("\n")
    PlayerHand = file.readline().strip("\n")
    PlayerStats = file.readline().strip("\n").split()
    current = file.readline().strip('\n')
    Completed_Locations = file.readline().strip('\n')
    RivalName = file.readline().strip('\n')
    RivalDept = file.readline().strip('\n')
    RivalHand = file.readline().strip('\n')
    RivalStats = file.readline().strip('\n').split()

    file.close()

    return Character(PlayerName, PlayerDept, PlayerHand, PlayerStats),Character(RivalName, RivalDept, RivalHand, RivalStats)
    
    
    
def LoadSetting(filename):
    print("not yet writen")
    


#Opens a text file "saves the game" then closes the file
def Save(filename, player, rival, current, loc_comp):
    file = open(filename,'w')
    #stats should come in as a list of stats in the order:
    #[power, spin, accuracy, defense, term, level, exp]
    playerStats_str = ""
    rivalStats_str = ""
    Completed_locations = ""
    
    for each in player.getStats():
        playerStats_str = playerStats_str + str(each) + " "

    for each in rival.getStats():
        rivalStats_str = rivalStats_str + str(each) + " "
        
    for each in loc_comp:
        Completed_locations = Completed_locations + " " + str(each)
        
    file.write(player.getName() + "\n" + player.getDept() + "\n" + player.getHand() + "\n" + playerStats_str + "\n" + current + "\n" + Completed_locations + "\n")
    file.write(rival.getName() + "\n" + rival.getDept() + "\n" + rival.getHand() + "\n" + rivalStats_str)
    file.close()



#Loads the title screen, prompts the user to make a new game or load a saved game from a text file.
def GameTitle():
    os.system('cls')
    time.sleep(.5)
    print ("Welcome to")
    time.sleep(1)
    print( "")
    print("      ___  ___________________________    ")
    print("     /   ||_______  _________________/  _ ")
    print("    / /| | / _  // // _  //_ | / __  | |_|"	)
    print("   / ___ |/ // // // , _//__ |/ / / /   _ "	)
    print("  /_/  |_/____/ \_/_/|_//_/|_/_/ /_/   |_|"	)
    print(" __________________________________________")
    print("")
    time.sleep(1)
    print("        ____________________________")
    print("       |_______  __________________/")
    print("              / // /_ / //___/      ")
    print("             / // /_ / // __/       ")
    print("             \_/_/  /_//___/        ")
    time.sleep(.3)
    print("      _______________________________")
    print("     |  ____________________________/")
    print("     | | ____/_ |  /  |  /  |/ /___  ")
    print("     | ||__  |_ | / | | / | |  ___/  ")
    print("     | |__/| || |/ /| |/ /| |/___    ")
    print("     |_______||_/_/ |___/ | |___/    ")
    print("")
    print("")
    time.sleep(1)

    while True:
        
        print("Type \"New\" to start a new game")
        print("Type \"Load\" to continue a saved game.")
        print("Type \"About\" to learn more about the game")
        user = input(">")
        print("\n")
        
        #New
        if user == "new" or user == "New":
            os.system('cls')
            print("Enter a name for your save file and remember it for next time")
            print("Make sure it ends in .txt")
            filename = input(">")                
            print("\n")
            
            Player,Rival = NewFirstTerm()
            Save(filename, Player, Rival, "Lobby", [])
            
            return filename
            
        #Load
        elif user == "Load" or user == "load":
            
            print("Enter the name of your saved file")
            print("make sure it ends in .txt")
            filename = input(">")
            print("\n")
            while (filename != "Back" and filename != "back"):
                try:
                    Load = open(filename,'r') 
                except IOError as ex:       
                    print('File not found, re-enter file name ')
                    print('or type \"Back\" to return to the title screen ')
                    filename = input(">")
                    print("\n")
                    
                else:
                    Load.close()
                    return filename
        #About       
        elif user == "About" or user == "about":
            aboutPage()

        else:
            print("Invalid input, please try again \n")
            time.sleep(1)


            
# This function prints the "About the Game" screen and then clears it afterward
def aboutPage():
    os.system('cls')
    time.sleep(.08)
    print(" This game was created by the collaboration of Austin Pinkerton, Liz Smith,\n Ryan Nichols, and Spencer Gass aka \"The Rabbit.\" In the hope of leaving a \n legacy greater and more memorable than their eating competition belt, \n this group of renegade 2nd termers pooled their individual talents to \n produce a game more challenging and more engaging than any of its kind. \n \n This strategy adventure game is set in ADTRAN\'s Huntsville campus. You \n begin the game by being accepted into the co-op program and then battling \n other ADTRAN employees in order to take control of different part of the \n company, and gain work experience. As you win battles you gain work \n experience, level up, and gain new skills. Over time you will make it through \n all 3 terms at ADTRAN and graduate from the co-op program. ")
    print("\n")
    input("Press enter to return to the tile screen")
    os.system('cls')
    


#Allows the user to create a new first term co-op 
def NewFirstTerm():
    name = ''
    otherName = ''
    
    os.system('cls')
    print("Hello there! Welcome to ADTRAN's Co-op program!")
    input(">")
    
    os.system('cls')
    print("I am an HR person, and I'm going to show you around!")
    input(">")
    
    os.system('cls')
    print("The Huntsville campus is full of electical engineers \nand software developers!")
    input(">")
    
    os.system('cls')
    print("Some employees don't take breaks. Others play ping pong!")
    input(">")
    
    os.system('cls')
    print("Myself...")
    input(">")
    
    os.system('cls')
    print("I do HR things and don't have time for ping pong.")
    input(">")
    
    while name == '':
        os.system('cls')
        print("First, what is your name?")
        name = input(">")
    
    os.system('cls')
    print("Right! so your name is " + name + "!")
    input(">")
    
    os.system('cls')
    print("This is another Co-op who has been your rival since you were a baby.")
    input(">")
    
    while otherName == '':
        os.system('cls')
        print("...Erm, whats his name again?")
        otherName = input(">")
    
    os.system('cls')
    print("Thats right I remember now! his name is " + otherName +  "!")
    input(">")
    
    os.system('cls')
    print(name + "! Your very own Co-op career is about to unfold!")
    input(">")
    
    os.system('cls')
    print("A world of dreams, adventures and Friday lunches awaits. \nLets go!")
    input(">")
    
    
    
    os.system('cls')
    print("WAIT! I almost forgot. It's unsafe, employees roam these halls.")
    input(">")
    
    os.system('cls')
    print("You need a ping pong paddle. Come with me!")
    input(">")
    
    os.system('cls')
    print("(In the HR office)")
    input(">")
    
    os.system('cls')
    print(otherName +": I'm bored, hurry up.")
    input(">")
    
    os.system('cls')
    print("HR: Just a minute " + otherName)
    input(">")
    
    os.system('cls')
    print("HR:",name,"are you left or right handed?")
    

    hand = ""
    while hand != "right" and hand != "left":
        hand = input(">")

        if hand == "Left" or hand == "l" or hand == "L":
            hand = "left"
        elif hand == "Right" or hand == "r" or hand == "R":
            hand = "right"

        if hand != "right" and hand != "left":
            os.system('cls')
            print("that's not a handedness silly goose, type right or left.")
    
    os.system('cls')
    print("HR: Here you are, your very own ping pong paddle!")
    input(">")
    
    os.system('cls')
    print("HR: Now it's time to choose the department you will work in for your \nfirst term.") 
    input(">")

    os.system('cls')
    print("Once you are a second or third termer you will have more \noptions but for now you have three. Choose!")
    input(">")
    
    while True:
        os.system('cls')
        print( "\n  1. Product Qualification\n  2. DVT\n  3. Tech Support\n")
        
        dept = input(">")
##        if dept == "1":
##            PQInfo()
##            continue
##        if dept == "2":
##            DVTInfo()
##            continue
##        if dept == "3":
##            TSInfo()
##            continue
        
        if dept == "Product Qualification" or dept == "product qualification" or dept == "PQ" or dept == "pq":
            PQInfo()
            os.system('cls')
            print("So you want to join the PQ team?")
            ans = input(">")
            if ans == 'yes' or ans == 'Yes' or ans == 'y' or ans == 'Y' or ans == "sure":
                NewPlayer = Character(name, "PQ", hand, [100,100,125,100,1,1,0])
                break
            else:
                os.system('cls')
                print("HR: Take your time.")
                input(">")
            
        
        if dept == "DVT" or dept == "dvt":
            DVTInfo()
            os.system('cls')
            print("Do you like the idea of testing our product\'s newest features?")
            ans = input(">")
            if ans == 'yes' or ans == 'Yes' or ans == 'y' or ans == 'Y' or ans == "sure":
                NewPlayer = Character(name, "DVT", hand, [125,125,75,100,1,1,0])
                break
            else:
                os.system('cls')
                print("HR: Take your time.")
                input(">")
            
        
        if dept == "Tech Support" or dept == "tech support" or dept == "TS" or dept == "ts":
            TSInfo()
            os.system('cls')
            print("Are you ready to man the phones?")
            ans = input(">")
            if ans == 'yes' or ans == 'Yes' or ans == 'y' or ans == 'Y' or ans == "sure":
                NewPlayer = Character(name, "Tech Support", hand, [75,75,100,150,1,1,0])
                break
            else:
                os.system('cls')
                print("HR: Take your time.")
                input(">")
                
    os.system('cls')
    print("Fantastic! I'm sure you will have a great time in", NewPlayer.getDept() + ".")
    input(">")
    
    os.system('cls')
    print(name,"got assigned to",NewPlayer.getDept() + ".")
    input(">")
    
    os.system('cls')
    print(otherName + ": I'll choose this one then!")
    input(">")
    
    

    if NewPlayer.getDept() == "PQ":
        NewRival = Character(otherName, "DVT", 'right', [125,125,75,100,1,1,0])
    elif NewPlayer.getDept() == "DVT":
        NewRival = Character(otherName, "Tech Support", 'right', [75,75,100,150,1,1,0])
    else:
        NewRival = Character(otherName, "PQ", 'right', [100,100,125,100,1,1,0])

    os.system('cls')
    print(otherName,"joined", NewRival.getDept() + ".")
    input(">")
    
    os.system('cls')
    print("HR: Alright time to get to work.")
    input(">")
    
    os.system('cls')
    print(otherName + ": Wait",name,"Let's play a quick game of ping pong!")
    input(">")
    Battle(NewPlayer,NewRival, 5)
    return NewPlayer,NewRival

        
# prints info for each department respectivly		 
def PQInfo():
    os.system('cls')
    print (" Department: Product Qualification\n")
    #print( " _______________________________________\n")
    #print( " Profile")
    #print( " _______________________________________")
    print( " Nickname: The Equalizer\n")
    print( "     Info: He/She is your standard first term Co-op with a" )
    print( "           Average Power, Spin and Defense but exceptional Acuracy. ")
    print( "           This Co-op is not the strongest, not the fastest, not  ")
    print( "           the smartest. However, what this Co-op lacks in stat ")
    print( "           variation, he/she makes up for it with determination.")
    #print( " _______________________________________\n")
    input(">")
    
def DVTInfo():
    os.system('cls')
    print( " Department: DVT\n")
    #print( " _______________________________________\n")
    #print( " Profile")
    #print( " _______________________________________")
    print( " Nickname: The Ghost\n")
    print( "     Info: Not much is known about this guy. We're not sure" )
    print( "           exactly what he does or what he's capable of. Also,")
    print( "           we don't think he does, either. Quick on his feet")
    print( "           and quick to act, this Co-op lacks in Defense but")
    print( "           more than makes up for it in his Power and Spin.")
    #print( " _______________________________________\n")
    input(">")
    
def TSInfo():
    os.system('cls')
    print( " Department: Tech Support\n")
    #print( " _______________________________________\n")
    #print( " Profile")
    #print( " _______________________________________")
    print( " Nickname: The Tank\n")
    print( "     Info: A highly knowledgable Co-op that specializes in " )
    print( "           taking not only a verbal beating but also a ")
    print( "           physical beatdown. This constant berating causes")
    print( "           an increased Defense stat. However, this co-op has")
    print( "           become sheepish and tired, resulting in a low Power.")
   # print( " _______________________________________\n")
    input(">")

#Prints ADTRAN with exlosions
def Aprint():
    print("      |   ___  __________________________  |     ")
    print("   \     /   ||_______  _________________|    /  ")
    print("    *   / /| | / _  // // _  //_ | / __  |  *    ")
    print("   -   / ___ |/ // // // , _//__ |/ / / / *  \   ")
    print("    / /_/  |_/____/ \_/_/|_//_/|_/_/ /_/  |      ")


    
#Spells out PING! in big letters 
def PingPrint():
    delay = .75
    time.sleep(.1)
    
    os.system('cls')  
    print("      ______  __")
    print("     / __  / / /")
    print("    / /_/ / /_/")
    print("   / ____/ __ ")
    print("  /_/     /_/")
    time.sleep(delay)

    os.system('cls')
    print("      ______ _____  __")
    print("     / __  //_  _/ / /")
    print("    / /_/ /  / /  /_/")
    print("   / ____/ _/ /_ __ ")
    print("  /_/     /____//_/")
    time.sleep(delay)
    
    os.system('cls')
    print("      ______ _____  ___   __ __")
    print("     / __  //_  _/ /   | / // /")
    print("    / /_/ /  / /  / /| |/ //_/")
    print("   / ____/ _/ /_ / / |   /__ ")
    print("  /_/     /____//_/  |__//_/")
    time.sleep(delay)
    
    os.system('cls')
    print("      ______ _____  ___   __ ______  __")
    print("     / __  //_  _/ /   | / // ____/ / /")
    print("    / /_/ /  / /  / /| |/ // / ___ /_/")
    print("   / ____/ _/ /_ / / |   // /__/ /__ ")
    print("  /_/     /____//_/  |__//______//_/")
    time.sleep(delay)
    
    os.system('cls')
    print("      ______  _______  __")
    print("     / ____/ / __   / / /")
    print("    / / ___ / /  / / /_/")
    print("   / /__/ // /__/ / __ ")
    print("  /______//______/ /_/")
    time.sleep(delay*2)


# Character class that deffines the players stats
class Character():
    def __init__(self, name, dept, hand, stats):
        self._name = name
        self._dept = dept
        self._hand = hand
        
        self._power = stats[0]
        self._spin = stats[1]
        self._accuracy = stats[2]
        self._defense = stats[3]
        self._term = stats[4]
        self._level = stats[5]
        self._exp = stats[6]

    
    def PowerAdd(self, number):
        self._Power += number
    def SpinAdd(self, number):
        self._spin += number
    def AccuracyAdd(self, number):
        self._accuracy += number
    def DefenseAdd(self, number):
        self._defense += number
    def ExpAdd(self, number):
        self._exp += number
    def TermUp(self):
        self._term +=1
    def LevelUp(self):
        self._level += 1
        

    def getPower(self):
        return self._power
    def getSpin(self):
        return self._spin
    def getAccuracy(self):
        return self._accuracy
    def getDefense(self):
        return self._defense
    def getHand(self):
        return self._hand
    def getTerm(self):
        return self._term
    def getLevel(self):
        return self._level
    def getExp(self):
        return self._exp    
    def getName(self):
        return self._name
    def getDept(self):
        return self._dept
    def getStats(self):
        return [self._power, self._spin, self._accuracy, self._defense, self._term, self._level, self._exp]
    
        
    def ShowStats(self):
        os.system('cls')
        print( "\n ____________________________________")
        print( "")
        print( " Current Stats                       ")
        print( " ____________________________________")
        print("(")
        print( "           Name: ", self._name)
        print( "           Hand: ", self._hand)
        print( "           Term: ", self._term)
        print( "          Level: ", self._level)
        print( "     Department: ", self._dept)
        print()
        print( "          Power: ", self._power)
        print( "           Spin: ", self._spin)
        print( "       Accuracy: ", self._accuracy)
        print( "        Defense: ", self._defense)
        print()
        print( "Work Experience: ", self._exp)
        print( " ____________________________________\n")

        

main()

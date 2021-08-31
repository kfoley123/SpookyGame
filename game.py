gameTitle = "◥(ฅº￦ºฅ)◤        Spooky.Game        ⊂(•̀﹏•́⊂ )∘˚˳°"
def showTitle():
    print("=========================================================")
    print("")
    print(gameTitle)
    print("")
    print("=========================================================")


def formatAnswerString(inputString):
    outputString = inputString.strip()
    return outputString.lower()

def deathScreen(remainingLives):
    print("")
    print(characterName + " has died")
    print("⎧ᴿᴵᴾ⎫◟◟◟◟◟◟◟◟ ❀◟(ó ̯ ò, )")
    print("")
    remainingLives -= 1
    print("remaining lives: "+ str(remainingLives))
    return remainingLives

partyMonk = False

# Game Starts Here
showTitle()

characterName = ""
characterName = input("choose a character name: ")
print("You have chosen the name " + characterName) 
print("")

lives = 5
while(lives > 0):

    playerChoiceOne = input(characterName + " comes to a fork in the road. Choose left or right: ")
    playerChoiceOne = formatAnswerString(playerChoiceOne)
    if(playerChoiceOne == "left"):
        lives = deathScreen(lives)
    elif(playerChoiceOne == "right"):
    
        invalidinput = True
        while(invalidinput):
            playerChoiceTwo = input("You see a chest on the side of the path. Do you open it? ")
            playerChoiceTwo = formatAnswerString(playerChoiceTwo)
            if(playerChoiceTwo == "yes" or playerChoiceTwo == "yeah" or playerChoiceTwo == "y"):
                print("The chest is full of fangs that bite down on your arm, servering it. You bleed to death!")
                lives = deathScreen(lives)
                invalidinput = False
            elif(playerChoiceTwo == "no" or playerChoiceTwo == "nope" or playerChoiceTwo == "n"):
                print(characterName + " noticed that the chest is a mimic and would have eaten you. Great job! You keep walking down the path ")
                invalidinput = True
                while(invalidinput):
                    playerChoiceThree = input("You see an old monk waiting by the side of the road. He asks if he can come with you. Do you accept? Yes or no? ")
                    playerChoiceThree = formatAnswerString(playerChoiceThree)
                    if(playerChoiceThree == "yes" or playerChoiceThree == "yeah" or playerChoiceThree == "y"):
                        print("The monk thanks you for your kindness and follows you down the road")
                        partyMonk = True
                        invalidinput = False
                    elif(playerChoiceThree == "no" or playerChoiceThree == "nope" or playerChoiceThree == "n"):
                        print("The monk warns you that it's dangerous to go alone but you as you continue to walk he is quickly out of sight")
                        invalidinput = False
                    else:
                        print("that is not a vaild option")
                if(partyMonk):
                    playerChoiceFour = input("You come up to a bridge over a great chasm. Becuase its narrow you can only go single file. The monk ushers you ahead of him. Do you go first?")
                    playerChoiceFour = formatAnswerString(playerChoiceFour)
                    if(playerChoiceFour == "yes" or playerChoiceFour == "yeah" or playerChoiceFour == "y"):
                        print("you see an arrow flying towards you and manage to block it with your shield")
                    elif(playerChoiceFour == "no" or playerChoiceFour == "nope" or playerChoiceFour == "n"):
                        print("You see an arrow coming towards the monk and before you can warn him it pierces his chest and he falls off the side of the bridge.")
                        partyMonk = False
                    
                    
                else:
                    print("You come up to a bridge over a great chasm. you cross the bridge")
            else: 
                print("that is not a valid option")



    else: 
        print("that is not a vaild option")

print("GAME OVER")



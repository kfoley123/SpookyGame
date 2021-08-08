gameTitle = "◥(ฅº￦ºฅ)◤        Spooky.Game        ⊂(•̀﹏•́⊂ )∘˚˳°"
print("=========================================================")
print("")
print(gameTitle)
print("")
print("=========================================================")


def formatAnswerString(inputString):
    outputString = inputString.strip()
    return outputString.lower()

partyMonk = False

characterName = ""
characterName = input("choose a character name: ")
print("You have chosen the name " + characterName) 
print("")

lives = 5
while(lives > 0):

    playerChoiceOne = input(characterName + " comes to a fork in the road. Choose left or right: ")
    playerChoiceOne = formatAnswerString(playerChoiceOne)
    if(playerChoiceOne == "left"):
        print("")
        print(characterName + " has died")
        print("⎧ᴿᴵᴾ⎫◟◟◟◟◟◟◟◟ ❀◟(ó ̯ ò, )")
        print("")
        lives -= 1
        print("remaining lives: "+ str(lives))
    elif(playerChoiceOne == "right"):
    
        invalidinput = True
        while(invalidinput):
            playerChoiceTwo = input("You see a chest on the side of the path. Do you open it? ")
            playerChoiceTwo = formatAnswerString(playerChoiceTwo)
            if(playerChoiceTwo == "yes" or playerChoiceTwo == "yeah" or playerChoiceTwo == "y"):
                print("The chest is full of fangs that bite down on your arm, servering it. You bleed to death!")
                print("")
                print(characterName + " has died")
                print("⎧ᴿᴵᴾ⎫◟◟◟◟◟◟◟◟ ❀◟(ó ̯ ò, )")
                print("")
                lives -= 1
                print("remaining lives: "+ str(lives))
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
            else: 
                print("that is not a valid option")



    else: 
        print("that is not a vaild option")

print("GAME OVER")



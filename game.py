gameTitle = "◥(ฅº￦ºฅ)◤        Spooky.Game        ⊂(•̀﹏•́⊂ )∘˚˳°"
print("=========================================================")
print("")
print(gameTitle)
print("")
print("=========================================================")

characterName = ""
characterName = input("choose a character name: ")
print("You have chosen the name " + characterName) 

lives = 5
while(lives > 0):

    playerChoiceOne = input(characterName + " comes to a fork in the road. Choose left or right: ")
    if(playerChoiceOne.lower() == "left"):
        print("")
        print(characterName + " has died")
        print("⎧ᴿᴵᴾ⎫◟◟◟◟◟◟◟◟ ❀◟(ó ̯ ò, )")
        print("")
        lives -= 1
        print("remaining lives: "+ str(lives))
    elif(playerChoiceOne.lower() == "right"):
    
        invalidinput = True
        while(invalidinput):
            playerChoiceTwo = input("You see a chest on the side of the path. Do you open it? ")
            if(playerChoiceTwo.lower() == "yes" or playerChoiceTwo.lower() == "yeah" or playerChoiceTwo.lower() == "y"):
                print("The chest is full of fangs that bite down on your arm, servering it. You bleed to death!")
                print("")
                print(characterName + " has died")
                print("⎧ᴿᴵᴾ⎫◟◟◟◟◟◟◟◟ ❀◟(ó ̯ ò, )")
                print("")
                lives -= 1
                print("remaining lives: "+ str(lives))
                invalidinput = False
            elif(playerChoiceTwo.lower() == "no" or playerChoiceTwo.lower() == "nope" or playerChoiceTwo.lower() == "n"):
                print(characterName + " noticed that the chest is a mimic and would have eaten you. Great job! You keep walking down the path ")
                invalidinput = False
            else: 
                print("that is not a valid option")


    else: 
        print("that is not a vaild option")

print("GAME OVER")

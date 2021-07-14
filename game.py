
gameTitle = "◥(ฅº￦ºฅ)◤        Spooky.Game        ⊂(•̀﹏•́⊂ )∘˚˳°"
print("=========================================================")
print("")
print(gameTitle)
print("")
print("=========================================================")

characterName = ""
characterName = input("choose a character name: ")
print("You have chosen the name " + characterName) 

playerChoiceOne = input(characterName + " comes to a fork in the road. Choose left or right: ")
if(playerChoiceOne.lower() == "left"):
    print("")
    print(characterName + " has died")
    print("⎧ᴿᴵᴾ⎫◟◟◟◟◟◟◟◟ ❀◟(ó ̯ ò, )")
    print("")
elif(playerChoiceOne.lower() == "right"):
    print(characterName + " has won")
else: 
    print("that is not a vaild option")

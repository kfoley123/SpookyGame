
gameTitle = "◥(ฅº￦ºฅ)◤        Spooky.Game        ⊂(•̀﹏•́⊂ )∘˚˳°"
print("=========================================================")
print("")
print(gameTitle)
print("")
print("=========================================================")

characterName = ""
characterName = input("choose a character name: ")
print("You have chosen the name " + characterName) 

playerChoiceOne = input("You come to a fork in the road. Choose left or right: ")
if(playerChoiceOne.lower() == "left"):
    print("You have died")
elif(playerChoiceOne.lower() == "right"):
    print("you have won")
else: 
    print("that is not a vaild option")

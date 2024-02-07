import random 
options=["Rock","Paper","Scissor"]
player=None
computer=random.choice(options)
while player not in options:
    player=input("Enter your Choice(Rock,Paper,Scissor):")
print("PLAYER:",player)   
print("COMPUTER:",computer)
if(player==computer):
    print("IT'S A TIE GAME!!")
elif(player=="Rock" and computer=="Paper"):
    print("YOU LOSE,BAD LUCK!!!")
elif(player=="Rock" and computer=="Scissor"):
    print("Congratulations, YOU WIN!!!")
elif(player=="Paper" and computer=="Rock"):
    print("Congratulations, YOU WIN!!!")
elif(player=="Paper" and computer=="Scissor"):
    print("YOU LOSE,BAD LUCK!!!")
elif(player=="Scissor" and computer=="Rock"):
    print("YOU LOSE,BAD LUCK!!!")  
else:
    print("Congratulations, YOU WIN!!!")

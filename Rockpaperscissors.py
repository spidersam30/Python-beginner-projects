from random import randint

r = ["Rock","Paper","Scissors"]

Computer = r[randint(0,2)]

player = False

while player == False:

   player = input("Rock,Paper,Scissors?")
   if player == Computer:
       print("tie")
   elif player == "Rock":
        if Computer == "Paper":
            print(Computer, "covers", player)
        else:
            print(player, "Smashes", Computer)

   elif player == "Paper":
        if Computer == "Scissors":
            print(Computer, "cuts", player)
        else:
            print(player, "covers", Computer)

   elif player == "Scissors":
        if Computer == "Rock":
           print(Computer, "breaks", player)
        else:
           print(player, "cuts", Computer)

   else:
    print("this is not a valid play")
 player = False
Computer = r[randint(0,2)]

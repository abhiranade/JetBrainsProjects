import random

# read from the ratings.txt file and store name and scores in a dictonary
file = open("ratings.txt")
i = file.readlines()
player_details = {}
j = 0
while j<len(i):
    name,score = i[j].split()
    player_details.update({name:score})
    j+=1
file.close()

print("Welcome to the rock, paper and scissors extended edition game !!")
print("In this extended edition you can work with 12 more game objects apart from rock, paper and scissors")
print("Here is the full list of game objects available for the game : ")
print("rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire")
print("You can choose all or a subset of objects to play the game !")
print("For every win you get 100 points, for every draw you get 50 points and for a loss you dont get any points.")
print("------------------------------------------------------------------------------------")
pname = input("To play the game please enter your name: ")
print(f"Hello, {pname}")

#Check if the enter name is present in dictonary; if yes then get the score from dictonary or else set score to zero
if pname in player_details.keys():
    pscore = player_details.get(pname)
    pscore = int(pscore)
else:
    pscore = 0

# these lists represent what each of the game objects beats other game objects
rock_beats = ['sponge','wolf','tree','human','snake','scissors','fire']
gun_beats = ['wolf','tree','human','snake','scissors','fire','rock']
lightning_beats = ['tree','human','snake','scissors','fire','rock','gun']
devil_beats = ['human','snake','scissors','fire','rock','gun','lightning']
dragon_beats = ['snake','scissors','fire','rock','gun','lightning','devil']
water_beats = ['scissors','fire','rock','gun','lightning','devil','dragon']
air_beats = ['fire','rock','gun','lightning','devil','dragon','water']
paper_beats = ['rock','gun','lightning','devil','dragon','water','air']
sponge_beats = ['gun','lightning','devil','dragon','water','air','paper']
wolf_beats = ['lightning','devil','dragon','water','air','paper','sponge']
tree_beats = ['devil','dragon','water','air','paper','sponge','wolf']
human_beats = ['dragon','water','air','paper','sponge','wolf','tree']
snake_beats = ['water','air','paper','sponge','wolf','tree','human']
scissors_beats = ['air','paper','sponge','wolf','tree','human','snake']
fire_beats = ['paper','sponge','wolf','tree','human','snake','scissors']

# logic to decide what are the playing objects , if user gives the input in the form of comma seperated objects then split and
# create a list of playing objects , if player doesnot give any input then the default game objects are rock, paper and scissors

rps = []
print("Please enter the game objects you want to play with seperated by comma.for ex. rock,devil,wolf,scissors (without spaces)")
print("If you dont enter anything then game will be played with default 3 objects : rock, paper, scissors")
game_obj = input("Your game objects : ")
if game_obj == "":
    print("Since you didnot choose any objects, game will be played by using rock,paper and scissors.")
    rps = ['rock','paper','scissors']
else:
    game_objects = game_obj.split(",")
    for obj in game_objects:
        rps.append(obj)
    
#Start playing the game
print("Okay, let's start")
print("Enter your choice : ")
print("game object name OR '!exit' (for exiting the game) or '!score' (for getting your score)")
player_choice = input()
while player_choice != "!exit":
    computer_choice = random.choice(rps)
    if player_choice == computer_choice:
        pscore += 50
        print(f"There is a draw ({computer_choice})")
    elif player_choice == "rock":
        if computer_choice in rock_beats:
            pscore += 100
            print(f"Well done. Computer chose {computer_choice} and failed")
        else:
            print(f"Sorry, but computer chose {computer_choice}")
    elif player_choice == "gun":
        if computer_choice in gun_beats:
            pscore += 100
            print(f"Well done. Computer chose {computer_choice} and failed")
        else:
            print(f"Sorry, but computer chose {computer_choice}")
    elif player_choice == "lightning":
        if computer_choice in lightning_beats:
            pscore += 100
            print(f"Well done. Computer chose {computer_choice} and failed")
        else:
            print(f"Sorry, but computer chose {computer_choice}")
    elif player_choice == "devil":
        if computer_choice in devil_beats:
            pscore += 100
            print(f"Well done. Computer chose {computer_choice} and failed")
        else:
            print(f"Sorry, but computer chose {computer_choice}")
    elif player_choice == "dragon":
        if computer_choice in dragon_beats:
            pscore += 100
            print(f"Well done. Computer chose {computer_choice} and failed")
        else:
            print(f"Sorry, but computer chose {computer_choice}")
    elif player_choice == "water":
        if computer_choice in water_beats:
            pscore += 100
            print(f"Well done. Computer chose {computer_choice} and failed")
        else:
            print(f"Sorry, but computer chose {computer_choice}")
    elif player_choice == "air":
        if computer_choice in air_beats:
            pscore += 100
            print(f"Well done. Computer chose {computer_choice} and failed")
        else:
            print(f"Sorry, but computer chose {computer_choice}")
    elif player_choice == "paper":
        if computer_choice in paper_beats:
            pscore += 100
            print(f"Well done. Computer chose {computer_choice} and failed")
        else:
            print(f"Sorry, but computer chose {computer_choice}")
    elif player_choice == "sponge":
        if computer_choice in sponge_beats:
            pscore += 100
            print(f"Well done. Computer chose {computer_choice} and failed")
        else:
            print(f"Sorry, but computer chose {computer_choice}")
    elif player_choice == "wolf":
        if computer_choice in wolf_beats:
            pscore += 100
            print(f"Well done. Computer chose {computer_choice} and failed")
        else:
            print(f"Sorry, but computer chose {computer_choice}")
    elif player_choice == "tree":
        if computer_choice in tree_beats:
            pscore += 100
            print(f"Well done. Computer chose {computer_choice} and failed")
        else:
            print(f"Sorry, but computer chose {computer_choice}")
    elif player_choice == "human":
        if computer_choice in human_beats:
            pscore += 100
            print(f"Well done. Computer chose {computer_choice} and failed")
        else:
            print(f"Sorry, but computer chose {computer_choice}")
    elif player_choice == "snake":
        if computer_choice in snake_beats:
            pscore += 100
            print(f"Well done. Computer chose {computer_choice} and failed")
        else:
            print(f"Sorry, but computer chose {computer_choice}")
    elif player_choice == "scissors":
        if computer_choice in scissors_beats:
            pscore += 100
            print(f"Well done. Computer chose {computer_choice} and failed")
        else:
            print(f"Sorry, but computer chose {computer_choice}")
    elif player_choice == "fire":
        if computer_choice in fire_beats:
            pscore += 100
            print(f"Well done. Computer chose {computer_choice} and failed")
        else:
            print(f"Sorry, but computer chose {computer_choice}")
    elif player_choice == "!score":
        print(f"Your score: {pscore}")
    else:
        print("Invalid input")
    player_choice = input("Please enter your choice : ")

# Code to write new scores into the ratings file
d1 = {}
pscore = str(pscore)
# if player name already exists in the file then update the score in player disctonary or else create a new row in the dictonary
if pname in player_details.keys():
    d1.update({pname:pscore})
    player_details.update(d1)
else:
    player_details.update({pname:pscore})

# create lists of all keys and values and write them in the file
p = list(player_details.keys())
s = list(player_details.values())
i = 0
lines = []
while i < len(p):
    line = p[i] + " " + s[i] + "\n"
    lines.append(line)
    i+=1

file = open("ratings.txt","w")
file.writelines(lines)
file.close()

print("Thank You !! BBye !!")

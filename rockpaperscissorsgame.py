from tkinter import*
import random

root = Tk()
root.title("Rock Paper Scissors Game")
root.config(background="black")
player_score = 0
computer_score = 0
options = [('rock',0),('paper',1),('scissors',2)]
def computer_win():
    global player_score, computer_score
    computer_score +=1
    cs_label.config(text="Computer Score"+str(computer_score))
    ps_label.config(text="Player Score"+str(player_score))
    winner_label.config(text="Computer Won")
    
def player_win():
    global player_score, computer_score
    player_score +=1
    cs_label.config(text="Computer Score"+ str(computer_score))
    ps_label.config(text="Player Score"+str(player_score))
    winner_label.config(text="Player Won")
    
def draw():
    global player_score, computer_score
    cs_label.config(text="Computer Score"+ str(computer_score))
    ps_label.config(text="Player Score"+str(player_score))
    winner_label.config(text="Its A Draw")
# Parameter is a simple value that can change.A value holder. def greet(name): 'name' is a parameter (empty box) print("Hello", name)

def computer_choice():# In the random module, we have a choice value which helps us to pick a random value from a list
    return random.choice(options)


def player_choice(player_input):
    global player_score, computer_score
    print(player_input)
    computer_input = computer_choice()
    print(computer_input)
    player_choice_label.config(text="Player has selected"+ player_input[0])
    computer_choice_label.config(text="Computer has selected"+ computer_input[0])
    if player_input == computer_input():
        draw()
    if player_input[1] == 0: # Player selected rock
        if computer_input[1]  == 1: # Computer selected paper
            computer_win()
        elif computer_input[1] == 2:
            player_win()
    if player_input[1] == 1:
        if computer_input[1] == 0:
            player_win()
        elif computer_input[1] == 2:
            computer_win()
    if player_input[1] == 2:
        if computer_input[1] == 0:
            computer_win()
        elif computer_input[1] == 1:
            player_win()
tl = Label(root, text="Rock Paper Scissors Game")
tl.place(x=100,y=10)
t2 = Label(root, text="Lets start the game")
t2.place(x=100,y=30)
t3 = Label(root,text="Options")
t3.place(x=300,y=70)
r = Button(root,command=lambda:player_choice(options[0]),text="rock")
r.place(x=375,y=110)
p = Button(root,command=lambda:player_choice(options[1]),text="paper")
p.place(x=425,y=110)
s = Button(root,command=lambda:player_choice(options[2]),text="scissors")
s.place(x=475,y=110)
player_choice_label = Label(root, width=20)
player_choice_label.place(x=375,y=200)
computer_choice_label = Label(root, width=20)
computer_choice_label.place(x=425, y=230)
cs_label = Label(root, width=20)
cs_label.place(x=400,y=275)
ps_label = Label(root, width=20)
ps_label.place(x=450,y=300)
winner_label = Label(root, width=20)
winner_label.place(x=500,y=230)

root.mainloop()
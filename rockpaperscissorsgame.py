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

def choice():
    player

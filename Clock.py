from tkinter import*
from tkinter.ttk import*
from time import strftime # string format time
import random


root=Tk()
root.title("Clock")
root.geometry("400x400")

def random_colour():

    color_list = [
        "red", "green", "blue", "pink", "cyan", "yellow", "orange", 
        "purple", "brown", "magenta"]
    
    color = random.choice(color_list)  # Pick a random color from the list
    Label_time.color = color
    
def time_now():

    t = strftime('%H:%M:%S %p')
    Label_time.config(text=t)
    random_colour()
    Label_time.config(background=Label_time.color)
    random_colour()
    Label_time.config(foreground=Label_time.color)
    Label_time.after(1000,time_now) # after function tells the program to wait for 1000 miliseconds to checck the time and change it


Label_time = Label(root, font=("calibri", 40, "bold"),foreground="blue",background="black")
Label_time.pack(anchor="center")
time_now()


root.mainloop()


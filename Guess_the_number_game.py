from tkinter import*
from random import randint

root = Tk()
root.title("Guess the number game")
root.geometry("400x400")

la_title = Label(root,text="Guess the number")
la_title.grid(row=5,column=0)
la_name = Label(root,text="What is your name")
la_name.grid(row=1,column=5)
en_name = Entry(root,width=30)
en_name.grid(row=2,column=5)
la_guess = Label(root,text=("Guess the number"))
la_guess.grid(row=5,column=10)
en_guess = Entry(root,width=20)
en_guess.grid(row=6,column=10)



root.mainloop()
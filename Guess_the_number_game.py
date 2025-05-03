from tkinter import*
from random import randint
from tkinter import messagebox

root = Tk()
root.title("Guess the number game")
root.geometry("400x400")
root.config(background="light blue")

Numb = randint(1,20)

def hello_message():
    print("Hello people" )
def button_pressed():
    person_name = en_name.get()
    messagebox.showinfo("name", "Hello "+ person_name + "I am thinking of a number between 1-20, can you guess it?")
def check_number():
    guess = en_guess.get()
    guess = int(guess)
    if guess > Numb:
        messagebox.showinfo("high","Your guess is too high")
    if guess < Numb:
        messagebox.showinfo("low","Your guess is too low")
    if guess == Numb:
        messagebox.showinfo("Good","You guessed correctly, good job!")

la_title = Label(root,text="Guess the number",bg="blue")
la_title.grid(row=0,column=20)
la_name = Label(root,text="What is your name")
la_name.grid(row=1,column=5)

en_name = Entry(root,width=30)
en_name.grid(row=1,column=7)
la_guess = Label(root,text=("Guess the number"))
la_guess.grid(row=2,column=5)

en_guess = Entry(root,width=30)
en_guess.grid(row=2,column=7)
bu_name = Button(root,text = "Enter",command=button_pressed)
bu_name.grid(row=1,column=10)

bu_guess = Button(root,text = "Enter",command=check_number)
bu_guess.grid(row=2,column=10)

root.mainloop()
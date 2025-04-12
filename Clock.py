from tkinter import*
from tkinter.ttk import*
from time import strftime # string format time

root=Tk()
root.title("Clock")
root.geometry("400x400")

def time_now():
    t = strftime('%H:%M:%S %p')
    Label_time.config(text=t)
    Label_time.after(1000,t) # after function tells the program to wait for 1000 miliseconds to checck the time and change it

Label_time = Label(root, font=("calibri", 40, "bold"),foreground="blue",background="black")
Label_time.pack(anchor="center")
time_now()

root.mainloop()


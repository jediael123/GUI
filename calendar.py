from tkinter import*

root = Tk()
root.geometry("400x400") # type: ignore
root.config(background="lightblue")
root.title("Calendar")
u=Label(root, text="Type in any year")
u.place(x=50,y=50)











root.mainloop()
from tkinter import*

root = Tk()
root.title("Distance Calculator")
root.config(background="light blue")

Etc = Label(root,text="Enter time:")
Etc.grid(row=5,column=5)
Et = Entry(root, width=30,fg="blue",bg="turquoise")
Eto = Label(root,text="Enter speed:")
Eto.grid(row=9,column=5)
Etv = Entry(root, width=30,fg="blue",bg="turquoise")
Etv.grid(row=10,column=5)
def convert():
    time= int(Etv.get())
    speed = int(Et.get())
    distance = speed*time
    l1.config(text=distance)
Et.grid(row=6,column=5)

Ph = Button(root, text="Convert", command=convert)
Ph.grid(row=7,column=5)

l1 = Label(root, text="distance?", width=15)
l1.grid(row=8, column=5)
root.mainloop()
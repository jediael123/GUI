from tkinter import*

root = Tk()
root.geometry('400x400')

root.config(background="light blue")
root.title("Pick templates")

u= Label(root, text="Pick templates")
u.place(x=40,y=60)
uq=Entry(root,width=30)
uq.place(x=120,y=60)

u= Label(root, text="Name your project")
u.place(x=40,y=90)
ue = Entry(root,width= 30)
ue.place(x=140,y=90)



root.mainloop()

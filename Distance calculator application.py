from tkinter import*

root = Tk()
root.title("Distance Calculator")
root.config(background="light blue")

time_label = Label(root,text="Enter time(hours):")
time_label.grid(row=5,column=5)
time_entry = Entry(root, width=30,fg="blue",bg="turquoise")
speed_label= Label(root,text="Enter speed(km):")
speed_label.grid(row=7,column=5)
speed_entry = Entry(root, width=30,fg="blue",bg="turquoise")
speed_entry.grid(row=7,column=6)
def convert():
    time= int(time_entry.get())
    speed = int(speed_entry.get())
    distance = speed*time
    l1.config(text=distance)
time_entry.grid(row=5,column=6)

con = Button(root, text="Convert", command=convert)
con.grid(row=9,column=5)

l1 = Label(root, text="distance?", width=15)
l1.grid(row=8, column=5)
root.mainloop()
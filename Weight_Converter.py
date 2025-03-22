from tkinter import*

root = Tk()

def convert():
    Kg = Et.get()
    if Kg.replace('.','',1).isdigit():#Checks if it is a valid number and so it can remove the first accurance of decimal and check if the rest of the numbers are decimal or not
        error_msg.grid_forget()#Hides any previous error message -- Hides the label widget
        GG=(float(Kg)*1000)
        PP=(float(Kg)*35.274)
        OO=(float(Kg)*2.20462)
        Gv.config(text=GG) 
        Pv.config(text=PP) 
        Ov.config(text=OO) 
    else:
        error_msg.grid(row=1,column=1)
error_msg = Label(root, text="Invalid Input")


root.title("Weight Converter")
root.config(background="light blue")
Etc = Label(root,text="Enter weight in Kg:")
Etc.grid(row=2,column=2)
Et = Entry(root, width=30,fg="blue",bg="turquoise")
Et.grid(row=2,column=4)
Ph = Button(root, text="Convert", command=convert)
Ph.grid(row=2,column=6)
Gv = Label(root)
Gv.grid(row=4,column=7)
G = Label(root,text="Grams")
G.grid(row=3,column=7)
Pv = Label(root)
Pv.grid(row=4,column=5)
P = Label(root,text="Pounds")
P.grid(row=3,column=5)
Ov = Label(root)
Ov.grid(row=4,column = 3)
O = Label(root,text="Ounces")
O.grid(row=3,column = 3)



root.mainloop()
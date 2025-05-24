from tkinter import*
from tkinter.ttk import*
root = Tk()
root.title("Table Generator")
root.geometry("400x400")
root.config(bg="blue")

main_label = Label(root,text="Table Generator")
main_label.grid(row=0,column=0,columnspan=3,pady=25)

Generate = Button(root,width=10,text="Generate")
Generate.grid(row=10,column=3)

table = Label(root)
table.grid(row=11,column=3)

num_and_range = Label(root,text="Number and range")
num_and_range.grid(row=5,column=1)
num = IntVar()#A variable used to store int values
combobox1 = Combobox(root,textvariable=num,width=5)#entering a value or selecting one from a list
combobox1['values'] = tuple(range(101))#creates the values for the combobox
#radio button-selects only one of the multiiple options
combobox1.grid(row=5,column=4)

val = IntVar()
radio10 = Radiobutton(root,variable=val,text="10", value=10)
radio20 = Radiobutton(root,variable=val,text="20",value=20)
radio30 = Radiobutton(root,variable=val,text="30",value=30)
val.set(10)#selects radiobutton 10 by default but can be changed
radio10.grid(row=5,column=10)
radio20.grid(row=7,column=10)
radio30.grid(row=11,column=10)








root.mainloop()
from tkinter import*

root = Tk()
root.title("Table Generator")
root.geometry("400x400")
root.config(bg="blue")

main_label = Label(root,text="Table Generator",bg="black",fg="white")
main_label.grid(row=0,column=0,columnspan=3,pady=25)

gen_label = Label(root,text="table",bg="black",fg="white")
gen_label.grid(row=3,column=0)

Generate = Button(root,bg="black",fg="white",width=10)
Generate.grid(row=10,column=3)









root.mainloop()
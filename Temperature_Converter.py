from tkinter import*

root = Tk()
root.title("Celsius to Fahrenheit Converter")
root.config(background="light blue")
Cf = Label(root, text="Celsius->Fahrenheit")
Cf.grid(row=2,column=5)
Etc = Label(root,text="Enter temperature in celcius:")
Etc.grid(row=5,column=0)




root.mainloop()
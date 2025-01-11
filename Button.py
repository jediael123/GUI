# Python tkinter is a standard GUI library for python which provides a fast and easy way to create desktop applications, it provides a variety of widgets like buttons, labels and more to create interactive user interfaces
from tkinter import*
root = Tk()
root.geometry('100x100')
b = Button(root, text = 'click me', background = 'blue')
b.pack(side = 'top')
root.mainloop()


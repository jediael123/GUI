from tkinter import*
import calendar

def showcal():
    new_root = Tk()
    new_root.title("Calendar")
    new_root.config(background= "lightgreen")
    new_root.geometry("700x700")
    fetch_year = int(year_field.get())
    content = calendar.calendar(fetch_year)#We are storing the calendar in the content variable using the charactor function in the calendar library
    cal = Label(new_root, text=content, font= "Consolas 12 bold")
    cal.grid(row=5, column=1, padx=20)
    new_root.mainloop()
if __name__ == "__main__":
    root = Tk()
    root.geometry("400x400") # type: ignore
    root.config(background="lightblue")
    root.title("Calendar")
    ua = Label(root, text="Calendar")
    u=Label(root, text="Type in any year")
    year_field = Entry(root)
    uo=Button(root, text="Show Calendar",command=showcal)
    ub=Button(root,text="Exit",command=exit)
    u.grid(row=2,column=1)
    ua.grid(row=1,column=1)
    year_field.grid(row=3,column=1)
    uo.grid(row=4,column=1)
    ub.grid(row=5,column=1)










    root.mainloop()
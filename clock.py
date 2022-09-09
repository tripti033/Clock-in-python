from tkinter import *
import time


root = Tk()
root.geometry("600x200")

def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%A")
    am_or_pm = time.strftime("%p")

    labell.config(text=hour + ":" + minute + ":" + second + " " + am_or_pm)
    labell.after(1000, clock)

    labell2.config(text = day)

def update():
    labell.config(text="New Text")

labell = Label(root, text="", font=("Helvetica", 48), fg="red", bg="black")
labell.pack(pady=20)

labell2 = Label(root, text="", font=("Helvetica", 14))
labell2.pack(pady=10)

clock()

root.mainloop()
from tkinter import *
import webbrowser
def clicked():
    webbrowser.open_new("https://www.youtube.com/channel/UCsn-etSqQyV-_1CzD-BfFvA")
win1 = Tk()
Fe = Frame(win1)
Fe.pack()
FeB = Frame(win1)
FeB.pack(side=TOP)
theLabel = Label(Fe, text="Click the button bellow for more dummy scripts!")
theLabel.pack()
B1 = Button(FeB, text="Click me!", fg="blue", command=clicked)
B1.pack(side=TOP)
win1.mainloop()
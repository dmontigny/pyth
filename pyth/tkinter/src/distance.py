from tkinter import *

window = Tk()

def convert():
    t1.insert(END, str(float(e1_value.get()) / .001) + " gm")
    t2.insert(END, str(float(e1_value.get()) * 2.20462) + " lb")
    t3.insert(END, str(float(e1_value.get()) * 35.274) + " oz")

b1 = Button(window, text = "Execute", command=convert)
b1.grid(row=0, column=3)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=0)

t1 = Text(window, height=1, width=20)
t2 = Text(window, height=1, width=20)
t3 = Text(window, height=1, width=20)
t1.grid(row=1, column=1)
t2.grid(row=1, column=2)
t3.grid(row=1, column=3)
window.mainloop()


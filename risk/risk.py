from tkinter import *
from math import *
main = Tk()
main.title('Risk Calculator')

#Full Screen
class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

def add():
    blank.delete(0, END)
    Ans = int(num1.get()) + int(num2.get())
    blank.insert(0, Ans)
def sub():
    blank.delete(0, END)
    Ans = int(num1.get()) - int(num2.get())
    blank.insert(0, Ans)
def mult():
    blank.delete(0, END)
    Ans = int(num1.get()) * int(num2.get())
    blank.insert(0, Ans)
def div():
    blank.delete(0, END)
    Ans = int(num1.get()) / int(num2.get())
    blank.insert(0, Ans)
def clear():
    blank.delete(0, END)
    num2.delete(0, END)
    num1.delete(0, END)
def sq():
    blank.delete(0, END)
    Ans = int(num1.get()) * int(num1.get())
    blank.insert(0, Ans)

def sqrtt():
    blank.delete(0, END)
    h = int(num1.get())
    a = sqrt(h)
    Ans = (int(a))
    blank.insert(0, Ans)


Label(main, text = "Enter Num 1:").grid(row=0)
Label(main, text = "Enter Num 2:").grid(row=1)
Label(main, text = "Your risk is:").grid(row=2)


num1 = Entry(main)
num2 = Entry(main)
blank = Entry(main)


num1.grid(row=0, column=1)
num2.grid(row=1, column=1)
blank.grid(row=2, column=1)


Button(main, text='Quit', command=main.destroy).grid(row=4, column=0, sticky=W)
Button(main, text='Add', command=add).grid(row=0, column=3, sticky=W,)
Button(main, text='Subtract', command=sub).grid(row=0, column=4, sticky=W)
Button(main, text='Multiply', command=mult).grid(row=0, column=5, sticky=W)
Button(main, text='Divide', command=div).grid(row=0, column=6, sticky=W)
Button(main, text='^2', command=sq).grid(row=0, column=7, sticky=W)
Button(main, text='Sqrt', command=sqrtt).grid(row=0, column=8, sticky=W)
Button(main, text='Clear', command=clear).grid(row=0, column=9, sticky=W)

Label(main, text = "To shrink the window, press esc.").grid(row=5)

app=FullScreenApp(main)
mainloop()
from tkinter import *
from math import *
main = Tk()
main.title('Risk Calculator')
#favicon
main.call('wm', 'iconphoto', main._w, PhotoImage(file='images/tdiFavicon.png'))

#variables
is_male = IntVar()
is_smoker = IntVar()
has_history = IntVar()
has_t2d = IntVar()

def calculate():
    blank.delete(0, END)
    
    calculated_risk = 1

    #get variables
    age_get = int(age.get())
    is_male_get = int(is_male.get())
    is_smoker_get = int(is_smoker.get())
    has_history_get = int(has_history.get())
    has_t2d_get = int(has_t2d.get())

    if age_get <= 45:
        calculated_risk = calculated_risk
    elif age_get > 45 and age_get <= 55:
        calculated_risk += 1
    elif age_get > 55 and age_get <= 65:
        calculated_risk += 2
    else:
        calculated_risk += 3

    if is_male_get == 1:
        calculated_risk += 1

    if is_smoker_get == 1:
        calculated_risk += 1

    if has_history_get == 1:
        calculated_risk += 1

    if has_t2d_get == 1:
        calculated_risk += 1

    blank.insert(0, calculated_risk)


Label(main, text = "Enter your age:").grid(row=0)
Label(main, text = "Your gender:").grid(row=1)
Label(main, text = "Are you a smoker?").grid(row=2)
Label(main, text = "Do you have a family history of pancreatic cancer?").grid(row=3)
Label(main, text = "Do you have Type 2 Diabetes?").grid(row=4)
Label(main, text = "Your risk is:").grid(row=5)


age = Entry(main)
male = Checkbutton(main, text="Male", variable=is_male)
female = Checkbutton(main, text="Female")
smoker_yes = Checkbutton(main, text="Yes", variable=is_smoker)
smoker_no = Checkbutton(main, text="No")
history_yes = Checkbutton(main, text="Yes", variable=has_history)
history_no = Checkbutton(main, text="No")
t2d_yes = Checkbutton(main, text="Yes", variable=has_t2d)
t2d_no = Checkbutton(main, text="No")
blank = Entry(main)


age.grid(row=0, column=1)
male.grid(row=1, column=1, sticky=W)
female.grid(row=1, column=2, sticky=W)
smoker_yes.grid(row=2, column=1)
smoker_no.grid(row=2, column=2)
history_yes.grid(row=3, column=1)
history_no.grid(row=3, column=2)
t2d_yes.grid(row=4, column=1)
t2d_no.grid(row=4, column=2)
blank.grid(row=5, column=1)


Button(main, text='Calculate Risk', command=calculate).grid(row=6, column=0, sticky=W)
Button(main, text='Quit', command=main.destroy).grid(row=6, column=1, sticky=W)


mainloop()
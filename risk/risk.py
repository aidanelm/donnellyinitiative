from tkinter import *
from math import *
main = Tk()
main.title('Risk Calculator')

def calculate():
    blank.delete(0, END)
    calculated_risk = 1

    age_get = int(age.get())
    gender_get = str(gender.get())

    if age_get <= 45:
        calculated_risk = calculated_risk
    elif age_get > 45 and age_get <= 55:
        calculated_risk += 1
    elif age_get > 55 and age_get <= 65:
        calculated_risk += 2
    else:
        calculated_risk += 3


    if gender_get == "M" or gender_get == "m" or gender_get == "Male" or gender_get == "male":
        calculated_risk += 1

    blank.insert(0, calculated_risk)


Label(main, text = "Enter your age:").grid(row=0)
Label(main, text = "Enter your gender (M/F):").grid(row=1)
Label(main, text = "Your risk is:").grid(row=2)


age = Entry(main)
gender = Entry(main)
blank = Entry(main)


age.grid(row=0, column=1)
gender.grid(row=1, column=1)
blank.grid(row=2, column=1)

Button(main, text='Calculate Risk', command=calculate).grid(row=4, column=0, sticky=W,)
Button(main, text='Quit', command=main.destroy).grid(row=5, column=0, sticky=W)

mainloop()
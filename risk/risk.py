from tkinter import *

#window
main = Tk()
main.title('Risk Calculator')
#favicon
main.call('wm', 'iconphoto', main._w, PhotoImage(file='images/tdiFavicon.png'))

#variables
is_male = IntVar()
is_smoker = IntVar()
has_history = IntVar()
has_t2d = IntVar()
is_overweight = IntVar()
is_obese = IntVar()
has_pancreatitis = IntVar()
has_peutz_jeghers = IntVar()
has_cirrhosis = IntVar()
is_ashkenazi = IntVar()
diet_healthiness = IntVar()
has_FMM_history = IntVar()
has_HBOC_history = IntVar()
has_FAP = IntVar()
has_LFS = IntVar()
has_Lynch = IntVar()
has_H_pylori = IntVar()
has_VHL = IntVar()
has_MEN1 = IntVar()

#calculation
def calculate():
    blank.delete(0, END)
    
    calculated_risk = 1

    #get variables
    age_get = int(age.get())
    is_male_get = int(is_male.get())
    is_smoker_get = int(is_smoker.get())
    has_history_get = int(has_history.get())
    has_t2d_get = int(has_t2d.get())
    is_overweight_get = int(is_overweight.get())
    is_obese_get = int(is_obese.get())
    has_pancreatitis_get = int(has_pancreatitis.get())
    has_peutz_jeghers_get = int(has_peutz_jeghers.get())
    has_cirrhosis_get = int(has_cirrhosis.get())
    is_ashkenazi_get = int(is_ashkenazi.get())
    diet_healthiness_get = int(diet_healthiness.get())
    has_FMM_history_get = int(has_FMM_history.get())
    has_HBOC_history_get = int(has_HBOC_history.get())
    has_FAP_get = int(has_FAP.get())
    has_LFS_get = int(has_LFS.get())
    has_Lynch_get = int(has_Lynch.get())
    has_H_pylori_get = int(has_H_pylori.get())
    has_VHL_get = int(has_VHL.get())
    has_MEN1_get = int(has_MEN1.get())

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

    if is_overweight_get == 1:
        calculated_risk += 1
    
    if is_obese_get == 1:
        calculated_risk += 1

    if has_pancreatitis_get == 1:
        calculated_risk += 1

    if has_peutz_jeghers_get == 1:
        calculated_risk += 1

    if has_cirrhosis_get == 1:
        calculated_risk += 1

    if is_ashkenazi_get == 1:
        calculated_risk += 1

    if diet_healthiness_get == 1:
        calculated_risk += 1

    if has_FMM_history_get == 1:
        calculated_risk += 1

    if has_HBOC_history_get == 1:
        calculated_risk += 1

    if has_FAP_get == 1:
        calculated_risk += 1

    if has_LFS_get == 1:
        calculated_risk += 1

    if has_Lynch_get == 1:
        calculated_risk += 1

    if has_H_pylori_get == 1:
        calculated_risk += 1

    if has_VHL_get == 1:
        calculated_risk += 1

    if has_MEN1_get == 1:
        calculated_risk += 1

    blank.insert(0, calculated_risk)

#description of data input
Label(main, text = "Enter your age:").grid(row=0)
Label(main, text = "Select your gender:").grid(row=1)
Label(main, text = "Are you a smoker?").grid(row=2)
Label(main, text = "Do you have a family history of pancreatic cancer?").grid(row=3)
Label(main, text = "Do you have Type 2 Diabetes?").grid(row=4)
Label(main, text = "Are you overweight or obese?").grid(row=5)
Label(main, text = "Do you have any form of pancreatitis?").grid(row=6)
Label(main, text = "Do you have Peutz-Jeghers syndrome?").grid(row=7)
Label(main, text = "Do you have hepatic cirrhosis?").grid(row=8)
Label(main, text = "Are you of Ashkenazi Jewish ancestry?").grid(row=9)
Label(main, text = "Is your diet high in meats and cholesterol?").grid(row=10)
Label(main, text = "Does your family have familial malignant melanoma?").grid(row=11)
Label(main, text = "Do you have HBOC syndrome?").grid(row=12)
Label(main, text = "Do you have familial adenomatous polyposis?").grid(row=13)
Label(main, text = "Do you have Li-Fraumeni syndrome?").grid(row=14)
Label(main, text = "Do you have Lynch syndrome?").grid(row=15)
Label(main, text = "Do you have a H. pylori infection?").grid(row=16)
Label(main, text = "Do you have Von Hippel-Lindau syndrome?").grid(row=17)
Label(main, text = "Do you have MEN1 syndrome?").grid(row=18)
Label(main, text = "Your risk is:").grid(row=19)

#data input
age = Entry(main)
male = Checkbutton(main, text="Male", variable=is_male)
female = Checkbutton(main, text="Female")
smoker_yes = Checkbutton(main, text="Yes", variable=is_smoker)
smoker_no = Checkbutton(main, text="No")
history_yes = Checkbutton(main, text="Yes", variable=has_history)
history_no = Checkbutton(main, text="No")
t2d_yes = Checkbutton(main, text="Yes", variable=has_t2d)
t2d_no = Checkbutton(main, text="No")
overweight_yes = Checkbutton(main, text="Overweight", variable=is_overweight)
obese_yes = Checkbutton(main, text="Obese", variable=is_obese)
healthy_weight = Checkbutton(main, text="Neither")
pancreatitis_yes = Checkbutton(main, text="Yes", variable=has_pancreatitis)
pancreatitis_no = Checkbutton(main, text="No")
peutz_jeghers_yes = Checkbutton(main, text="Yes", variable=has_peutz_jeghers)
peutz_jeghers_no = Checkbutton(main, text="No")
cirrhosis_yes = Checkbutton(main, text="Yes", variable=has_cirrhosis)
cirrhosis_no = Checkbutton(main, text="No")
ashkenazi_yes = Checkbutton(main, text="Yes", variable=is_ashkenazi)
ashkenazi_no = Checkbutton(main, text="No")
poor_diet_yes = Checkbutton(main, text="Yes", variable=diet_healthiness)
poor_diet_no = Checkbutton(main, text="No")
FMM_yes = Checkbutton(main, text="Yes", variable="has_FMM_history")
FMM_no = Checkbutton(main, text="No")
HBOC_yes = Checkbutton(main, text="Yes", variable=has_HBOC_history)
HBOC_no = Checkbutton(main, text="No")
FAP_yes = Checkbutton(main, text="Yes", variable=has_FAP)
FAP_no = Checkbutton(main, text="No")
LFS_yes = Checkbutton(main, text="Yes", variable=has_LFS)
LFS_no = Checkbutton(main, text="No")
Lynch_yes = Checkbutton(main, text="Yes", variable=has_Lynch)
Lynch_no = Checkbutton(main, text="No")
H_pylori_yes = Checkbutton(main, text="Yes", variable=has_H_pylori)
H_pylori_no = Checkbutton(main, text="No")
VHL_yes = Checkbutton(main, text="Yes", variable=has_VHL)
VHL_no = Checkbutton(main, text="No")
MEN1_yes = Checkbutton(main, text="Yes", variable=has_MEN1)
MEN1_no = Checkbutton(main, text="No")

#result
blank = Entry(main)

#positioning of input boxes
age.grid(row=0, column=1)
male.grid(row=1, column=1, sticky=W)
female.grid(row=1, column=2, sticky=W)
smoker_yes.grid(row=2, column=1)
smoker_no.grid(row=2, column=2)
history_yes.grid(row=3, column=1)
history_no.grid(row=3, column=2)
t2d_yes.grid(row=4, column=1)
t2d_no.grid(row=4, column=2)
overweight_yes.grid(row=5, column=1)
obese_yes.grid(row=5, column=2)
healthy_weight.grid(row=5, column=3)
pancreatitis_yes.grid(row=6, column=1)
pancreatitis_no.grid(row=6, column=2)
peutz_jeghers_yes.grid(row=7, column=1)
peutz_jeghers_no.grid(row=7, column=2)
cirrhosis_yes.grid(row=8, column=1)
cirrhosis_no.grid(row=8, column=2)
ashkenazi_yes.grid(row=9, column=1)
ashkenazi_no.grid(row=9, column=2)
poor_diet_yes.grid(row=10, column=1)
poor_diet_no.grid(row=10, column=2)
FMM_yes.grid(row=11, column=1)
FMM_no.grid(row=11, column=2)
HBOC_yes.grid(row=12, column=1)
HBOC_no.grid(row=12, column=2)
FAP_yes.grid(row=13, column=1)
FAP_no.grid(row=13, column=2)
LFS_yes.grid(row=14, column=1)
LFS_no.grid(row=14, column=2)
Lynch_yes.grid(row=15, column=1)
Lynch_no.grid(row=15, column=2)
H_pylori_yes.grid(row=16, column=1)
H_pylori_no.grid(row=16, column=2)
VHL_yes.grid(row=17, column=1)
VHL_no.grid(row=17, column=2)
MEN1_yes.grid(row=18, column=1)
MEN1_no.grid(row=18, column=2)

blank.grid(row=19, column=1)

#buttons at bottom of screen
Button(main, text='Calculate Risk', command=calculate).grid(row=19, column=2, sticky=W)


mainloop()
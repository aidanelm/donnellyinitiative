import tkinter as tk

window = tk.Tk()
window.title("Risk Calculator")

user_risk = 1

print("What is your age?")

user_age = int(input())

if user_age >= 45 and user_age < 55:
    user_risk += 1

elif user_age >= 55 and user_age < 65:
    user_risk += 2

if user_age >= 65:
    user_risk += 3

print("Do you have diabetes? y/n")


print("Your risk is a " + str(user_risk) +".")
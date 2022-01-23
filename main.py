from connDatabase import *
from tkinter import * 

i = 0

while i == 0:
    print("Insert your username: ")
    name = input()
    print("Insert your password: ")
    password = input()
    i = login(name, password)

print("Login accepted")



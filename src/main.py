from classes.connDatabase import *
import tkinter as tk

def onClick():
    name = eUser.get()
    password = ePass.get()
    status = loginVerification(name, password)
    msg = ""
    
    if  status == 1:
        msg = "Login accepted"
    else: msg = "Wrong Password"

    warning = tk.Label(root, text=msg)
    warning.grid(column=1, row=3)

root = tk.Tk()

window = tk.Canvas(root, width=300, height=200)
window.grid(columnspan=3, pady=0, padx=0)

tUser = tk.Label(root, text="Login: ")
eUser = tk.Entry(root, width=30)
tPass = tk.Label(root, text="Password: ")
ePass = tk.Entry(root, width=30)
mainBtn = tk.Button(root, text="Submit", command=onClick)

tUser.grid(column=0, row=0, pady=5)
eUser.grid(column=1, row=0)
tPass.grid(column=0, row=1, pady=10)
ePass.grid(column=1, row=1)
mainBtn.grid(column=1, row=2, pady=10)

root.mainloop()




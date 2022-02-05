import tkinter as tk

class login(tk.Tk):
    def __init__(self):
        super().__init__()

        #Login window configuration
        self.title("Login")
        self.geometry("490x560+440+70")

        #Label
        self.tUser = tk.Label(self, text="Login: ")
        self.tPass = tk.Label(self, text="Password: ")
        
        #Entry
        self.eUser = tk.Entry(self, width=30)
        self.ePass = tk.Entry(self, width=30)
        
        #Button
        self.mainBtn = tk.Button(self, text="Submit")

        self.tUser.grid(column=0, row=0, pady=5)
        self.eUser.grid(column=1, row=0)
        self.tPass.grid(column=0, row=1, pady=10)
        self.ePass.grid(column=1, row=1)
        self.mainBtn.grid(column=1, row=2, pady=10)    

    def onClick(self):
        name = eUser.get()
        password = ePass.get()
        status = loginVerification(name, password)
        msg = ""

        if  status == 1:
            msg = "Login accepted"
        else: msg = "Wrong Password"

        warning = tk.Label(self, text=msg)
        warning.grid(column=1, row=3)
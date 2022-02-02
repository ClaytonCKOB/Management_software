#Class that will represent the user
class User:
    def __init__(self, name):
        # name As String
        # login As Integer, 0 = false, 1 = true
        self.name = name
        self.login = 0

    def login_state(self, login):
        self.login = login
#   21A21A0530
class Manager:
    def __init__(self):
        self.username = "devi"
        self.pswd = "530"

    def verify(self, user, pswd):
        if self.username == user and self.pswd == pswd:
            return "Successfully logged in"
        else:
            return "Unsuccessful login"

    def user_activation_status(self, user, activate_list):
        if user in activate_list:
            user.set_status("active")
            activate_list.remove(user)
            return user.get_name(), "Account activated"
        else:
            return "No records found for activation requests"
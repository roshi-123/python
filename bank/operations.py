class Operations:
    def deposit(self, current_amount, deposit_amount, user):
        user.set_amount(current_amount + deposit_amount)
        return "Deposit successful :)"

    def withdrawal(self, current_amount, withdrawal_amount, user):
        if withdrawal_amount > current_amount:
            return "Insufficient balance :("
        else:
            user.set_amount(current_amount - withdrawal_amount)
            return "Withdrawal successful :)"

    def balance(self, user):
        return f"Current balance: {user.get_amount()}"
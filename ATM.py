class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin  # User's PIN for security
        self.balance = balance  # Starting balance
        self.transaction_history = []  # To keep track of all transactions

    def check_pin(self):
        """Verifies the entered PIN against the user's PIN."""
        entered_pin = int(input("Enter your PIN: "))
        if entered_pin == self.pin:
            return True
        else:
            print("Incorrect PIN.")
            return False

    def balance_inquiry(self):
        """Displays the current balance."""
        print(f"Your current balance is: ${self.balance}")

    def cash_withdrawal(self):
        """Allows the user to withdraw cash from their account."""
        if self.check_pin():
            amount = float(input("Enter the amount to withdraw: "))
            if amount > self.balance:
                print("Insufficient balance.")
            else:
                self.balance -= amount
                self.transaction_history.append(f"Withdrew ${amount}")
                print(f"${amount} withdrawn successfully.")

    def cash_deposit(self):
        """Allows the user to deposit cash into their account."""
        if self.check_pin():
            amount = float(input("Enter the amount to deposit: "))
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            print(f"${amount} deposited successfully.")

    def change_pin(self):
        """Allows the user to change their PIN."""
        if self.check_pin():
            new_pin = int(input("Enter your new PIN: "))
            self.pin = new_pin
            self.transaction_history.append("PIN changed")
            print("PIN changed successfully.")

    def view_transaction_history(self):
        """Displays the transaction history."""
        print("Transaction History:")
        if not self.transaction_history:
            print("No transactions available.")
        else:
            for transaction in self.transaction_history:
                print(transaction)

def atm_menu(atm):
    """Displays the ATM menu and handles user input."""
    while True:
        print("\nATM Menu:")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Change PIN")
        print("5. View Transaction History")
        print("6. Exit")
        
        choice = input("Select an option: ")

        if choice == '1':
            atm.balance_inquiry()
        elif choice == '2':
            atm.cash_withdrawal()
        elif choice == '3':
            atm.cash_deposit()
        elif choice == '4':
            atm.change_pin()
        elif choice == '5':
            atm.view_transaction_history()
        elif choice == '6':
            print("Exiting. Thank you for using the ATM.")
            break
        else:
            print("Invalid option. Please try again.")

# Example usage
if __name__ == "__main__":
    # Create an instance of the ATM with a starting PIN and balance
    atm = ATM(pin=1234, balance=500.0)
    atm_menu(atm)


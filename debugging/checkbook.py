class Checkbook:
    """
    Class Description:
    A simple checkbook management system that allows deposits, withdrawals, and balance checking.

    Attributes:
        balance (float): The current balance of the checkbook.
    """
    def __init__(self):
        """
        Initializes the checkbook with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a specified amount into the checkbook.

        Parameters:
            amount (float): The amount to deposit into the checkbook.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the checkbook, if there are sufficient funds.

        Parameters:
            amount (float): The amount to withdraw from the checkbook.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current balance of the checkbook.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main function that runs the checkbook application, prompting the user for actions.
    """
    cb = Checkbook()
    
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        
        if action.lower() == 'exit':
            break
        
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value for the deposit amount.")
        
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value for the withdrawal amount.")
        
        elif action.lower() == 'balance':
            cb.get_balance()
        
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

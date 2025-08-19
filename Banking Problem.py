def show_balance(balance):
    print("****************")
    print(f"Your balance is:$ {balance:.2f}")
    print("***************")

def deposit(balance):
    deposit_amount = float(input("Enter deposit amount: "))
    if deposit_amount <=0:
        print("Deposit amount cannot be less than zero")
        return balance
    else:
        balance += deposit_amount
        print(f"Your updated balance is :${balance:.2f}")
        return balance

def withdraw(balance):
    withdraw_amount = float(input("Enter withdraw amount: "))
    if withdraw_amount > balance:
        print("You don't have enough money!")
    elif withdraw_amount < 0:
        print("Money cannot be negative!")
    else:
        balance -= withdraw_amount
        print(f"Your updated balance is :$ {balance:.2f}")
    return balance


def main():
    balance = 0
    is_running = True
    while is_running:
        print("*********************")
        print("Welcome to my Python Banking Program!!!")
        print("*********************")
        print("1.Balance" 
              "\n2.Deposit" 
              "\n3.Withdraw"
              "\n4.Exit")
        number=int(input("Enter your choice:"))
        if number==1:
            show_balance(balance)
        elif number==2:
            balance=deposit(balance)
        elif number==3:
            balance=withdraw(balance)
        elif number==4:
            is_running=False
            print("Thank you for using my Python Banking Problem")
        else:
            print("Invalid choice")
if __name__=='__main__':
    main()
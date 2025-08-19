def show_balance(balance):
    print("****************")
    print(f"Your balance is:$ {balance:.2f}")
    print("***************")
    if balance < 500:
        print("Please maintain your minimum balance!!")
    elif balance==500:
        print("You have enough minimum balance ")
    else:
        print("Your account is healthy!")

def deposit(balance):
    try:
        deposit_amount = float(input("Enter deposit amount: "))
        if deposit_amount <=0:
            print("Deposit amount cannot be less than or equal to zero")
            return balance
        else:
            balance += deposit_amount
            print(f"Your updated balance is :${balance:.2f}")
            return balance
    except ValueError:
        print("Invalid Input Please enter a valid value")
        return balance

def withdraw(balance):
    try:
        withdraw_amount = float(input("Enter withdraw amount: "))
        if withdraw_amount > balance:
            print("You don't have enough money!")
        elif withdraw_amount <= 0:
            print("Money cannot be zero or negative!")
        elif balance - withdraw_amount <500:
            print("Withdrawal denied ! Minimum balance of $500 must be maintained")
        else:
            balance -= withdraw_amount
            print(f"Your updated balance is :$ {balance:.2f}")
        return balance
    except ValueError:
        print("Invalid Input Please enter a valid value")
        return balance

def main():
    balance = 0
    is_running = True

    while balance<500:
        prev_balance=balance
        balance = deposit(balance)
        if balance == prev_balance:
            continue
        if balance < 500:
            print("Your bank balance is too low ,so you can't able to withdraw , Please deposit more!!")


    while is_running:
        print("*********************")
        print("Welcome to my Python Banking Program!!!")
        print("*********************")
        print("1.Balance"
              "\n2.Deposit"
              "\n3.Withdraw"
              "\n4.Exit")
        try:
            number=int(input("Enter your choice:"))
            if number==1:
                show_balance(balance)

            elif number==2:
                balance=deposit(balance)

            elif number==3:
                balance=withdraw(balance)

            elif number==4:
                confirm = input("Are you sure you want to exit? (y/n): ").strip().lower()
                if confirm=="y":
                    is_running=False
                    show_balance(balance)
                    print("Thank you for using my Python Banking Problem")
                else:
                    print("Exit cancelled .Returning to menu again...")
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid input. Please enter a number (1-4).")

if __name__=='__main__':
    main()
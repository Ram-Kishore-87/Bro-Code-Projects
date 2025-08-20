#Slot Machine Program
import random

def spin_row():
    symbol=['🍒','🍉','🍋','🔔','⭐']
    return [random.choice(symbol) for _ in range (3)]

def print_row(row):
    print("********************")
    print(" | ".join(f"{s:3}" for s in row))
    print("********************")

def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=='🍒':
            return bet*2
        elif row[0]=='🍉':
            return bet*3
        elif row[0]=='🍋':
            return bet*4
        elif row[0] =='🔔':
            return bet*5
        elif row[0]=='⭐':
            return bet*6
    return 0
def main():
    balance=100
    print("********************")
    print("Welcome to Python Slot Machine")
    print("********************")
    print("Symbols 🍒 🍉 🍋 🔔 ⭐")

    while balance>0:
        print(f"Your current balance is ${balance}")

        bet=(input("Enter your bet(or Q to quit): "))
        if bet.upper()=="Q":
            break
        if not bet.isdigit():
            print("Please enter a valid bet!!")
            continue
        if bet == balance:
            confirm = input("You are betting the entire amount of balance! Are you sure? (Yes/No): ").upper()
            if confirm not in ("Y","YES"):
                continue


        bet=int(bet)
        if bet>balance:
            print("Insufficient balance")
            continue

        if bet <=0:
            print("Bet must be greater than 0")
            continue

        balance-=bet

        row=spin_row()

        print("Spinning!!! \n")

        print_row(row)

        payout=get_payout(row,bet)

        if payout>0:
            print("********************")
            print("Hurray ! You won this round man!!!!")
            print("********************\n")
            print(f"Your payout is ${payout}")
        else:
            print("Sorry you lost this round!!!")
        balance+=payout

        play_again=input("Would you like to play again? (YES/NO): ").upper()

        if play_again not in ("Y","YES"):
            break
    print('*********************')
    print(f"Game Over! Your final balance is {balance}")
    print('*********************')
if __name__ == '__main__':
    main()
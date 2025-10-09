balance = 1000
pin = "1234"
def check_balance():
    global balance
    print(f"Your Current Balance is: {balance} USD")



def deposit_money(amount):
    global balance
    balance += amount
    print(f"{amount} USD deposited sucessfully! ")
    print(f"Your New Balance is: {balance} USD ")



def withdraw_money(amount):
    global balance
    if amount <= balance :
        balance -= amount
        print(f"{amount} USD withdrawn successfully! ")
    else:
        print("Insufficent Funds! ")
attempts = 3

while attempts > 0:
    entered_pin = input("Enter your 4-digit PIN: ")

    if entered_pin == pin:
        print("PIN accepted. Access granted!\n")
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN. {attempts} attempt(s) remaining.\n")

if attempts == 0:
    print("Too many incorrect attempts. Card blocked!")
    exit()





while True:
    print("\nWelcome to the ATM!")
    print("\n===== ATM MENU ====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("\nEnter your choice 1-4: ")
    
    if choice == "1" :
      check_balance()
    
    elif choice == "2" :
        amount = float(input("Enter the amount to deposit: "))
        deposit_money(amount)

    elif choice == "3" :
        amount = float(input("Enter the amount for withdrawal: "))
        withdraw_money(amount)
    
    elif choice == "4" :
      print("Thanks for using this ATM GOODBYE! ")
      break

    else:
      print("Please select a valid option!")


def deposit(name, amount):
    accounts[name] += amount
    print(f"Hi {name}! Your balance is ${accounts[name]} after deposit")


def withdraw(name, amount):
    if amount > accounts[name]:
        print("Insufficient funds! You are too poor for this.")
    else:
        accounts[name] -= amount
        print(f"Hi {name}! Your balance is ${accounts[name]} after Withdraw")


accounts = {
    "dij": 5000,
    "chiran": 200,
    "aakru": 10_500,
    "juna": 50_000,
    "dipak": 100
}
while True:
    name = input("Enter your name:").lower()
    if name.lower() == "exit":
        print("Closing the shop. GooDidbye!")
        break
    if name in accounts:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Logout")
        choice = input("Enter the choice(1-3):")
        if choice == "1":

            amount = int(input("Enter the amount for deposit:"))
            print("Enter the valid number")
            deposit(name, amount)

        elif choice == "2":
            amount = int(input("Enter the amount for Withdraw: "))
            withdraw(name, amount)

    else:
        print("Account donot exists!")
        new_account = input(
            f"Do you wanna create account with the name {name}(y/n)")
        if new_account == "y":
            initial_money = 0
            accounts[name] = initial_money
            print(
                f"Account created successfully for {name} with ${initial_money}!")
        elif new_account == "n":
            print("Thanks for choosing us")
        else:
            break

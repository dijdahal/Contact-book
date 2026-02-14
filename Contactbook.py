def display_screen():
    print("1. View")
    print("2. update")
    print("3. Exit")


def update_contact(name):
    new_num = input(f"Enter new number for {name}")
    contacts[name] = new_num
    print("Updated!!")


def add_new_contact(name):
    new_contact = input(f"Enter the new number for{name}")
    contacts[name] = new_contact


contacts = {"Dij": "0000", "Chiran": "6969", "Aakru": "98260", "Aash": "69"}

while True:
    name = input("Enter the name you are looking for Contact :")
    if name.lower() == "exit":
        print("Closing the shop. Goodbye!")
        break  # This 'kills' the heartbeat and stops the program
    if name in contacts:
        display_screen()

        choice = int(input("Enter your choice(1-3): "))
        if choice == 1:
            print(f"{contacts[name]}")
            print("\n")
        elif choice == 2:
            update_contact(name)
        elif choice == 3:
            print("eXITINGG THE PROGRAM..................")
            break
    else:
        add_new_contact(name)

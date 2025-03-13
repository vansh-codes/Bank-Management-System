import random

# Storing client data in dictionaries for better efficiency
clients = {
    "Dilraj Singh": {"mobile": "9988737374", "account": "A300185355", "pin": "0001", "balance": 10000},
    "Shlok Srivastava": {"mobile": "9786437893", "account": "A300147657", "pin": "0002", "balance": 20000},
    "Arvind Arora": {"mobile": "9835268593", "account": "A300124627", "pin": "0003", "balance": 30000},
    "Ajay Nager": {"mobile": "8736203905", "account": "A300196783", "pin": "0004", "balance": 40000},
    "Gaurav Taneja": {"mobile": "7593920024", "account": "A300135734", "pin": "0005", "balance": 50000},
}

fd_clients = {
    "Rajiv Bhatia": {"mobile": "9988737345", "fd_id": "F30011353", "amount": 100000, "years": 5}
}

# Function to authenticate user
def authenticate():
    name = input("Enter Registered Name: ")
    pin = input("Enter your PIN: ")
    if name in clients and clients[name]["pin"] == pin:
        return name
    print("Invalid name or PIN! Try again.")
    return None

while True:
    print("************************************************************")   
    print("========== WELCOME TO ITSOURCECODE BANKING SYSTEM ==========")
    print("************************************************************")
    print("==========     (a). Open New Client Account     ============")
    print("==========     (b). Fixed Deposit(FD)           ============")
    print("==========     (c). Withdraw Money              ============")
    print("==========     (d). Deposit Money               ============")
    print("==========     (e). Check Clients & Balance     ============")
    print("==========     (f). Check FD Clients            ============")
    print("==========     (g). Delete account              ============")
    print("==========     (h). Delete FD account           ============")
    print("==========     (i). Quit                        ============")
    print("************************************************************")

    choice = input("Select an option: ").lower()

    if choice == "a":
        if len(clients) >= 10:
            print("Client limit reached!")
            continue
        name = input("Enter your Full Name: ")
        mobile = input("Enter your Mobile Number: ")
        account = "A3001" + str(random.randint(10000, 99999))
        pin = input("Enter a 4-digit PIN: ")
        deposit = float(input("Enter initial deposit amount: "))
        clients[name] = {"mobile": mobile, "account": account, "pin": pin, "balance": deposit}
        print(f"Account created successfully!\nAccount Number: {account}\nBalance: {deposit}")

    elif choice == "b":
        name = input("Enter your Full Name: ")
        mobile = input("Enter your Mobile Number: ")
        fd_id = "F3001" + str(random.randint(1000, 9999))
        amount = float(input("Enter FD amount: "))
        years = int(input("Enter FD duration (years): "))
        interest = (amount * years * 6) / 100
        total_savings = amount + interest
        fd_clients[name] = {"mobile": mobile, "fd_id": fd_id, "amount": amount, "years": years}
        print(f"FD Created! FD ID: {fd_id}\nTotal Savings after {years} years: {total_savings}")

    elif choice == "c":
        user = authenticate()
        if user:
            amount = float(input("Enter withdrawal amount: "))
            if amount > clients[user]["balance"]:
                print("Insufficient funds!")
            else:
                clients[user]["balance"] -= amount
                print(f"Withdrawal successful! New Balance: {clients[user]['balance']}")

    elif choice == "d":
        user = authenticate()
        if user:
            amount = float(input("Enter deposit amount: "))
            clients[user]["balance"] += amount
            print(f"Deposit successful! New Balance: {clients[user]['balance']}")

    elif choice == "e":
        for name, details in clients.items():
            print(f"Client: {name}, Account: {details['account']}, Balance: {details['balance']}")

    elif choice == "f":
        for name, details in fd_clients.items():
            print(f"FD Client: {name}, FD ID: {details['fd_id']}, Amount: {details['amount']}, Years: {details['years']}")

    elif choice == "g":
        user = authenticate()
        if user:
            del clients[user]
            print("Account deleted successfully!")

    elif choice == "h":
        name = input("Enter FD Client Name: ")
        if name in fd_clients:
            del fd_clients[name]
            print("FD Account deleted successfully!")
        else:
            print("FD Client not found!")

    elif choice == "i":
        print("Thank you for using our banking system! Goodbye.")
        break

    else:
        print("Invalid choice! Try again.")

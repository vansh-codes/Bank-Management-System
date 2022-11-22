import random

FD_Clients = ['Rajiv Bhatia']                        #stored data for FD
FD_MobileNumber = ['9988737345']
FD_ID = ['F30011353']
FD_Amount = ['100000']
FD_Years = ['5']

NamesOFClients = ['Dilraj Singh', 'Shlok Srivastava', 'Arvind Arora', 'Ajay Nager', 'Gaurav Taneja']    
MobileNumber = ['9988737374','9786437893','9835268593','8736203905','7593920024']
AccountNumber = ['A300185355','A300147657','A300124627','A300196783','A300135734']
ClientPins = ['0001', '0002', '0003', '0004', '0005']
ClientBalances = [10000, 20000, 30000, 40000, 50000]
ClientDeposition = 0
ClientWithdrawal = 0
ClientBalance = 0
disk1 = 1
disk2 = 5
disk3 = 1
u = 0
v=0
def pass1():
    global v
    global w
    while v < 1:
        w = -1
        name = input("Enter Registered Name : ")
        pin = input("Enter your Pin : ")
        while w < len(NamesOFClients) - 1:
            w = w + 1
            if name == NamesOFClients[w]:
                if pin == ClientPins[w]:
                    v = v + 1
                    return True
            else:
                return False
while True:
    print("************************************************************")        #Mainmenu
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

    SelectLetter = input("Select a Letter from the Above Box Menu : ")
    
    if SelectLetter == "a":                                                     #Program for 'a' menu
        NumberOfClient = eval(input("Number of Clients : "))
        u = u + NumberOfClient

        if u > 5:
            print("\n")
            print("Sorry! Cannot register more than 5 customers")
            print("Please Try Again!")
            u = u - NumberOfClient
        else:
            while disk1 <= u:
                name = input("Enter your Fullname : ")
                NamesOFClients.append(name)
                mobilenum = int(input("Enter your Mobile Number : "))
                MobileNumber.append(mobilenum)
                gen_account = random.randint(10000,99999)                      #Generating random Acc.no
                account = "A3001" + str(gen_account)                           #A3001 is the bank's branch code
                AccountNumber.append(account)
                pin = str(input("Please Enter a 4 digit Pin to Secure your Account : "))
                ClientPins.append(pin)
                ClientBalance = 0
                ClientDeposition = eval(input("Please enter amount to Deposit to Start an Account : "))
                ClientBalance = ClientBalance + ClientDeposition
                ClientBalances.append(ClientBalance)
                print("\nName = ", end=" ")
                print(NamesOFClients[disk2])
                print("Mobile Number = ", end=" ")
                print(MobileNumber[disk2])
                print("Account Number = ", end =" ")
                print(AccountNumber[disk2])
                print("Pin = ****", end=" ")
                print(ClientPins[disk2])
                print("Balance = ", "P", end=" ")
                print(ClientBalances[disk2], end=" ")
                disk1 = disk1 + 1
                disk2 = disk2 + 1
                print("\nYour name is added to Client Table")
                print("Your account number is added to Client Table")
                print("Your pin is added to Client Table")
                print("Your balance is added to Client Table")
                print("----**New Account created Successfully !**----")
                print("******Your account has been secured by the Pin*******")
                print("******DO NOT share your ACCOUNT PIN with anyone******")
                print("\n")
                print("Your Name is now available on the Client list now : ")
                print(NamesOFClients)
                print("\n")
                print("Note! Please remember the Name, Registered Mobile Number and Pin")
                print("========================*************===========================")

        mainMenu = input(" Press Any Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
        
    elif SelectLetter == "b":                                                     #Program for 'b' menu
        NumberOfClient = eval(input("Number of Clients : "))
        u = u + NumberOfClient

        if u > 5:
            print("\n")
            print("Client registration exceed reached or Client registration too low")
            u = u - NumberOfClient
        else:
            while disk3 <= u:
                name = input("Enter your Fullname : ")
                FD_Clients.append(name)
                mobilenum = int(input("Enter your Mobile Number : "))
                FD_MobileNumber.append(mobilenum)
                gen_id = random.randint(1000,9999)
                fdid = "A3001" + str(gen_id)                                     #Generating random FD Acc.no
                FD_ID.append(fdid)        
                FD_Am = eval(input("Please enter amount to create FD : "))
                FD_Am = 0 + FD_Am
                FD_Amount.append(FD_Am)
                FD_t = eval(input("Please enter years for FD : "))
                FD_Years.append(FD_t)
                print("\n")
                print("Rate of Interest on FD is 6%")
                print("\n")
                FD_save = (FD_Am*FD_t*6)/100
                FD_Savings = FD_Am + FD_save
                print("Interest Amount is :",FD_save)
                print("Your Savings till next",FD_t,"years is ",FD_Savings)
                print("\nName = ", end=" ")
                print( FD_Clients[disk3])
                print("Mobile Number = ", end=" ")
                print(MobileNumber[disk3])
                print("FD ID = ", end =" ")
                print(FD_ID[disk3])
                print("Amount = ", end=" ")
                print(FD_Amount[disk3], end=" ")
                print("\n")
                print("Total Savings after 5 years will be :",FD_Savings)
                disk3 = disk3 + 1
                print("\n")
                print("----**FD created successfully !**----")
                print("\n")
                print("\n")
                print("Note! Please remember the Name, Registered Mobile Number and FD ID")
                print("==========================*************===========================")

        mainMenu = input(" Press Any Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
        
    elif SelectLetter == "c":                                                     #Program for 'c' menu
        if pass1()==True:
            print("Your Current Balance:", "P", end=" ")
            print(ClientBalances[w], end=" ")
            print("\n")
            ClientBalance = (ClientBalances[w])
            ClientWithdrawal = eval(input("Enter amount to Withdraw : "))
            if ClientWithdrawal < 0.05*ClientBalance:
                print("Withdrawal amount should be more than 5% of the balance!")
                print("Enter amount more than ",0.05*ClientBalance)
                ClientWithdrawal = eval(input("Enter amount to Withdraw : "))
                ClientBalance = ClientBalance - ClientWithdrawal
                print("\n")
                print("----Withdraw Successfully!----")
                ClientBalances[w] = ClientBalance
                print("Your New Balance: ", "P", ClientBalance, end=" ")
                print("\n\n")
            elif ClientWithdrawal > ClientBalance:
                print("Withdrawal Fail! Withdrawal money exceeds your balance! ")                        
                print("Enter amount less than ",ClientBalance)
                ClientWithdrawal = eval(input("Insert value to Withdraw : "))
                ClientBalance = ClientBalance - ClientWithdrawal
                print("\n")
                print("----Withdraw Successfully!----")
                ClientBalances[w] = ClientBalance
                print("Your New Balance: ", "P", ClientBalance, end=" ")
                print("\n\n")
            else:
                ClientBalance = ClientBalance - ClientWithdrawal
                print("\n")
                print("----Withdraw Successfully!----")
                ClientBalances[w] = ClientBalance
                print("Your New Balance: ", "P", ClientBalance, end=" ")
                print("\n")
        if v < 1:
            print("Your Record not found or name and pin does not match!\n")     
        mainMenu = input(" Press Any Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
        
    elif SelectLetter == "d":                                                     #Program for 'd' menu
        if pass1()==True:
            print("Your Current Balance: ", "P", end=" ")
            print(ClientBalances[w], end=" ")
            ClientBalance = (ClientBalances[w])
            print("\n")
            ClientDeposition = eval(input("Enter amount to deposit : "))
            ClientBalance = ClientBalance + ClientDeposition
            ClientBalances[w] = ClientBalance
            print("\n")
            print("----Deposition successful!----")
            print("Your New Balance: ", "P", ClientBalance, end=" ")
            print("\n")
        if v < 1:
            print("Your Record not found or name and pin does not match!\n")
        mainMenu = input(" Press Any Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
        
    elif SelectLetter == "e":                                                     #Program for 'e' menu
        w = 0
        print("Client name list and balances mentioned below : ")
        print("\n")
        if w <= len(NamesOFClients) - 1:
            while w <= len(NamesOFClients) - 1:
                print("-> Customer = ", NamesOFClients[w])
                print("-> Mobile Number = ", MobileNumber[w])
                print("-> Account Number = ", AccountNumber[w])
                print("-> Balance = ", "P", ClientBalances[w], end=" ")
                print("\n")
                w = w + 1
        else:
            print("!!!No Record Found!!!")
            print("******************************") 
        mainMenu = input(" Press Any Key to go Back to Main Menu to Conduct Another Transaction or Quit_ ")
        
    elif SelectLetter == "f":                                                     #Program for 'f' menu
        w = 0
        print("FD Client Name mentioned below : ")
        print("\n")
        if w <= len(FD_Clients) - 1:
            while w <= len(FD_Clients) - 1:
                print("-> Customer = ", FD_Clients[w])
                print("-> Mobile Number = ", FD_MobileNumber[w])
                print("-> FD_ID = ", FD_ID[w])
                print("-> Amount = ", FD_Amount[w])
                print("-> Years = ", FD_Years[w])
                print("\n")
                w = w + 1
        else:
                print("!!!!!No Record Found!!!!!")
                print("******************************") 
        mainMenu = input(" Press Any Key to go Back to Main Menu to Conduct Another Transaction or Quit_ ")

    elif SelectLetter == "g":                                     #Program for 'g' menu
        if pass1()==True:
            del NamesOFClients[w]
            del MobileNumber[w]
            del AccountNumber[w]
            del ClientPins[w]
            del ClientBalances[w]
            disk2 = disk2-1
            print("v",v)
            print("!!ACCOUNT DELETED!!")
            print("!!NOTE : You can create another account anytime!!")
            print("*****Thank you for your visit!*****")
        if v < 1:
            print("Your Record not found or name and pin does not match!\n")
                    
        mainMenu = input(" Press Any Key to go Back to Main Menu to Conduct Another Transaction or Quit_ ")
        
    elif SelectLetter == 'h':                                            #Program for 'h' menu
        v = 0
        while v < 1:
            w = -1
            name = input("Enter Registered Name : ")
            while w < len(FD_Clients) - 1:
                w = w + 1
                if name == FD_Clients[w]:
                    v = v + 1
                    del FD_Clients[w]
                    del FD_MobileNumber[w]
                    del FD_ID[w]
                    del FD_Amount[w]
                    del FD_Years[w]
                    disk3 = disk3-1
                    print("!!ACCOUNT DELETE!!")           
                    print("!!NOTE : You can create another account anytime!!")
                    print("*****Thank you for your visit!*****")
                else:
                    print("Incorrect Username Entered!")
                    
        mainMenu = input(" Press Any Key to go Back to Main Menu to Conduct Another Transaction or Quit_ ")


    elif SelectLetter == "i":                                                     #Program for 'i' menu
        print("Thank you for using and trusting our banking system!")
        print("Thank You! ")
        print("Visit Again! ")
        print("Have A Good Day!")
        break

    else:
        print("Invalid choice!")
        print("Please choose from Menu")
        print("Please Try again!")

        mainMenu = input("Press Any Key to go Back to Main Menu to Conduct Another Transaction or Quit_")

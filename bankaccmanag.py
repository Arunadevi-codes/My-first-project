class bankaccount:
    def __init__(self):
        self.Available_amount = 5000
        name=input("Enter your name: ")
        Acc_no=int(input("Enter your Account number: "))
        print("-----------Hello", name, "Welcome-----------")
        print("Your Available balance", self.Available_amount)
        

    def menu(self):
        print("\n1. Deposite")
        print("2. Withdraw")
        print("3. See Available balance")
        print("4. Exit")
        self.choice = int(input("Enter your choice: "))
        return self.choice

    def deposite(self):
        amt= int(input("Enter amount to be deposited: "))
        self.Available_amount+=amt
        print(amt, "Amount deposited successfuly")

    def withdraw(self):
        wamt= int(input("Enter amount to be withdraw: "))
        if (wamt<=self.Available_amount):
            self.Available_amount-=wamt
            print(wamt, "Withdrawn Successfully")
        else:
            print("Insufficient balance")
    

    def display(self):
        print("Availabe balance: ", self.Available_amount)

bank=bankaccount()


while True:
    bank.menu()
    if (bank.choice ==1):
        bank.deposite()
    elif (bank.choice ==2):
        bank.withdraw()
    elif (bank.choice == 3):
        bank.display()
    elif (bank.choice == 4):
        print("========Thank you========")
        break


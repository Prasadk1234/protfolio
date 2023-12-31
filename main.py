print("""What is the difference between Functions and methods
methods are who can written in class and represent the class. Fuctions are those 
      who can write function without any class""")


class Atm:

    def __int__(self):
        self.pin = ""
        self.balance = 0

        self.menu()

    def menu(self):
        user_input = input("""
        How would like to proceed?
        1. Enter to create pin
        2. Enter 2 to Deposit
        3. Enter 3 to withdraw
        4. Enter to check balance
        5. Enter 5 to exit
        """)
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.deposite()
        elif user_input == '3':
            self.cash_withdraw()
        elif user_input == '4':
            self.check_balance()
        else:
            print('bye')

    def create_pin(self):
        self.pin = input('Enter Your PIN')
        print('Pin set successfully')
        self.menu()

    def deposite(self):
        temp = input('Enter the pin')
        if temp == self.pin:
            amount = int(input('Enter the amount'))
            self.balance = self.balance + amount
            print('deposite Successfully')
        else:
            print('insufficient balance')

        self.menu()

    def cash_withdraw(self):
        temp = input('Enter your pin')
        if temp == self.pin:
            amount = int(input('Enter the amount'))
            if amount < self.balance:
                self.balance = self.balance - amount
                print('operation Successful')
            else:
                print('insufficient fund')
        else:
            print('Incorrect Pin')

        self.menu()

    def check_balance(self):
        temp = input('Enter your pin')
        if temp == self.pin:
            print(self.balance)
        else:
            print('invalid pin')
        self.menu()


p = Atm()
p.menu()

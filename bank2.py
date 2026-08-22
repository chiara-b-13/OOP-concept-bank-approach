import random 

class Users:
    def __init__(self, username, password, ID, email):
        self.username = username
        self.password = password
        self.ID = ID
        self.email = email
        self.balance = 0

    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password
    
    def get_ID(self) :
        return self.ID
    
    def get_email(self):
        return self.email
    
    def get_balance(self):
        return str(self.balance)
    
    def increase_balance(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def decrease_balance(self, amount):
        self.balance = self.balance - amount
        return self.balance

email_list = []
numbers = []
dict_user = {} # key : id, value : user
system = True
user = None

def registration():
    print('-- Registration --')
    name = input('Enter account name:   ')
    if len(name) == 0:
        print('Account name cannot be blank.')
        registration()
    else:
        email_condition = False
        while email_condition == False:
            email = input('Enter email name:   ')
            if '@' and '.' not in email:
                print('You must enter a valid email.')
                email_condition = False
            elif len(email) == 0:
                print('Email cannot be blank')
                email_condition = False
            elif email in email_list:
                print('This email already exists, please use another one')
                email_condition = False
            else:
                email_condition = True
                email_list.append(email)
        password_condition = False
        while password_condition == False:
            password = input('Enter password:  ')
            if len(password) == 0:
                print('Password cannot be blank.')
                password_condition = False
            else:
                password_condition = True

        password1_condition = False
        while password1_condition == False:
            passconfirm = input('Re-enter password to confirm:  ')     
            if passconfirm != password:
                print('Password must be the same.')
                password1_condition = False
            else:
                password1_condition = True

        A = random.randint(1, 99999999)
        while A in numbers : 
            A = random.randint(1, 99999999)
        numbers.append(A)

        user = Users(name, password, A, email)
        dict_user[A] = user

        print(dict_user[A].get_username())
        print(dict_user[A].get_password())
        print(dict_user[A].get_ID())
        print(dict_user[A].get_email())
        print(dict_user[A].get_balance())
        print('You have successfully made your account, your current balance is 0 Rp.')

def login():
    loginID = int(input('Enter your ID:     '))
    loginpass = input('Enter your password:     ')
    try : 
        user = dict_user[loginID]
        if user.get_password() == loginpass: 
            print('succesfully logged in !')
            return user
        else:
            print('the password you have entered is incorrect, please try again.')
            return 
    except :
        print('Please make an account first before logging in.')
        return 
    
    

def user_screen(user) :

    print('+=======================================================================+')
    print('Welcome to the bank.')
    print(user.get_username())
    print('+=======================================================================+')
    print('1 - deposit')
    print('2 - withdraw')
    print('3 - transfer')
    print('4 - balance')
    print('5 - logout')

    q1 = input('What would you like to do today?:   ')
    if q1 == '1':
        deposit(user)
    elif q1 == '2':
        withdrawal(user)
    elif q1 == '3':
        transfer(user)
    elif q1 == '4':
        balance1(user)
    elif q1 == '5':
        return
    else:
        print("Sorry, i don't understand what you mean by that.")
    user_screen(user)

def deposit(user):
    amount = int(input('Amount you want to deposit:     '))
    if amount < 0:
        print('Amount cannot be below 0.')
        deposit(user)
    else:
        print(user.get_username())
        print(user.get_balance())
        last_amount = user.increase_balance(amount)
        print(last_amount)
        user_screen(user)

def withdrawal(user):
    withdrawal_condition = True
    while withdrawal_condition == True:
        amount = int(input('Amount you want to deposit:     '))
        if amount <= 0:
            print('Amount cannot be less then or equal to 0')
        elif amount > int(user.get_balance()):
            print('Amount must be less then your current balance')
            
        else:
            last_amount = user.decrease_balance(amount)
            print(last_amount)
            withdrawal_condition == False
            user_screen(user)

def transfer(user):
    transfer_condition = True
    destination = int(input('Which account would you like to transfer to?:      '))
    if int(user.get_ID()) == destination:
        print('You cannot transfer to your own account.')
        return
    elif destination in numbers:
        user_destination = dict_user[destination]
    else : 
        print('Sorry, this account does not exist in our system.')
        return

    

    amount = int(input('Amount you want to transfer:     '))
    if amount <= 0:
        print('Amount cannot be less then or equal to 0')
    elif amount > int(user.get_balance()):
        print('Amount must be less then your current balance')
    else:
        last_amount = user.decrease_balance(amount)
        print(last_amount)

        last_amount = user_destination.increase_balance(amount)
        print(last_amount)


    return

def balance1(user):
    print('Your current balance is:     ')
    print(user.get_balance())
    user_screen(user)

# def start():
#     print('+=======================================================================+')
#     print('Welcome to the bank.')
#     print('+=======================================================================+')
#     print('1 - login')
#     print('2 - registration')
#     print('3 - login ( admin )')
#     print('4 - exit')

#     q1 = input('What would you like to do today?:   ')
#     if q1 == '2':
#         registration()
#     elif q1 == '1':
#         login()
#     elif q1 == '4':
#         print('Thank you for using our bank.')
#     else:
#         print("Sorry i don't understand what you mean by that.")


while system == True:
    print('+=======================================================================+')
    print('Welcome to the bank.')
    print('+=======================================================================+')
    print('1 - login')
    print('2 - registration')
    print('3 - login ( admin )')
    print('4 - exit')

    q1 = input('What would you like to do today?:   ')
    if q1 == '2':
        registration()
        system = True
    elif q1 == '1':
        user = login()
        print(user)
        if len(user.get_username()) > 0 : 
            user_screen(user)
        system = True
    elif q1 == '4':
        print('Thank you for using our bank.')
        system = False
    else:
        print("Sorry i don't understand what you mean by that.")
        system = True
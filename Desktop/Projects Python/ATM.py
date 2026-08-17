correct_pin = 1234
attempts = 3
balance = 10000
flag = False
transactions = []

while attempts>0:
    print('='*40)
    pin = int(input('Enter the Pin : '))
    if pin == correct_pin:
        print('Login Successfull ')
        flag = True
        break
    else:
        attempts -=1
        if attempts <=0:
            print('Maximum Attempts Failed')
            print('Account Blocked')
            break
        print('Incorrect Pin Try again')
        print('Available Attempts : ',attempts)
if flag:
    while True:
        print('='*40)
        print('ATM Menu')
        print('1.Check Balance')
        print('2.Deposit Money')
        print('3.Withdraw Money')
        print('4.Mini Statement')
        print('5.Exit')
        print('='*40)
        choice = int(input('Enter Your Choice : '))
        if choice == 1:
            print('='*40)
            print('Available Balance : ',balance)
            print('='*40)
        elif choice == 2:
            print('='*40)
            amount = float(input('Enter Money To Deposit : '))
            balance += amount
            transactions.insert(0,'Amount Deposited '+str(amount))
            print('Amount Deposited Successfully : ',amount)
            print('='*40)
        elif choice == 3:
            print('='*40)
            amount = float(input('Enter Money to withdraw : '))
            if amount <=0:
                print('Invalid amount')
            elif amount%100 !=0:
                print('Enter amount only multiples of 100')
            elif amount>balance:
                print('Insufficient Balance')
            else:
                print('Money withdraw Successfully',amount)
                transactions.insert(0,'Money Withdraw '+str(amount))
                balance -= amount
            print('='*40)
        elif choice == 4:
            print('='*40)
            for i in transactions:
                print(i)
            print('='*40)
        elif choice == 5:
            print('='*40)
            print('Thank You For Using ATM')
            print('='*40)
            break
        else:
            print('Invalid Choice')

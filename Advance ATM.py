import time
import getpass

print("Enter Your Card Please : --------")
time.sleep(0)
Password = 1234
for attempt in range(3):
    pin = int(input("Enter Your Pin: "))
    if pin == Password:
        break
    else:
        print(f'Incorrect PIN. {2 - attempt} attempts remaining.')
else:
    print("Too many incorrect attempts. Exiting.")
    exit()
Balance = 100000
print("    Welcome Jaydev Pokahriyal Sir \n   How can i Hep you")
print("=====================================================")
print('''1 = Balance Enquiry.  2 = Cash Withdrawl.\n3 = Banking.          4 = KYC Enquiry.''')
fch = int(input("Choose any one please (1-4) : "))
print("=====================================================")
if fch == 1:
    print("Your Account Balance is", Balance, "Rs...")
    print("thanks for visit our ATM\nHave a nice day sir !")
if fch == 2:
    print("_________How many cash you want Sir / Madam _________")
    Withdrawl_Amount = int(input("Enter Amount : "))
    if (Withdrawl_Amount > Balance):
        print("You Can't withdrawl this Amount")
    else:
        Remaining_Balance = Balance - Withdrawl_Amount
        print(f"Withdrawal successful. Remaining balance is : {Remaining_Balance} Rs.")
        print("Thanks for using our ATM. Have a nice day Sir/Madam !")
if fch == 3:
    print(
        '''1 = Create a new Account.               2 = Open Fixed Deposit Scheme.\n3 = Apply for new Credit card.          4 = Complain.''')
    fch = int(input("Choose any one please (1-4) :"))
    if fch == 1:
        name = input("Enter your name : ")
        age = input("Enter your age : ")
        pan = getpass.getpass("Enter PAN No : ")
        aadhar = int(input("Enter Aadhar No : "))
        mobile_no = int(input("Enter Your Mobile No : "))
        address = input("Enter Address : ")
        email = input("Enter your email address : ")
        print("Thank you for submitting the form!")
        print("===============================================")
        print("Name : ", name)
        print("Age : ", age)
        print("PAN No : ", pan)
        print("Aadhar No : ", aadhar)
        print("Mobile No : ", mobile_no)
        print("Address : ", address)
        print("Email : ", email)
        print("===========================================")
        print("Please wait I'll verifying your Data which you have given......")
        time.sleep(5)

        print("Your Account has been succesfully created..")

        print("Account Holder name:", name)
        print("Account no: 0262000101339377")
        print("IFSC Code: PUNB0026200")
        print("Address: durga colony kashipur (u.s.nagar)")
        print("Mobile No:", mobile_no)

    if fch == 2:
        name = input("Enter your name : ")
        age = input("Enter your age : ")
        pan = getpass.getpass("Enter PAN No : ")
        aadhar = int(input("Enter Aadhar No : "))
        mobile_no = int(input("Enter Your Mobile No : "))
        address = input("Enter Address : ")
        email = input("Enter your email address : ")

        print("Thank you for submitting the form!")
        print("===========================================")
        print("Name : ", name)
        print("Age : ", age)
        print("PAN No : ", pan)
        print("Aadhar No : ", aadhar)
        print("Mobile No : ", mobile_no)
        print("Address : ", address)
        print("Email : ", email)
        print("Please wait I'll verifying your Data which you have given......")
        time.sleep(5)

        print("Ok, the data you have given is absolutely correct.")
        print("So tell me which of these offers do you want ?")
        print("==========================================================")
        print('''1 = 1 year Deposit (7%)\n2 = 3 year Deposit(8.5%)\n3 = 5 year Deposit(12.5%)''')

    if fch == 3:
        name = input("Enter your name : ")
        age = input("Enter your age : ")
        pan = getpass.getpass("Enter PAN No : ")
        aadhar = float(input("Enter Aadhar No : "))
        mobile_no = float(input("Enter Your Mobile No : "))
        address = input("Enter Address : ")
        email = input("Enter your email address : ")

        print("Thank you for submitting the form!")
        print("============================================================")

        print("Name : ", name)
        print("Age : ", age)
        print("PAN No : ", pan)
        print("Aadhar No : ", aadhar)
        print("Mobile No : ", mobile_no)
        print("Address : ", address)
        print("Email : ", email)

        print("Please wait I'll verifying your Data which you have given......")
        time.sleep(5)

        print("Ok, the data you have given is absolutely correct.")
        print("===========================================")
        print("Your Account has been succesfully created..")

        print("Account Holder name : ", name)
        print("Credit Card No : ", 2447130001)
        print("DOB : ", "16/07/2001")
        print("Expiry Date :", "12/30")
    if fch == 4:
        print("Please Leave your comment here")

        comment = (input("Enter your Comment here : "))

        print("Thanks for your feedback")

        print("We will definitely try to find a solution to your complaint.\nThanks for giving your opinion.")

if fch == 4:
    print("Welcome ot our KYC Enquiry portal ")
    aadhar = int(input("Enter your aadhar no : "))
    pan = getpass.getpass(input("Enter your pan no : "))

    print("Thank you for submitting the form!")

print("Thanks for your Contribution in kyc update")
print()
print("We will update your KYC as soon as possible")

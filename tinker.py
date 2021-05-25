#imports
from tkinter import *
import os
import random
from PIL import ImageTk, Image

#main screen
master = Tk()
master.title("Banking Model")


#Account number Generation
global account_number

account_number = random.randint(1055510,9981010)
account_number = str(account_number)

#Function
def finish_reg():
    name =temp_name.get()
    age =temp_age.get()
    gender =temp_gender.get()
    Phone =temp_Phone.get()
    password =temp_password.get()
    all_accounts= os.listdir()

    if name == "" or age == "" or gender == "" or Phone == "" or password == "" :
        notif.config(fg="red",text="All fields are Required *")
        return

    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg="red",text="Account already exits ")
            return
        else:
            new_file=open(name,"w")
            
            new_file.write(name + "\n")
            new_file.write(age + "\n")
            new_file.write(gender + "\n")
            new_file.write(Phone + "\n")
            new_file.write("0" + "\n" )
            new_file.write(password + "\n")
            new_file.write(account_number)
            new_file.close()
            notif.config(fg="blue",text="Your Account is sucessfully created\n\nYour Account Number is " + str (account_number))
            #notif.config(fg="blue",text="Your Account Number is " + str (account_number))

    

def register():
    #var_define
    global temp_name
    global temp_age
    global temp_gender
    global temp_Phone
    global temp_password   
    global notif
    
    temp_name=StringVar()
    temp_age=StringVar()
    temp_gender=StringVar()
    temp_Phone=StringVar()
    temp_password=StringVar()

    #register screen
    register_screen=Toplevel(master)
    register_screen.title("Register")
    

    #Label
    Label(register_screen, text="Enter the following details ", font=("calibri",14)).grid(row=0,pady=12,sticky=N)
    Label(register_screen, text="NAME  ", font=("calibri",12)).grid(row=1,sticky=W,pady=5)
    Label(register_screen, text="AGE  ", font=("calibri",12)).grid(row=2,sticky=W,pady=5)
    Label(register_screen, text="GENDER  ", font=("calibri",12)).grid(row=3,sticky=W,pady=5)
    Label(register_screen, text="Phone No.  ", font=("calibri",12)).grid(row=4,sticky=W,pady=8)
    Label(register_screen, text="PASSWORD  ", font=("calibri",12)).grid(row=5,sticky=W,pady=5)
    
    notif=Label(register_screen, font=("calibri",12))
    notif.grid(row=8,sticky=N,pady=10)

    #Entries
    Entry(register_screen, textvariable=temp_name).grid(row=1,column=0,sticky=E)
    Entry(register_screen, textvariable=temp_age).grid(row=2,column=0,sticky=E)
    Entry(register_screen, textvariable=temp_gender).grid(row=3,column=0,sticky=E)
    Entry(register_screen, textvariable=temp_Phone).grid(row=4,column=0,sticky=E)
    Entry(register_screen, textvariable=temp_password,show="*").grid(row=5,column=0,sticky=E)

    #Button
    Button(register_screen, text="Register", command=finish_reg, font=("calibri",12)).grid(row=6,pady=10,sticky=N)

def finish_deposit():
    if amount.get() == "" :
        deposit_notif.config("Amount is required", fg="red")
        return
    if float(amount.get()) <=0 :
        deposit_notif.config("Please enter a valid Amount", fg="red")
        return

    file= open(login_name,"r+")
    file_data= file.read()
    details= file_data.split("\n")
    current_balance= details[4]
    updated_balance= current_balance
    updated_balance= float(current_balance) + float(amount.get())
    file_data= file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Current Balance: Rs." + str(updated_balance), fg="green")
    deposit_notif.config(text="Balance Updated", fg="green")
        
def finish_withdraw():
    if withdraw_amount.get() == "" :
        withdraw_notif.config("Amount is required", fg="red")
        return
    if float(withdraw_amount.get()) <= 0 :
        withdraw_notif.config("Please enter a valid Amount", fg="red")
        return

    file= open(login_name,"r+")
    file_data= file.read()
    details= file_data.split("\n")
    current_balance= details[4]

    if float(withdraw_amount.get()) > float(current_balance):
        withdraw_notif.config(text="Insufficent Fund!!", fg="red")
        return
    
    updated_balance= current_balance
    updated_balance= float(current_balance) - float(withdraw_amount.get())
    file_data= file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Current Balance: Rs." + str(updated_balance), fg="green")
    withdraw_notif.config(text="Balance Updated", fg="green")


def finish_fd():
    try:
        if fd_amount.get() == ""  :
            fd_notif.config("Amount is required", fg="red")
            return
        if fd_time.get() == ""  :
            fd_notif.config("Enter Time for F.D.", fg="red")
            return
        if float(fd_amount.get()) <= 0 :
            fd_notif.config("Please enter a valid Data", fg="red")
            return

        if fd_time.get() == "":
            fd_notif.config("Please enter a valid Data", fg="red")
            reverse

    except ValueError:
            fd_notif.config("Enter Valid Info", fg="red")
            
            
    
    file= open(login_name,"r+")
    file_data= file.read()
    details= file_data.split("\n")
    current_balance= details[4]

    if float(fd_amount.get()) > float(current_balance) :
        fd_notif.config(text="Insufficent Fund!!", fg="red")
        return

    if float(fd_amount.get()) < 10000:
        fd_notif.config(text="Amount Should be greater than 10,000/-!!", fg="red")
        return
    
    updated_balance= current_balance
    updated_balance= float(current_balance) - float(fd_amount.get())
    file_data= file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    fd_notif.config(fg="green",text="Your F.D. is sucessfully created \n " "Current Balance: Rs." + str(updated_balance))

def return_table():

    #FD3 screen
    fd2_screen.destroy()
    fd3_screen = Toplevel(master)
    fd3_screen.title("Fixed Deposit")
    

def fd2():
    #Variables
    global fd_amount
    global fd_time
    global fd2_screen
    global fd_notif
    
    fd_amount=StringVar()
    fd_time=StringVar()
    
    #Login screen
    fd2_screen = Toplevel(master)
    fd2_screen.title("Fixed Deposit")

    #Label
    Label(fd2_screen, text="Enter the following details ", font=("calibri",14)).grid(row=0,pady=12,sticky=N)
    Label(fd2_screen, text="Amount  ", font=("calibri",12)).grid(row=1,sticky=W,pady=5)
    Label(fd2_screen, text="Time  ", font=("calibri",12)).grid(row=2,sticky=W,pady=5)

    fd_notif=Label(fd2_screen, font=("calibri",12))
    fd_notif.grid(row=3,sticky=N,pady=10)

    #Entries
    Entry(fd2_screen, textvariable=fd_amount).grid(row=1,column=0,sticky=E)
    Entry(fd2_screen, textvariable=fd_time).grid(row=2,column=0,sticky=E)

    #Button
    Button(fd2_screen, text="Register", command=finish_fd, font=("calibri",12)).grid(row=4,pady=10,sticky=N)
    Button(fd2_screen, text="Return Table", command=return_table, font=("calibri",12)).grid(row=4,column=0,pady=10,sticky=W)
    
def fd():

    
    #Login screen
    fd_screen = Toplevel(master)
    fd_screen.title("Fixed Deposit")

    #Label
    Label(fd_screen,fg="orange", text="Important Info. for F.D.", font=("calibri",16)).grid(row=0,pady=12,sticky=N)
    Label(fd_screen, text="1. Amount Should be greater than 10,000/-", font=("calibri",12)).grid(row=1,sticky=W)
    Label(fd_screen, text="2. Time should be in mutiple of 1 year", font=("calibri",12)).grid(row=2,sticky=W)
    Label(fd_screen, text="3. Fixed Interest Rate is 6% per annum", font=("calibri",12)).grid(row=3,sticky=W)

    #Button
    Button(fd_screen, text="I Agree", font=("Calibri",12), command=fd2).grid(row=5,pady=10,sticky=N)


    
def loan():
    print("Loan")

def login_session():
    global login_name
    all_accounts=os.listdir()
    login_name =temp_login_name.get()
    login_password =temp_login_password.get()
    login_account =temp_login_account.get()

    for name in all_accounts:
        if name==login_name:
            file = open(name,"r")
            file_data =file.read()
            file_data = file_data.split("\n")
            password =file_data[5]
            account =file_data[6]

            #Account Dashboard
            if login_password == password and login_account == account:
                login_screen.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.title("Dashboard")

                #Label
                Label(account_dashboard, text ="Account Dashboard", font=("calibri",12)).grid(row=0,pady=10,sticky=N)
                Label(account_dashboard, text ="WELCOME "+name, font=("calibri",14)).grid(row=1,pady=5,sticky=N)

                #Button
                Button(account_dashboard, text ="Personal Details", font=("calibri",12),width=30,command=personal_details).grid(row=3,padx=10,sticky=N)
                Button(account_dashboard, text ="Deposits", font=("calibri",12),width=30,command=deposits).grid(row=4,padx=10,sticky=N)
                Button(account_dashboard, text ="Withdrawl", font=("calibri",12),width=30,command=withdraw).grid(row=5,padx=10,sticky=N)
                Button(account_dashboard, text ="Fixed Deposit", font=("calibri",12),width=30,command=fd ).grid(row=6,padx=10,sticky=N)
                Button(account_dashboard, text ="Loan", font=("calibri",12),width=30,command=loan ).grid(row=7,padx=10,sticky=N)
                Label(account_dashboard).grid(row=9,padx=10,sticky=N)
                return
            else:
                login_notif.config(fg="red", text = "Incorrect Details !!")
                return
        login_notif.config(fg="red", text = "No Account Found !!")


def deposits():
    
    #Variable define
    global amount
    global deposit_notif
    global current_balance_label
    amount = StringVar()
    
    file = open(login_name,"r")
    file_data = file.read()
    user_details = file_data.split("\n")
    details_balance = user_details[4]

    #Deposit_screen
    deposit_screen = Toplevel(master)
    deposit_screen.title("Deposit")

    #Label
    Label(deposit_screen, text="Deposit", font=("Calibri",12)).grid(row=0,sticky=N,pady=10)
    current_balance_label= Label(deposit_screen,text="Balance : Rs." + details_balance,font=("calibri",12))
    current_balance_label.grid(row=1,sticky=W)
    Label(deposit_screen, text="Amount :  ", font=("Calibri",12)).grid(row=2,sticky=W,padx=5)
    deposit_notif = Label(deposit_screen,font=("calibri",12))
    deposit_notif.grid(row=4,sticky=N,pady=5)

    #Entry
    Entry(deposit_screen, textvariable=amount).grid(row=3,column=0)

    #Button
    Button(deposit_screen, text="Finish", font=("Calibri",12), command=finish_deposit, width=20).grid(row=5,sticky=W,pady=5)
    
def withdraw():
    #Variable define
    global withdraw_amount
    global withdraw_notif
    global current_balance_label
    withdraw_amount = StringVar()
    
    file = open(login_name,"r")
    file_data = file.read()
    user_details = file_data.split("\n")
    details_balance = user_details[4]

    #withdraw_screen
    withdraw_screen = Toplevel(master)
    withdraw_screen.title("withdraw")

    #Label
    Label(withdraw_screen, text="withdraw", font=("Calibri",12)).grid(row=0,sticky=N,pady=10)
    current_balance_label= Label(withdraw_screen,text="Balance : Rs." + details_balance,font=("calibri",12))
    current_balance_label.grid(row=1,sticky=W)
    Label(withdraw_screen, text="Amount :  ", font=("Calibri",12)).grid(row=2,sticky=W,padx=5)
    withdraw_notif = Label(withdraw_screen,font=("calibri",12))
    withdraw_notif.grid(row=4,sticky=N,pady=5)

    #Entry
    Entry(withdraw_screen, textvariable=withdraw_amount).grid(row=3,column=0)

    #Button
    Button(withdraw_screen, text="Finish", font=("Calibri",12), command=finish_withdraw, width=20).grid(row=5,sticky=W,pady=5)

def personal_details():
    file = open(login_name,"r")
    file_data = file.read()
    user_details = file_data.split("\n")
    
    details_name = user_details[0]
    details_age = user_details[1]
    details_gender = user_details[2]
    details_Phone = user_details[3]
    details_balance = user_details[4]
    details_account = user_details[6]

    #details_account = random_acc

    #Personal Details screen
    personal_details_screen = Toplevel(master)
    personal_details_screen.title("Personal Details")

    #Label
    Label(personal_details_screen, text ="Personal Details", font=("calibri",12),width=15).grid(row=0,pady=10,sticky=N)
    Label(personal_details_screen, text ="Name :" + details_name, font=("calibri",12)).grid(row=2,pady=10,sticky=N)
    Label(personal_details_screen, text ="Age :" + details_age, font=("calibri",12)).grid(row=3,pady=10,sticky=N)
    Label(personal_details_screen, text ="Gender :" + details_gender, font=("calibri",12)).grid(row=4,pady=10,sticky=N)
    Label(personal_details_screen, text ="Phone :" + details_Phone, font=("calibri",12)).grid(row=5,pady=10,sticky=N)
    Label(personal_details_screen, text ="Account No. : " + details_account, font=("calibri",12)).grid(row=6,pady=10,sticky=N)
    Label(personal_details_screen,fg="blue", text ="Balance: Rs. " + details_balance, font=("calibri",12)).grid(row=7,pady=10,sticky=N)

    
    


    
def login():

    #Variable define
    global temp_login_name
    global login_screen
    global temp_login_password
    global temp_login_account
    global login_notif

    temp_login_name =StringVar()
    temp_login_password =StringVar()
    temp_login_account = StringVar()
    
    #Login screen
    login_screen = Toplevel(master)
    login_screen.title("Login")

    #Label
    Label(login_screen, text = "Login to your account",font=("calibri",12)).grid(row=0,pady=10,sticky=N)
    Label(login_screen, text = "Username",font=("calibri",12)).grid(row=1,sticky=W)
    #Label(login_screen, text = "Phone No.",font=("calibri",12)).grid(row=2,sticky=W)
    Label(login_screen, text = "Account No.",font=("calibri",12)).grid(row=2,sticky=W)
    Label(login_screen, text = "Password",font=("calibri",12)).grid(row=3,sticky=W)
    login_notif = Label (login_screen, font =("calibri",12))
    login_notif.grid(row=4,sticky=N)

    #Entry
    Entry(login_screen, textvariable=temp_login_name).grid(row=1,column=1,padx=5)
    Entry(login_screen, textvariable=temp_login_account).grid(row=2,column=1,padx=5)
    Entry(login_screen, textvariable=temp_login_password,show="*").grid(row=3,column=1,padx=5)

    #Buttons
    Button(login_screen, text="Login", command= login_session,width=15,font=("Calibri",12)).grid(row=5,sticky=W,pady=5,padx=5)
    
#image
img=Image.open("banklogo2.png")
img=img.resize((150,150))
img= ImageTk.PhotoImage(img)

#label
Label(master, text="Bank of Varanasi 'BOV' ", font=("calibri",18)).grid(row=0,pady=12,sticky=N)
Label(master, text="It's Most secure Bank Ever", font=("calibri",14)).grid(row=1,sticky=N)
Label(master, image=img).grid(row=2,sticky=N,pady=15)

#Buttons
Button(master, text="Registration", font =("calibri",12),width=20, command= register).grid(row=3,sticky=N)
Button(master, text="Login", font =("calibri",12),width=20, command= login).grid(row=4,pady=10,sticky=N)


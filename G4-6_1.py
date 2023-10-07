from tkinter import *
from tkinter.messagebox import showinfo
from datetime import datetime
from abc import ABCMeta, abstractmethod
import random

color = '#ffffff'     #to customize the windows
current = ""          #contains the logged in account

class InvalidWithdraw(Exception): # user-defined exception class inheriting from Exception class 
    pass

class Administrator:
    all_accounts = []

    @classmethod
    def search_account(cls,a,b): #this method will be used to search the existing accounts
        for i in cls.all_accounts:
            if i.account.account_no == a and i.account.password == b:
                return i

class Account(metaclass=ABCMeta):       #abstract class
    def __init__(self, acc, password, date, bal=0, strg = ''):
        self.account_no = acc
        self.password = password
        self.balance = bal
        self.string = strg
        self.date = date

    def withdraw(self):   #making a window here as this window won't be linked to any other widow 
        def func():
            amount = withdraw_entry.get()

            try:   
                if int(amount) > self.balance:
                    withdraw_entry.delete(0,END)
                    raise InvalidWithdraw
            except InvalidWithdraw:
                showinfo(message='Insufficient Balance')
                return

            if not(amount.isdigit()):
                showinfo(message='Invalid Entry')
                withdraw_entry.delete(0,END)
                
            else:
                self.balance -= int(amount)
                showinfo(message=f'{amount} has been withdrawn from the account \nBalance: {self.balance}')
                self.string += getdate()+' ! '+amount+' has been withdrawn from the account !Balance: '+str(self.balance)+'.!'
                withdraw_win.destroy()

        existing_win.destroy()  
        withdraw_win = Tk()
        withdraw_win.geometry("640x480+180+80")
        withdraw_win.title("Savings Account")
        withdraw_win.configure(background=color)
        withdraw_win.resizable(False,False)

        main = Label(withdraw_win, text="Withdraw", font=("Comic Sans MS", 25,'bold'), fg=color, bg='#8dc43e', pady=30,padx = 340)
        main.pack()

        back_button = Button(withdraw_win, text="<", font=('Arial Rounded MT Bold', 12,'bold'),bg=color, relief="raised", bd=1, command=withdraw_win.destroy)
        back_button.place(x=30,y=37)

        if color=='#ffffff':
            other_color = '#000000'
            back_button.config(fg=other_color)

        else:
            other_color = '#ffffff'
            back_button.config(fg=other_color)
            
        withdraw_lab = Label(withdraw_win,text="Enter the amount to Withdraw",font=("Arial",20,'bold'),fg=other_color,bg=color)
        withdraw_lab.place(x=80,y=190)

        withdraw_entry = Entry(withdraw_win, width=30,font=("Arial",18,'bold'),cursor=f'xterm {color}',fg=color,bg=other_color)
        withdraw_entry.place(x=80,y=240)

        back2 = Button(withdraw_win,text="Done",font=('Arial',15,'bold'),fg=color,bg="#8dc43e",relief="raised",bd=12,command=func)
        back2.place(x=280,y=360)

        withdraw_win.mainloop()

    def deposit(self):         #making a window here as this window won't be linked to any other widow
        def func():
            amount = deposits_entry.get()
            if not(amount.isdigit()):
                showinfo(message='Invalid Entry')
                deposits_entry.delete(0,END)
                
            else:
                self.balance += int(amount)
                showinfo(message=f'{amount} has been deposited to the account \nBalance: {self.balance}')
                self.string += getdate()+' ! '+amount+' has been deposited to the account !Balance: '+str(self.balance)+'.!'
                deposit_win.destroy()

        existing_win.destroy()  
        deposit_win = Tk()
        deposit_win.geometry("640x480+180+80")
        deposit_win.title("Deposit")
        deposit_win.configure(background=color)
        deposit_win.resizable(0,0)

        main = Label(deposit_win, text="Deposit", font=("Comic Sans MS", 25,'bold'), fg=color, bg='#8dc43e', pady=30,padx = 340)
        main.pack()

        back_button = Button(deposit_win, text="<", font=('Arial Rounded MT Bold', 12,'bold'),bg=color, relief="raised", bd=1, command=deposit_win.destroy)
        back_button.place(x=30,y=37)

        if color=='#ffffff':
            other_color = '#000000'
            back_button.config(fg=other_color)

        else:
            other_color = '#ffffff'
            back_button.config(fg=other_color)
            
        deposits_lab = Label(deposit_win,text="Enter the amount to Deposit",font=("Arial",20,'bold'),fg=other_color,bg=color)
        deposits_lab.place(x=80,y=190)

        deposits_entry = Entry(deposit_win, width=30,font=("Arial",18,'bold'),cursor=f'xterm {color}',fg=color,bg=other_color)
        deposits_entry.place(x=80,y=240)

        back2 = Button(deposit_win,text="Done",font=('Arial',15,'bold'),fg=color,bg="#8dc43e",relief="raised",bd=12,command=func)
        back2.place(x=280,y=360)

        deposit_win.mainloop()

    @abstractmethod
    def report(self):
        pass


class Saving_account(Account):
    def __init__(self, acc, password, date, bal=0, strg=''):
        super().__init__(acc, password, date, bal, strg)
        self.interestRate = self.balance * 0.05

    def monthlyInterest(self,d): 

        temp = self.date.split('-')
        temp = int(temp[1])

        temp2 = d.split('-')
        temp2 = int(temp2[1])

        if temp < temp2: #checking if the month has passed to credit the interest rate
            self.balance += round(self.interestRate)
            self.string += d+' !Interest rate has been credited to the account ! Balance: '+str(self.balance)+'.!'
            self.date = d  #assigning the current date to the attribute date

    def report(self): #implementing the abstract method
        def next_list():
            global n
            n += 1
            if n < length:
                content = strg[n].strip('!')
                content =content.split('!')
                lab12.config(text=content[0])
                lab13.config(text=content[1])
                lab14.config(text=content[2])

            if n+1 >= length :
                next_button.destroy()

        existing_win.destroy()
        report = Tk()
        report.geometry("852x480+180+80")
        report.title("Statement")
        report.configure(background=color)
        report.resizable (0,0)

        main = Label(report, text="Statement", font=("Comic Sans MS", 25,'bold'), fg=color, bg='#8dc43e', pady=30,padx = 380)
        main.pack()

        back_button = Button(report, text="<", font=('Arial Rounded MT Bold', 12,'bold'), relief="raised", bd=1, command=report.destroy)
        back_button.place(x=30,y=37)

        if color == '#ffffff': #checking which mode is currently on and customizing the window accordingly
            back_button.config(fg='#000000', bg=color)
            other_color = '#000000'
            
        else:
            back_button.config(fg='#ffffff', bg=color)
            other_color = '#ffffff'

        next_button = Button(report, text="Next", font=("Arial", 16, 'bold'), fg=color, bg="#8dc43e", relief="raised", bd=8,command=next_list)
        next_button.place(x=395, y=390)

        lab1 = Label(report,text='First Name:',font=('Arial', 14,'bold'),fg='#8dc43e', bg=color)
        lab1.place(x=50, y=120)

        lab2 = Label(report,text=first_name,font=('Arial', 14,'bold'),fg=other_color, bg=color)
        lab2.place(x=250, y=120)

        lab3 = Label(report,text='Last Name:',font=('Arial', 14,'bold'),fg='#8dc43e', bg=color)
        lab3.place(x=470, y=120)

        lab4 = Label(report,text=last_name,font=('Arial', 14,'bold'),fg=other_color, bg=color)
        lab4.place(x=640, y=120)

        lab5 = Label(report,text='Account Number:',font=('Arial', 14,'bold'),fg='#8dc43e', bg=color)
        lab5.place(x=50, y=160)

        lab6 = Label(report,text=self.account_no,font=('Arial', 14,'bold'),fg=other_color, bg=color)
        lab6.place(x=250, y=160)

        lab7 = Label(report,text='Account Title:',font=('Arial', 16,'bold'),fg='#8dc43e', bg=color)
        lab7.place(x=470, y=160)

        lab8 = Label(report,text='Savings Account',font=('Arial', 16,'bold'),fg=other_color, bg=color)
        lab8.place(x=640, y=160)

        lab9 = Label(report,text='Balance:',font=('Arial', 16,'bold'),fg='#8dc43e', bg=color)
        lab9.place(x=50, y=200)

        lab9 = Label(report,text='5000',font=('Arial', 16,'bold'),fg=other_color, bg=color)
        lab9.place(x=250, y=200)

        lab10 = Label(report,text='Interest Rate:',font=('Arial', 16,'bold'),fg='#8dc43e', bg=color)
        lab10.place(x=470, y=200)

        lab11 = Label(report,text='5%',font=('Arial', 16,'bold'),fg=other_color, bg=color)
        lab11.place(x=640, y=200)

        strg = self.string.split('.')
        strg.pop()
        length = len(strg)

        global n
        n = 0
        content = strg[n].strip('!')
        content =content.split('!')

        if n+1 < length:
            lab12 = Label(report,text=content[0],font=('Arial', 16,'bold'),fg=other_color, bg=color)
            lab12.place(x=70, y=265)

            lab13 = Label(report,text=content[1],font=('Arial', 16,'bold'),fg=other_color, bg=color)
            lab13.place(x=70, y=315)

            lab14 = Label(report,text=content[2],font=('Arial', 16,'bold'),fg=other_color, bg=color)
            lab14.place(x=70, y=365)

        else:
            next_button.destroy()

        report.mainloop()
        
class Checking_account(Account):
    def __init__(self,acc, password, date, bal=0, strg=''):
        super().__init__(acc, password, date, bal, strg)
        self.overdraft_fee = 500
        self.credit_limit = -50000

    def withdraw(self):    #overriding the withdraw method of super class
        def func():
            amount = withdraw_entry.get()
            if not(amount.isdigit()):
                showinfo(message='Invalid Entry')
                withdraw_entry.delete(0,END)
               
            elif (self.balance - int(amount)) <= self.credit_limit:
                showinfo(message='Credit Limit had been reached')
                withdraw_entry.delete(0,END)
                
            else:
                if self.balance < int(amount):
                    self.balance -= self.overdraft_fee
                    
                self.balance -= int(amount)
                showinfo(message=f'{amount} has been withdrawn from the account \nBalance: {self.balance}')
                self.string += getdate()+' ! '+amount+' has been withdrawn from the account !Balance: '+str(self.balance)+'.!'
                withdraw_win.destroy()

        existing_win.destroy()  
        withdraw_win = Tk()
        withdraw_win.geometry("640x480+180+80")
        withdraw_win.title("Savings Account")
        withdraw_win.configure(background=color)
        withdraw_win.resizable(0,0)

        main = Label(withdraw_win, text="Withdraw", font=("Comic Sans MS", 25,'bold'), fg=color, bg='#8dc43e', pady=30,padx = 340)
        main.pack()

        back_button = Button(withdraw_win, text="<", font=('Arial Rounded MT Bold', 12,'bold'),bg=color, relief="raised", bd=1, command=withdraw_win.destroy)
        back_button.place(x=30,y=37)

        if color=='#ffffff':
            other_color = '#000000'
            back_button.config(fg=other_color)

        else:
            other_color = '#ffffff'
            back_button.config(fg=other_color)
            
        withdraw_lab = Label(withdraw_win,text="Enter the amount to Withdraw",font=("Arial",20,'bold'),fg=other_color,bg=color)
        withdraw_lab.place(x=80,y=190)

        withdraw_entry = Entry(withdraw_win, width=30,font=("Arial",18,'bold'),cursor=f'xterm {color}',fg=color,bg=other_color)
        withdraw_entry.place(x=80,y=240)

        back2 = Button(withdraw_win,text="Done",font=('Arial',15,'bold'),fg=color,bg="#8dc43e",relief="raised",bd=12,command=func)
        back2.place(x=280,y=360)

        withdraw_win.mainloop()

    def report(self): #implementing the abstract method

        def next_list():
            global n
            n += 1
            if n < length:
                content = strg[n].strip('!')
                content =content.split('!')
                lab14.config(text=content[0])
                lab15.config(text=content[1])
                lab16.config(text=content[2])

            if n+1 >= length :
                next_button.destroy()

        existing_win.destroy()
        report = Tk()
        report.geometry("852x480+180+80")
        report.title("Statement")
        report.configure(background=color)
        report.resizable (0,0)

        main = Label(report, text="Statement", font=("Comic Sans MS", 25,'bold'), fg=color, bg='#8dc43e', pady=25,padx = 380)
        main.pack()

        back_button = Button(report, text="<", font=('Arial Rounded MT Bold', 12,'bold'), relief="raised", bd=1, command=report.destroy)
        back_button.place(x=30,y=37)

        if color == '#ffffff': #checking which mode is currently on and customizing the window accordingly
            back_button.config(fg='#000000', bg=color)
            other_color = '#000000'
            
        else:
            back_button.config(fg='#ffffff', bg=color)
            other_color = '#ffffff'

        next_button = Button(report, text="Next", font=("Arial", 16, 'bold'), fg=color, bg="#8dc43e", relief="raised", bd=8,command=next_list)
        next_button.place(x=395, y=410)

        lab1 = Label(report,text='First Name:',font=('Arial', 14,'bold'),fg='#8dc43e', bg=color)
        lab1.place(x=50, y=110)

        lab2 = Label(report,text=first_name,font=('Arial', 14,'bold'),fg=other_color, bg=color)
        lab2.place(x=250, y=110)

        lab3 = Label(report,text='Last Name:',font=('Arial', 14,'bold'),fg='#8dc43e', bg=color)
        lab3.place(x=470, y=110)

        lab4 = Label(report,text=last_name,font=('Arial', 14,'bold'),fg=other_color, bg=color)
        lab4.place(x=640, y=110)

        lab5 = Label(report,text='Account Number:',font=('Arial', 14,'bold'),fg='#8dc43e', bg=color)
        lab5.place(x=50, y=150)

        lab6 = Label(report,text=self.account_no,font=('Arial', 14,'bold'),fg=other_color, bg=color)
        lab6.place(x=250, y=150)

        lab7 = Label(report,text='Account Title:',font=('Arial', 16,'bold'),fg='#8dc43e', bg=color)
        lab7.place(x=470, y=150)

        lab8 = Label(report,text='Checking Account',font=('Arial', 16,'bold'),fg=other_color, bg=color)
        lab8.place(x=640, y=150)

        lab9 = Label(report,text='Credit Limit:',font=('Arial', 16,'bold'),fg='#8dc43e', bg=color)
        lab9.place(x=50, y=190)

        lab9 = Label(report,text=self.credit_limit,font=('Arial', 16,'bold'),fg=other_color, bg=color)
        lab9.place(x=250, y=190)

        lab10 = Label(report,text='Overdraft Fee:',font=('Arial', 16,'bold'),fg='#8dc43e', bg=color)
        lab10.place(x=470, y=190)

        lab11 = Label(report,text=self.overdraft_fee,font=('Arial', 16,'bold'),fg=other_color, bg=color)
        lab11.place(x=640, y=190)

        lab12 = Label(report,text='Balance:',font=('Arial', 16,'bold'),fg='#8dc43e', bg=color)
        lab12.place(x=50, y=230)

        lab13 = Label(report,text=self.balance,font=('Arial', 16,'bold'),fg=other_color, bg=color)
        lab13.place(x=250, y=230)
        
        strg = self.string.split('.')
        strg.pop()
        length = len(strg)

        global n
        n = 0
        content = strg[n].strip('!')
        content =content.split('!')

        if n+1 < length:
            lab14 = Label(report,text=content[0],font=('Arial', 16,'bold'),fg=other_color, bg=color)
            lab14.place(x=70, y=275)

            lab15 = Label(report,text=content[1],font=('Arial', 16,'bold'),fg=other_color, bg=color)
            lab15.place(x=70, y=325)

            lab16 = Label(report,text=content[2],font=('Arial', 16,'bold'),fg=other_color, bg=color)
            lab16.place(x=70, y=375)

        else:
            next_button.destroy()

        report.mainloop()


class Loan_account(Account):
    def __init__(self, p_amount, loan_duration, acc, password, date , bal=0, strg=''):
        super().__init__(acc, password, date, bal, strg)
        self.principleAmount = p_amount
        self.interestRate = self.principleAmount * 0.02
        self.loanDuration = loan_duration

    def monthlyDebt(self,d): #checking if the month has passed to debit the monthly loan pay
        if self.loanDuration == 0:
            return
        
        temp = self.date.split('-')
        temp = int(temp[1])

        temp2 = d.split('-')
        temp2 = int(temp2[1])

        if temp < temp2:
            self.balance -= (round((self.principleAmount/self.loanDuration) + self.interestRate))
            self.loanDuration -= 1
            self.string += d+' ! Monthly debt has been debited from the account ! Balance:'+str(self.balance)+'.!'
            self.date = d
    
    def report(self): #implementing the abstract method

        def next_list():
            global n
            n += 1
            if n < length:
                content = strg[n].strip('!')
                content =content.split('!')
                lab14.config(text=content[0])
                lab15.config(text=content[1])
                lab16.config(text=content[2])

            if n+1 >= length :
                next_button.destroy()

        existing_win.destroy()
        report = Tk()
        report.geometry("852x480+180+80")
        report.title("Statement")
        report.configure(background=color)
        report.resizable (0,0)

        main = Label(report, text="Statement", font=("Comic Sans MS", 25,'bold'), fg=color, bg='#8dc43e', pady=25,padx = 380)
        main.pack()

        back_button = Button(report, text="<", font=('Arial Rounded MT Bold', 12,'bold'), relief="raised", bd=1, command=report.destroy)
        back_button.place(x=30,y=37)

        if color == '#ffffff': #checking which mode is currently on and customizing the window accordingly
            back_button.config(fg='#000000', bg=color)
            other_color = '#000000'
            
        else:
            back_button.config(fg='#ffffff', bg=color)
            other_color = '#ffffff'

        next_button = Button(report, text="Next", font=("Arial", 16, 'bold'), fg=color, bg="#8dc43e", relief="raised", bd=8,command=next_list)
        next_button.place(x=395, y=410)

        lab1 = Label(report,text='First Name:',font=('Arial', 14,'bold'),fg='#8dc43e', bg=color)
        lab1.place(x=50, y=110)

        lab2 = Label(report,text=first_name,font=('Arial', 14,'bold'),fg=other_color, bg=color)
        lab2.place(x=250, y=110)

        lab3 = Label(report,text='Last Name:',font=('Arial', 14,'bold'),fg='#8dc43e', bg=color)
        lab3.place(x=470, y=110)

        lab4 = Label(report,text=last_name,font=('Arial', 14,'bold'),fg=other_color, bg=color)
        lab4.place(x=640, y=110)

        lab5 = Label(report,text='Account Number:',font=('Arial', 14,'bold'),fg='#8dc43e', bg=color)
        lab5.place(x=50, y=150)

        lab6 = Label(report,text=self.account_no,font=('Arial', 14,'bold'),fg=other_color, bg=color)
        lab6.place(x=250, y=150)

        lab7 = Label(report,text='Account Title:',font=('Arial', 16,'bold'),fg='#8dc43e', bg=color)
        lab7.place(x=470, y=150)

        lab8 = Label(report,text='Loan Account',font=('Arial', 16,'bold'),fg=other_color, bg=color)
        lab8.place(x=640, y=150)

        lab9 = Label(report,text='Loan Amount:',font=('Arial', 16,'bold'),fg='#8dc43e', bg=color)
        lab9.place(x=50, y=190)

        lab9 = Label(report,text=self.principleAmount,font=('Arial', 16,'bold'),fg=other_color, bg=color)
        lab9.place(x=250, y=190)

        lab10 = Label(report,text='Loan Duration:',font=('Arial', 16,'bold'),fg='#8dc43e', bg=color)
        lab10.place(x=470, y=190)

        lab11 = Label(report,text=f'{self.loanDuration} months remain',font=('Arial', 16,'bold'),fg=other_color, bg=color)
        lab11.place(x=640, y=190)

        lab12 = Label(report,text='Interest Rate: ',font=('Arial', 16,'bold'),fg='#8dc43e', bg=color)
        lab12.place(x=50, y=230)

        lab13 = Label(report,text='2%',font=('Arial', 16,'bold'),fg=other_color, bg=color)
        lab13.place(x=250, y=230)

        lab14 = Label(report,text='Balance: ',font=('Arial', 16,'bold'),fg='#8dc43e', bg=color)
        lab14.place(x=470, y=230)

        lab15 = Label(report,text=self.balance,font=('Arial', 16,'bold'),fg=other_color, bg=color)
        lab15.place(x=640, y=230)
        
        strg = self.string.split('.')
        strg.pop()
        length = len(strg)

        global n
        n = 0
        content = strg[n].strip('!')
        content =content.split('!')

        if n+1 < length:
            lab14 = Label(report,text=content[0],font=('Arial', 16,'bold'),fg=other_color, bg=color)
            lab14.place(x=70, y=275)

            lab15 = Label(report,text=content[1],font=('Arial', 16,'bold'),fg=other_color, bg=color)
            lab15.place(x=70, y=325)

            lab16 = Label(report,text=content[2],font=('Arial', 16,'bold'),fg=other_color, bg=color)
            lab16.place(x=70, y=375)

        else:
            next_button.destroy()

        report.mainloop()


class Customer:
    acc = []

    def __init__(self, fname, lname, address, account_no, password, date, bal, strg, types, a=None, b=None):
        self.fname = fname
        self.lname = lname
        self.address = address

        if types == '1': #creating the instance of saving, checking and loan account by identifying the type
            self.account = Saving_account(account_no, password, date, bal,strg)
            
        elif types == '2':
            self.account = Checking_account(account_no, password, date, bal, strg)

        elif types == '3':
            self.account = Loan_account(a , b, account_no, password, date, bal,strg)


#-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
            
def getdate():     #this will give the curent date
    current = str(datetime.now())
    current = current.split()
    i = current[0]
    i = i.split('-')
    date = i[2]+'-'+i[1]+'-'+i[0]
    return date


def create_account():
    def savings(): #to create savings account
        new_acc.destroy()
        
        def detail():
            r = Tk()
            r.geometry("400x400")
            r.title("Details")
            r.configure(background=color)
            r.wm_attributes("-topmost",True)

            if color=='#ffffff':
                other_color = '#000000'
    
            else:
                other_color = '#ffffff'
                
            main = Label(r, text="Savings Account", font=("Comic Sans MS", 20,'bold'), fg=color, bg='#8dc43e', pady=30,padx=100)
            main.pack(anchor='center')

            instruct = Label(r, text="Instructions:", font=("Arial", 15,'bold'), fg='#8dc43e', bg=color, padx=10,pady=10)
            instruct.pack(anchor='w')
            
            lab1 = Label(r, text="To create the Savings Account minimum deposit", font=("Arial", 13,'bold'), fg=other_color, bg=color, padx=10,pady=10)
            lab1.pack(anchor='w')

            lab2 = Label(r, text=" of 10000 is required.", font=("Arial", 13,'bold'), fg=other_color, bg=color, padx=10,pady=10)
            lab2.pack(anchor='w')

            lab3 = Label(r, text="The interest Rate is 5% which will be deposited", font=("Arial", 13,'bold'), fg=other_color, bg=color,padx=10,pady=10)
            lab3.pack(anchor='w')

            lab3 = Label(r, text=" to the Account Balance every month.", font=("Arial", 13,'bold'), fg=other_color, bg=color, padx=10, pady=10)
            lab3.pack(anchor='w')
            
            button = Button(r, text="Ok", font=('Arial Rounded MT Bold', 13), fg=color, bg='#8dc43e', relief="raised", bd=7, command=r.destroy)
            button.pack(anchor='center')

            r.mainloop()
            
        detail()
        def func():
            deposit = deposit_entry.get()
            if not(deposit.isdigit()):
                showinfo(message='Invalid Entry')
                deposit_entry.delete(0,END)
                
            elif int(deposit) < 10000:
                showinfo(message='Deposited Amount should be greater than 10000')
                deposit_entry.delete(0,END)
                
            elif int(deposit) > 10000:
                deposit_entry.delete(0,END)
                account_no = ''                 #generating the account number
                account_no += str(random.randint(10,99))+'-'
                account_no += str(random.randint(100,999))+'-'
                account_no += str(random.randint(100000,999999))
                date = getdate()
                strg = getdate() + '!'+'Account Created !Balance: '+ deposit
                password = str(random.randint(1000,9999))                       #generating the password
                temp = Customer(fname, lname, address, account_no, password, date, int(deposit), strg, '1')
                Administrator.all_accounts.append(temp)
                savings_win.destroy()

                def reveal(): #to reveal password
                    global is_true
                    if  is_true:
                        pass_lab.config(text=f'Password:\t{password}')
                        is_true = False
                    elif not(is_true):
                        pass_lab.config(text=f'Password:\tXXXX')
                        is_true = True
                        
                congrats = Tk()
                congrats.geometry("640x480+180+80")
                congrats.title("Savings Account")
                congrats.configure(background=color)
                congrats.resizable(False,False)

                main = Label(congrats, text="Congratulations", font=("Comic Sans MS", 25,'bold'), fg=color, bg='#8dc43e', pady=30,padx = 340)
                main.pack()

                back_button = Button(congrats, text="<", font=('Arial Rounded MT Bold', 12,'bold'),bg=color, relief="raised", bd=1, command=congrats.destroy)
                back_button.place(x=30,y=37)


                if color=='#ffffff':
                    other_color = '#000000'
                    back_button.config(fg=other_color)

                else:
                    other_color = '#ffffff'
                    back_button.config(fg=other_color)
                    
                acccreate_lab= Label(congrats,text="Your Account has been created",font=("Arial",18,'bold'),fg='#8dc43e',bg=color,padx=40,pady=15)
                acccreate_lab.pack(anchor='w')

                accno_lab= Label(congrats,text=f"Account No. :\t{account_no}",font=("Arial",16,'bold'),fg=other_color,bg=color,padx=40,pady=15)
                accno_lab.pack(anchor='w')

                pass_lab= Label(congrats,text=f"Password :\tXXXX",font=("Arial",16,'bold'),fg=other_color,bg=color,padx=40,pady=15)
                pass_lab.pack(anchor='w')

                global is_true
                is_true = True
                
                reveal = Button(congrats,text="Reveal Password",font=('Arial',10,'bold'),fg=color,bg="#8dc43e",relief="raised",bd=12,command=reveal)
                reveal.pack(pady=10)

                mainmenu = Button(congrats,text="Main Menu",font=('Arial',12,'bold'),fg=color,bg="#8dc43e",relief="raised",bd=12,command=congrats.destroy)
                mainmenu.pack(pady=10)

                congrats.mainloop()

                
        savings_win = Tk()
        savings_win.geometry("640x480+180+80")
        savings_win.title("Savings Account")
        savings_win.configure(background=color)
        savings_win.resizable(0,0)

        main = Label(savings_win, text="Savings Account", font=("Comic Sans MS", 25,'bold'), fg=color, bg='#8dc43e', pady=30,padx = 340)
        main.pack()

        back_button = Button(savings_win, text="<", font=('Arial Rounded MT Bold', 12,'bold'),bg=color, relief="raised", bd=1, command=savings_win.destroy)
        back_button.place(x=30,y=37)

        if color=='#ffffff':
            other_color = '#000000'
            back_button.config(fg=other_color)

        else:
            other_color = '#ffffff'
            back_button.config(fg=other_color)
            
        deposit_lab = Label(savings_win,text="Enter the amount to Deposit:",font=("Arial",20,'bold'),fg=other_color,bg=color)
        deposit_lab.place(x=80,y=190)

        deposit_entry = Entry(savings_win, width=30,font=("Arial",18,'bold'),cursor=f'xterm {color}',fg=color,bg=other_color)
        deposit_entry.place(x=80,y=240)

        back2 = Button(savings_win,text="Done",font=('Arial',15,'bold'),fg=color,bg="#8dc43e",relief="raised",bd=12,command=func)
        back2.place(x=280,y=360)

        savings_win.mainloop()
        
    def checking(): #to create checking account
        new_acc.destroy()
        def detail():
            r = Tk()
            r.geometry("400x400")
            r.title("Details")
            r.configure(background=color)
            r.wm_attributes("-topmost",True)

            if color=='#ffffff':
                other_color = '#000000'
    
            else:
                other_color = '#ffffff'
                
            main = Label(r, text="Checking Account", font=("Comic Sans MS", 20,'bold'), fg=color, bg='#8dc43e', pady=30,padx=100)
            main.pack(anchor='center')

            instruct = Label(r, text="Instructions:", font=("Arial", 15,'bold'), fg='#8dc43e', bg=color, padx=10,pady=10)
            instruct.pack(anchor='w')
            
            lab1 = Label(r, text="You can overdraft while withdrawing upto the", font=("Arial", 13,'bold'), fg=other_color, bg=color, padx=10,pady=10)
            lab1.pack(anchor='w')

            lab2 = Label(r, text="credit limit which is 50000.", font=("Arial", 13,'bold'), fg=other_color, bg=color, padx=10,pady=10)
            lab2.pack(anchor='w')

            lab3 = Label(r, text="The overdraft fee is 500 per withdraw which will", font=("Arial", 13,'bold'), fg=other_color, bg=color,padx=10,pady=10)
            lab3.pack(anchor='w')

            lab3 = Label(r, text="be debited from Account Balance.", font=("Arial", 13,'bold'), fg=other_color, bg=color, padx=10, pady=10)
            lab3.pack(anchor='w')
            
            button = Button(r, text="Ok", font=('Arial Rounded MT Bold', 13), fg=color, bg='#8dc43e', relief="raised", bd=7, command=r.destroy)
            button.pack(anchor='center')

            r.mainloop()
            
        detail()
        def func():
            deposit = deposit_entry.get()
            if not(deposit.isdigit()) or int(deposit) == 0:
                showinfo(message='Invalid Entry')
                deposit_entry.delete(0,END)               
  
            else:
                deposit_entry.delete(0,END)
                account_no = ''             #generating the account number
                account_no += str(random.randint(10,99))+'-'
                account_no += str(random.randint(100,999))+'-'
                account_no += str(random.randint(100000,999999))
                date = getdate()
                strg = getdate() + '!'+'Account Created !Balance: '+deposit
                password = str(random.randint(1000,9999))      # generating the password
                temp = Customer(fname, lname, address, account_no, password, date, int(deposit), strg, '2')
                Administrator.all_accounts.append(temp) 
                checking_win.destroy()
                
                def reveal(): #to reveal password
                    global is_true
                    if  is_true:
                        pass_lab.config(text=f'Password:\t{password}')
                        is_true = False
                    elif not(is_true):
                        pass_lab.config(text=f'Password:\tXXXX')
                        is_true = True
                        
                congrats = Tk()
                congrats.geometry("640x480+180+80")
                congrats.title("Checking Account")
                congrats.configure(background=color)
                congrats.resizable(0,0)

                main = Label(congrats, text="Congratulations", font=("Comic Sans MS", 25,'bold'), fg=color, bg='#8dc43e', pady=30,padx = 340)
                main.pack()

                back_button = Button(congrats, text="<", font=('Arial Rounded MT Bold', 12,'bold'),bg=color, relief="raised", bd=1, command=congrats.destroy)
                back_button.place(x=30,y=37)


                if color=='#ffffff':
                    other_color = '#000000'
                    back_button.config(fg=other_color)

                else:
                    other_color = '#ffffff'
                    back_button.config(fg=other_color)
                    
                acccreate_lab= Label(congrats,text="Your Account has been created",font=("Arial",18,'bold'),fg='#8dc43e',bg=color,padx=40,pady=15)
                acccreate_lab.pack(anchor='w')

                accno_lab= Label(congrats,text=f"Account No. :\t{account_no}",font=("Arial",16,'bold'),fg=other_color,bg=color,padx=40,pady=15)
                accno_lab.pack(anchor='w')

                pass_lab= Label(congrats,text=f"Password :\tXXXX",font=("Arial",16,'bold'),fg=other_color,bg=color,padx=40,pady=15)
                pass_lab.pack(anchor='w')

                global is_true
                is_true = True
                
                reveal = Button(congrats,text="Reveal Password",font=('Arial',10,'bold'),fg=color,bg="#8dc43e",relief="raised",bd=12,command=reveal)
                reveal.pack(pady=10)

                mainmenu = Button(congrats,text="Main Menu",font=('Arial',12,'bold'),fg=color,bg="#8dc43e",relief="raised",bd=12,command=congrats.destroy)
                mainmenu.pack(pady=10)

                congrats.mainloop()
                
        checking_win = Tk()
        checking_win.geometry("640x480+180+80")
        checking_win.title("Checking Account")
        checking_win.configure(background=color)
        checking_win.resizable(0,0)

        main = Label(checking_win, text="Checking Account", font=("Comic Sans MS", 25,'bold'), fg=color, bg='#8dc43e', pady=30,padx = 340)
        main.pack()

        back_button = Button(checking_win, text="<", font=('Arial Rounded MT Bold', 12,'bold'),bg=color, relief="raised", bd=1, command=checking_win.destroy)
        back_button.place(x=30,y=37)

        if color=='#ffffff':
            other_color = '#000000'
            back_button.config(fg=other_color)

        else:
            other_color = '#ffffff'
            back_button.config(fg=other_color)
            
        deposit_lab = Label(checking_win,text="Enter the amount to Deposit:",font=("Arial",20,'bold'),fg=other_color,bg=color)
        deposit_lab.place(x=80,y=190)

        deposit_entry = Entry(checking_win, width=30,font=("Arial",18,'bold'),cursor=f'xterm {color}',fg=color,bg=other_color)
        deposit_entry.place(x=80,y=240)

        back2 = Button(checking_win,text="Done",font=('Arial',15,'bold'),fg=color,bg="#8dc43e",relief="raised",bd=12,command=func)
        back2.place(x=280,y=360)

        checking_win.mainloop()
       
    def loan(): #to create loan account
        new_acc.destroy()
        def detail():
            r = Tk()
            r.geometry("400x400")
            r.title("Details")
            r.configure(background=color)
            r.wm_attributes("-topmost",True)

            if color=='#ffffff':
                other_color = '#000000'
    
            else:
                other_color = '#ffffff'
                
            main = Label(r, text="Loan Account", font=("Comic Sans MS", 20,'bold'), fg=color, bg='#8dc43e', pady=30,padx=120)
            main.pack(anchor='center')

            instruct = Label(r, text="Instructions:", font=("Arial", 15,'bold'), fg='#8dc43e', bg=color, padx=10,pady=10)
            instruct.pack(anchor='w')
            
            lab1 = Label(r, text="You can get loan of any amount you want. The", font=("Arial", 13,'bold'), fg=other_color, bg=color, padx=10,pady=10)
            lab1.pack(anchor='w')

            lab2 = Label(r, text="interest rate on the loan is 2%.", font=("Arial", 13,'bold'), fg=other_color, bg=color, padx=10,pady=10)
            lab2.pack(anchor='w')

            lab3 = Label(r, text="Every month the interest and the fraction of", font=("Arial", 13,'bold'), fg=other_color, bg=color,padx=10,pady=10)
            lab3.pack(anchor='w')

            lab3 = Label(r, text="loan will be debited from Account Balance.", font=("Arial", 13,'bold'), fg=other_color, bg=color, padx=10, pady=10)
            lab3.pack(anchor='w')
            
            button = Button(r, text="Ok", font=('Arial Rounded MT Bold', 13), fg=color, bg='#8dc43e', relief="raised", bd=7, command=r.destroy)
            button.pack(anchor='center')

            r.mainloop()
                    
        detail()
        def deposit_func():
            def func():
                deposit = deposit_entry.get()
                if not(deposit.isdigit()) or int(deposit) == 0:
                    showinfo(message='Invalid Entry')
                    deposit_entry.delete(0,END)               
      
                else:
                    deposit_entry.delete(0,END)
                    account_no = ''             #generating the account number
                    account_no += str(random.randint(10,99))+'-'
                    account_no += str(random.randint(100,999))+'-'
                    account_no += str(random.randint(100000,999999))
                    date = getdate()
                    strg = getdate() + '!'+'Account Created !Balance: '+deposit
                    password = str(random.randint(1000,9999))       #generating the password
                    temp = Customer(fname, lname, address, account_no, password, date, int(deposit), strg, '3',int(loan),int(duration))
                    Administrator.all_accounts.append(temp) 
                    loan_deposit_win.destroy()
                    def reveal():
                        global is_true
                        if  is_true:
                            pass_lab.config(text=f'Password:\t{password}')
                            is_true = False
                        elif not(is_true):
                            pass_lab.config(text=f'Password:\tXXXX')
                            is_true = True
        
                    congrats = Tk()
                    congrats.geometry("640x480+180+80")
                    congrats.title("Loan Account")
                    congrats.configure(background=color)
                    congrats.resizable(0,0)

                    main = Label(congrats, text="Congratulations", font=("Comic Sans MS", 25,'bold'), fg=color, bg='#8dc43e', pady=30,padx = 340)
                    main.pack()

                    back_button = Button(congrats, text="<", font=('Arial Rounded MT Bold', 12,'bold'),bg=color, relief="raised", bd=1, command=congrats.destroy)
                    back_button.place(x=30,y=37)


                    if color=='#ffffff':
                        other_color = '#000000'
                        back_button.config(fg=other_color)

                    else:
                        other_color = '#ffffff'
                        back_button.config(fg=other_color)
                        
                    acccreate_lab= Label(congrats,text="Your Account has been created",font=("Arial",18,'bold'),fg='#8dc43e',bg=color,padx=40,pady=15)
                    acccreate_lab.pack(anchor='w')

                    accno_lab= Label(congrats,text=f"Account No. :\t{account_no}",font=("Arial",16,'bold'),fg=other_color,bg=color,padx=40,pady=15)
                    accno_lab.pack(anchor='w')

                    pass_lab= Label(congrats,text=f"Password :\tXXXX",font=("Arial",16,'bold'),fg=other_color,bg=color,padx=40,pady=15)
                    pass_lab.pack(anchor='w')

                    global is_true
                    is_true = True
                    
                    reveal = Button(congrats,text="Reveal Password",font=('Arial',10,'bold'),fg=color,bg="#8dc43e",relief="raised",bd=12,command=reveal)
                    reveal.pack(pady=10)

                    mainmenu = Button(congrats,text="Main Menu",font=('Arial',12,'bold'),fg=color,bg="#8dc43e",relief="raised",bd=12,command=congrats.destroy)
                    mainmenu.pack(pady=10)

                    congrats.mainloop()

            loan = loan_entry.get()
            duration = duration_entry.get()
            
            if not(loan.isdigit()) or int(loan) == 0:
                showinfo(message='Invalid Loan Amount')
                loan_entry.delete(0,END)               
  
            elif not(duration.isdigit()) or int(duration) == 0:
                duration_entry.delete(0,END)

            else:
                loan_win.destroy()
                loan_deposit_win = Tk()
                loan_deposit_win.geometry("640x480+180+80")
                loan_deposit_win.title("Loan Account Deposit")
                loan_deposit_win.configure(background=color)
                loan_deposit_win.resizable(0,0)

                main = Label(loan_deposit_win, text="Loan Account Deposit", font=("Comic Sans MS", 25,'bold'), fg=color, bg='#8dc43e', pady=30,padx = 340)
                main.pack()

                back_button = Button(loan_deposit_win, text="<", font=('Arial Rounded MT Bold', 12,'bold'),bg=color, relief="raised", bd=1, command=loan_deposit_win.destroy)
                back_button.place(x=30,y=37)

                if color=='#ffffff':
                    other_color = '#000000'
                    back_button.config(fg=other_color)

                else:
                    other_color = '#ffffff'
                    back_button.config(fg=other_color)
                    
                deposit_lab = Label(loan_deposit_win,text="Enter the amount to Deposit:",font=("Arial",20,'bold'),fg=other_color,bg=color)
                deposit_lab.place(x=80,y=190)

                deposit_entry = Entry(loan_deposit_win, width=30,font=("Arial",18,'bold'),cursor=f'xterm {color}',fg=color,bg=other_color)
                deposit_entry.place(x=80,y=240)

                back2 = Button(loan_deposit_win,text="Done",font=('Arial',15,'bold'),fg=color,bg="#8dc43e",relief="raised",bd=12,command=func)
                back2.place(x=280,y=360)

                loan_deposit_win.mainloop()
                
                
        loan_win = Tk()
        loan_win.geometry("640x480+180+80")
        loan_win.title("Loan Account")
        loan_win.configure(background=color)
        loan_win.resizable(0,0)

        main = Label(loan_win, text="Loan Account", font=("Comic Sans MS", 25,'bold'), fg=color, bg='#8dc43e', pady=30,padx = 340)
        main.pack()

        back_button = Button(loan_win, text="<", font=('Arial Rounded MT Bold', 12,'bold'),bg=color, relief="raised", bd=1, command=loan_win.destroy)
        back_button.place(x=30,y=37)

        if color=='#ffffff':
            other_color = '#000000'
            back_button.config(fg=other_color)

        else:
            other_color = '#ffffff'
            back_button.config(fg=other_color)
            
        loan_lab = Label(loan_win,text="Enter the Loan Amount:",font=("Arial",18,'bold'),fg=other_color,bg=color)
        loan_lab.place(x=80,y=160)

        loan_entry = Entry(loan_win, width=30,font=("Arial",16,'bold'),cursor=f'xterm {color}',fg=color,bg=other_color)
        loan_entry.place(x=80,y=200)

        duration_lab = Label(loan_win,text="Enter the Loan Duration:",font=("Arial",18,'bold'),fg=other_color,bg=color)
        duration_lab.place(x=80,y=260)

        duration_entry = Entry(loan_win, width=30,font=("Arial",16,'bold'),cursor=f'xterm {color}',fg=color,bg=other_color)
        duration_entry.place(x=80,y=300)

        back2 = Button(loan_win,text="Done",font=('Arial',15,'bold'),fg=color,bg="#8dc43e",relief="raised",bd=12,command=deposit_func)
        back2.place(x=280,y=360)

        loan_win.mainloop()


    global fname, lname, address
    if indicate == 1:
        login.destroy()
        fname = current.fname
        lname = current.lname
        address = current.address
        
    elif indicate==2:
        if entry1.get() == '' or entry2.get() == '' or entry3.get() == '':
            showinfo(message='Please fill all the fields')
            return
        else:
            fname = entry1.get()
            lname = entry2.get()
            address = entry3.get()
        details.destroy()
        
    new_acc = Tk()
    new_acc.geometry("852x480+180+80")
    new_acc.title("Accounts")
    new_acc.configure(background=color)
    new_acc.resizable(False,False)

    main = Label(new_acc, text="Accounts", font=("Comic Sans MS", 25,'bold'), fg=color, bg='#8dc43e', pady=30,padx = 390)
    main.pack()

    savings = Button(new_acc,text="Savings Account",font=("Arial",15,'bold'),fg=color,bg="#8dc43e",relief="raised",bd=12, command=savings)
    savings.pack(pady=18)

    checking = Button(new_acc,text="Checking Account",font=("Arial",15,'bold'),fg=color,bg="#8dc43e",relief="raised",bd=12, command=checking)
    checking.pack(pady=18)

    loan = Button(new_acc,text="Loan Account",font=('Arial',15,'bold'),fg=color,bg="#8dc43e",relief="raised",bd=12, command=loan)
    loan.pack(pady=18)

    back_button = Button(new_acc, text="<", font=('Arial Rounded MT Bold', 12,'bold'), relief="raised", bd=1, command=new_acc.destroy)
    back_button.place(x=30,y=37)

    if color == '#ffffff': #checking which mode is currently on and customizing the back button accordingly
        back_button.config(fg='#000000', bg=color)
        
    else:
        back_button.config(fg='#ffffff', bg=color)
        
    new_acc.mainloop()
    
def new_cust():
    global entry1, entry2, entry3, details, indicate
    indicate = 2
    create_win.destroy()
    details = Tk()
    details.geometry("640x480+180+80") #customization
    details.title("details")
    details.configure(background=color)
    details.resizable(False,False)

    main = Label(details, text="Details", font=("Comic Sans MS", 25,'bold'), fg=color, bg='#8dc43e', pady=25,padx = 280)
    main.pack()

    if color=='#ffffff':
        other_color = '#000000'
    
    else:
        other_color = '#ffffff'
    
    lab1 = Label(details, text="Enter your  First Name:", font=("Comic Sans MS", 18), fg=other_color, bg=color)
    lab1.place(x=50,y=120)

    entry1 = Entry(details,width=30, font=("Arial", 15,'bold'),cursor=f'xterm {color}',fg=color,bg=other_color)
    entry1.place(x=50,y=165)

    lab2 = Label(details, text="Enter your Last Name:", font=("Comic Sans MS", 18), fg=other_color, bg=color)
    lab2.place(x=50,y=210)

    entry2 = Entry(details, width=30, font=("Arial", 15,'bold'),cursor=f'xterm {color}',fg=color,bg=other_color)
    entry2.place(x=50,y=255)

    lab3 = Label(details, text="Enter your Address :", font=("Comic Sans MS", 18), fg=other_color, bg=color)
    lab3.place(x=50,y=300)

    entry3 = Entry(details, width=30,font=("Arial", 15,'bold'),cursor=f'xterm {color}',fg=color,bg=other_color)
    entry3.place(x=50,y=345)

    confirm = Button(details, text="Confirm", font=("Arial", 15, 'bold'), fg=color, bg="#8dc43e", relief="raised", bd=7, command=create_account)
    confirm.place(x=275, y=400)
    
    details.mainloop()


def existing_cust():
    def submit():
        global current
        username = username_entry.get()
        password = pass_entry.get()
        
        if not(password.isdigit()):     #checking if the password is a valid
            pass_entry.delete(0, END)
            showinfo(message='Invalid Input for password')
            return
        
        a = Administrator()
        temp = a.search_account(username,password) #searching the customer
        if temp == None :                   #checking if the customer does not exist
            username_entry.delete(0, END)
            pass_entry.delete(0, END)
            showinfo(message='User not found')
            return
        else:
            global current,indicate #to indicate which from which window the funtion is called as the func create_account()
            current = temp
            indicate = 1    # is being called from two different windows the indicate will indicate the window
            create_account()
        
    global login
    create_win.destroy()
    login = Tk()
    login.geometry("600x360+340+130")
    login.title("Login")
    login.configure(background=color)
    login.resizable(0,0)

    loginLabel = Label(login, text="Login", font=("Comic Sans Ms", 20), fg=color, bg="#8dc43e", pady=20,padx=270)
    loginLabel.pack()

    back_button = Button(login, text="<", font=('Arial Rounded MT Bold', 10,'bold'), bg=color, relief="raised", bd=1, command=login.destroy)
    back_button.place(x=30,y=34)

    if color=='#ffffff':
        other_color = '#000000'
        back_button.config(fg='#000000')
    else:
        other_color = '#ffffff'
        back_button.config(fg='#ffffff')
        
    username_label = Label(login, text="Enter Username: ", font=("Arial", 12, 'bold'), fg=other_color, bg=color)
    username_label.place(x=160, y=110)

    username_entry = Entry(login, width=30, font=("Arial", 12,'bold'), cursor=f'xterm {color}' , fg=color,bg=other_color)
    username_entry.place(x=160, y=135)

    pass_label = Label(login, text="Enter Password:", font=("Arial", 12, 'bold'), fg=other_color, bg=color)
    pass_label.place(x=160, y=185)

    pass_entry = Entry(login, width=30, font=("Arial", 12,'bold'),cursor=f'xterm {color}', fg=color,bg=other_color)
    pass_entry.place(x=160, y=210)

    submit = Button(login, text="Confirm", font=("Arial", 12, 'bold'), fg=color, bg="#8dc43e", relief="raised", bd=7, command=submit)
    submit.place(x=260, y=260)
    login.mainloop()
    
def create_acc():
    user_win.destroy()
    global create_win   #making it global just so that it could be destroyed in the other function otherwise it won't be destroyed
    create_win = Tk()
    create_win.geometry("852x480+180+80")
    create_win.title("Create Account")
    create_win.configure(background=color)
    create_win.resizable(False,False)

    main = Label(create_win, text="Create Account", font=("Comic Sans MS", 25,'bold'), fg=color, bg='#8dc43e', pady=30,padx = 390)
    main.pack()

    new_acc = Button(create_win,text="New Customer",font=("Arial",15,'bold'),fg=color,bg="#8dc43e",relief="raised",bd=12,command=new_cust)
    new_acc.pack(pady=18)

    existing_acc = Button(create_win,text="Existing Customer",font=("Arial",15,'bold'),fg=color,bg="#8dc43e",relief="raised",bd=12,command=existing_cust)
    existing_acc.pack(pady=18)

    back = Button(create_win,text="Back",font=('Arial',15,'bold'),fg=color,bg="#8dc43e",relief="raised",bd=12,command=create_win.destroy)
    back.pack(pady=18)

    create_win.mainloop()
    
def user():
    def login_acc():
        def user_menu():
            global indicate2
            if isinstance(current.account,Saving_account):  # checking if the account is an instance of saving account class
                current.account.monthlyInterest(getdate())
                
            elif isinstance(current.account,Loan_account): # checking if the account is an instance of loan account class
                current.account.monthlyDebt(getdate())

            global existing_win
            if indicate2 == 2:
                login_win.destroy()
            else:
                user_win.destroy()
                
            existing_win = Tk()
            existing_win.geometry("852x480+180+80")
            existing_win.title("Account Interface")
            existing_win.configure(background=color)
            existing_win.resizable(0,0)

            global first_name, last_name   #due to the limitations of tkinter we can't pass arguments to any function therefore making 
            first_name = current.fname        # arguments global just so it could be accessed in the function
            last_name = current.lname
            
            lab1 = Label(existing_win,text=f"Welcome back {current.fname}",font=("Comic Sans MS",25,'bold'),fg=color,bg='#8dc43e'
                         ,pady=30,padx=250,activeforeground=color,activebackground='#8dc43e')
            lab1.pack()

            withdraw_btn = Button(existing_win,text="Withdraw",font=('Arial',15,'bold'),fg=color,bg="#8dc43e",relief="raised",
                                  bd=12,activeforeground=color,activebackground='#8dc43e',command=current.account.withdraw)
            withdraw_btn.pack(pady=18)

            deposit_btn = Button(existing_win,text="Deposit",font=('Arial',15,'bold'),fg=color,bg="#8dc43e",
                               relief="raised",bd=12,activeforeground=color,activebackground='#8dc43e',command=current.account.deposit)
            deposit_btn.pack(pady=18)

            report_btn = Button(existing_win,text="Report",font=('Arial',15,'bold'),fg=color,bg="#8dc43e",
                               relief="raised",bd=12,activeforeground=color,activebackground='#8dc43e', command=current.account.report)
            report_btn.pack(pady=18)
            
            photo = PhotoImage(file='home button.png')
            home_btn = Button(existing_win,image=photo,relief='raised',command=existing_win.destroy,bd=3,
                          activeforeground=color,activebackground='#8dc43e')
            home_btn.place(x=30,y=45)

            existing_win.mainloop()

        def submit():
            username = username_entry.get()
            password = pass_entry.get()
            
            if not(password.isdigit()):     #checking if the password is a valid
                pass_entry.delete(0, END)
                showinfo(message='Invalid Input for password')
                return
            
            a = Administrator()
            temp = a.search_account(username,password) #searching the customer
            if temp == None :                   #checking if the customer does not exist
                username_entry.delete(0, END)
                pass_entry.delete(0, END)
                showinfo(message='User not found')
                return
            else:
                global current,indicate2
                current = temp
                indicate2 = 2
                user_menu()

        if current == '':    
            global login_win
            user_win.destroy()
            login_win = Tk()
            login_win.geometry("600x360+340+130")
            login_win.title("Login")
            login_win.configure(background=color)
            login_win.resizable(0,0)

            loginLabel = Label(login_win, text="Login", font=("Comic Sans Ms", 20), fg=color, bg="#8dc43e", pady=20,padx=270)
            loginLabel.pack()

            back_button = Button(login_win, text="<", font=('Arial Rounded MT Bold', 10,'bold'), bg=color, relief="raised", bd=1, command=login_win.destroy)
            back_button.place(x=30,y=34)

            if color=='#ffffff':
                other_color = '#000000'
                back_button.config(fg='#000000')
            else:
                other_color = '#ffffff'
                back_button.config(fg='#ffffff')
                
            username_label = Label(login_win, text="Enter Username: ", font=("Arial", 12, 'bold'), fg=other_color, bg=color)
            username_label.place(x=160, y=110)

            username_entry = Entry(login_win, width=30, font=("Arial", 12,'bold'), cursor=f'xterm {color}' , fg=color,bg=other_color)
            username_entry.place(x=160, y=135)

            pass_label = Label(login_win, text="Enter Password:", font=("Arial", 12, 'bold'), fg=other_color, bg=color)
            pass_label.place(x=160, y=185)

            pass_entry = Entry(login_win, width=30, font=("Arial", 12,'bold'),cursor=f'xterm {color}', fg=color,bg=other_color)
            pass_entry.place(x=160, y=210)

            submit = Button(login_win, text="Confirm", font=("Arial", 12, 'bold'), fg=color, bg="#8dc43e", relief="raised", bd=7, command=submit)
            submit.place(x=260, y=260)
            login_win.mainloop()
        else:
            global indicate2
            indicate2 = 1
            user_menu()

    global user_win
    user_win = Tk()
    user_win.geometry("852x480+180+80")
    user_win.title("How we know you?")
    user_win.configure(background=color)
    user_win.resizable(False,False)
    window.destroy()

    lab1 = Label(user_win, text="User", font=("Comic Sans MS", 25,'bold'), fg=color, bg='#8dc43e', pady=30,padx = 390)
    lab1.pack()

    new_acc = Button(user_win,text="New Account",font=("Arial",15,'bold'),fg=color,bg="#8dc43e",relief="raised",bd=12,
                     activeforeground=color,activebackground='#8dc43e',command=create_acc)
    new_acc.pack(pady=18)

    existing_acc = Button(user_win,text="Existing Account",font=("Arial",15,'bold'),fg=color,bg="#8dc43e",relief="raised",bd=12,
                          activeforeground=color,activebackground='#8dc43e',command=login_acc)
    existing_acc.pack(pady=18)

    back = Button(user_win,text="Back",font=('Arial',15,'bold'),fg=color,bg="#8dc43e",relief="raised",bd=12
                  ,activeforeground=color,activebackground='#8dc43e',command=user_win.destroy)
    back.pack(pady=18)

    user_win.mainloop()

def getstring(account): #breaking the string into parts and returning only the desired part
    content = account.string.split('.')
    n = len(content)
    found = None
    for i in range(-1,-n-1,-1):
        if 'withdraw' in content[i].lower():
            found = content[i]
            break
        elif 'deposit' in content[i].lower():
            found = content[i]
            break

    if found == None:
        strg1 ='No transaction have'
        strg2 = 'been made'
    else:
        found = found.split('!')
        strg1 = found[1]
        strg2 = ''
        for i in found[2]:
            if i.isdigit():
                strg2 += i
        if 'withdraw' in found[2].lower():
            strg2 += ' Withdrawn'
        elif 'deposit'in found[2].lower():
            strg2 += ' Deposited'

    return strg1 , strg2

def ad_func():  # admin function
    def submit():
        def gen_report():
            
            def next_list():
                global n
                n += 1
                if n < length:
                    i = Administrator.all_accounts[n]
                    label1.config(text=i.fname)
                    label2.config(text=i.lname)
                    label3.config(text=i.account.account_no)
                    label4.config(text=i.account.balance)

                    a,b = getstring(i.account)

                    label5.config(text=a)
                    label6.config(text=b)
                else:
                    label1.config(text='')
                    label2.config(text='')
                    label3.config(text='')
                    label4.config(text='')
                    label5.config(text='')
                    label6.config(text='')
                    next_button.destroy()
                    
                n += 1
                if n < length:
                    i = Administrator.all_accounts[n]
                    label7.config(text=i.fname)
                    label8.config(text=i.lname)
                    label9.config(text=i.account.account_no)
                    label10.config(text=i.account.balance)

                    a,b = getstring(i.account)

                    label11.config(text=a)
                    label12.config(text=b)
                else:
                    label7.config(text='')
                    label8.config(text='')
                    label9.config(text='')
                    label10.config(text='')
                    label11.config(text='')
                    label12.config(text='')
                    next_button.destroy()

                n += 1  
                if n < length:
                    i = Administrator.all_accounts[n]
                    label13.config(text=i.fname)
                    label14.config(text=i.lname)
                    label15.config(text=i.account.account_no)
                    label16.config(text=i.account.balance)

                    a,b = getstring(i.account)

                    label17.config(text=a)
                    label18.config(text=b)
                    
                else:
                    label13.config(text='')
                    label14.config(text='')
                    label15.config(text='')
                    label16.config(text='')
                    label17.config(text='')
                    label18.config(text='')
                    next_button.destroy()
                    
                n += 1
                if n < length:
                    i = Administrator.all_accounts[n]
                    label19.config(text=i.fname)
                    label20.config(text=i.lname)
                    label21.config(text=i.account.account_no)
                    label22.config(text=i.account.balance)

                    a,b = getstring(i.account)

                    label23.config(text=a)
                    label24.config(text=b)
                else:
                    label19.config(text='')
                    label20.config(text='')
                    label21.config(text='')
                    label22.config(text='')
                    label23.config(text='')
                    label24.config(text='')
                    next_button.destroy()

                if n+1 == length:
                    next_button.destroy()
                    
            administrator.destroy()
            admin_report = Tk()
            admin_report.geometry("852x480+180+80")
            admin_report.title("Report")
            admin_report.configure(background=color)
            admin_report.resizable (0,0)

            main = Label(admin_report, text="Report", font=("Comic Sans MS", 25,'bold'), fg=color, bg='#8dc43e', pady=30,padx = 380)
            main.pack()
            
            back_button = Button(admin_report, text="<", font=('Arial Rounded MT Bold', 12,'bold'), relief="raised", bd=1, command=admin_report.destroy)
            back_button.place(x=30,y=37)
            
            if color == '#ffffff': #checking which mode is currently on and customizing the window accordingly
                back_button.config(fg='#000000', bg=color)
                other_color = '#000000'
                
            else:
                back_button.config(fg='#ffffff', bg=color)
                other_color = '#ffffff'

            fname_lab = Label(admin_report,text='First Name',font=('Arial', 16,'bold'),fg='#8dc43e', bg=color)
            fname_lab.place(x=30, y=110)

            lname_lab = Label(admin_report,text='Last Name',font=('Arial', 16,'bold'),fg='#8dc43e', bg=color)
            lname_lab.place(x=170, y=110)

            account_lab = Label(admin_report,text='Account Number',font=('Arial', 16,'bold'),fg='#8dc43e', bg=color)
            account_lab.place(x=310, y=110)

            bal_lab = Label(admin_report,text='Balance',font=('Arial', 16,'bold'),fg='#8dc43e', bg=color)
            bal_lab.place(x=520, y=110)

            tran_lab = Label(admin_report,text='Last Transaction',font=('Arial', 16,'bold'),fg='#8dc43e', bg=color)
            tran_lab.place(x=640, y=110)

            next_button = Button(admin_report, text="Next", font=("Arial", 10, 'bold'), fg=color, bg="#8dc43e", relief="raised", bd=7,command=next_list)
            next_button.place(x=410, y=430)

            length = len(Administrator.all_accounts)

            global n
            n=0
            if n < length:
                i = Administrator.all_accounts[n]
                label1 = Label(admin_report,text=i.fname,font=('Arial', 16,'bold'),fg=other_color, bg=color)
                label1.place(x=30, y=170)

                label2 = Label(admin_report,text=i.lname,font=('Arial', 16,'bold'),fg=other_color, bg=color)
                label2.place(x=170, y=170)

                label3 = Label(admin_report,text=i.account.account_no,font=('Arial', 16,'bold'),fg=other_color, bg=color)
                label3.place(x=310, y=170)

                label4 = Label(admin_report,text=i.account.balance,font=('Arial', 16,'bold'),fg=other_color, bg=color)
                label4.place(x=520, y=170)

                a,b = getstring(i.account)

                label5 = Label(admin_report,text=a ,font=('Arial', 16,'bold'),fg=other_color, bg=color)
                label5.place(x=640, y=155)

                label6 = Label(admin_report,text=b ,font=('Arial', 16,'bold'),fg=other_color, bg=color)
                label6.place(x=640, y=185)

            n += 1
            if n < length:
                i = Administrator.all_accounts[n]
                label7 = Label(admin_report,text=i.fname,font=('Arial', 16,'bold'),fg=other_color, bg=color)
                label7.place(x=30, y=245)

                label8 = Label(admin_report,text=i.lname,font=('Arial', 16,'bold'),fg=other_color, bg=color)
                label8.place(x=170, y=245)

                label9 = Label(admin_report,text=i.account.account_no,font=('Arial', 16,'bold'),fg=other_color, bg=color)
                label9.place(x=310, y=245)

                label10 = Label(admin_report,text=i.account.balance,font=('Arial', 16,'bold'),fg=other_color, bg=color)
                label10.place(x=520, y=245)

                a,b = getstring(i.account)

                label11 = Label(admin_report,text=a ,font=('Arial', 16,'bold'),fg=other_color, bg=color)
                label11.place(x=640, y=230)
                
                label12 = Label(admin_report,text=b ,font=('Arial', 16,'bold'),fg=other_color, bg=color)
                label12.place(x=640, y=260)
            else:
                next_button.destroy()
                
            n += 1    
            if n < length:
                i = Administrator.all_accounts[n]
                label13 = Label(admin_report,text=i.fname,font=('Arial', 16,'bold'),fg=other_color, bg=color)
                label13.place(x=30, y=320)

                label14 = Label(admin_report,text=i.lname,font=('Arial', 16,'bold'),fg=other_color, bg=color)
                label14.place(x=170, y=320)

                label15 = Label(admin_report,text=i.account.account_no,font=('Arial', 16,'bold'),fg=other_color, bg=color)
                label15.place(x=310, y=320)

                label16 = Label(admin_report,text=i.account.balance,font=('Arial', 16,'bold'),fg=other_color, bg=color)
                label16.place(x=520, y=320)

                a,b = getstring(i.account)

                label17 = Label(admin_report,text=a ,font=('Arial', 16,'bold'),fg=other_color, bg=color)
                label17.place(x=640, y=305)
                
                label18 = Label(admin_report,text=b ,font=('Arial', 16,'bold'),fg=other_color, bg=color)
                label18.place(x=640, y=335)
            else:
                next_button.destroy()
                
            n += 1
            if n < length:
                i = Administrator.all_accounts[n]
                label19 = Label(admin_report,text=i.fname,font=('Arial', 16,'bold'),fg=other_color, bg=color)
                label19.place(x=30, y=395)

                label20 = Label(admin_report,text=i.lname,font=('Arial', 16,'bold'),fg=other_color, bg=color)
                label20.place(x=170, y=395)

                label21 = Label(admin_report,text=i.account.account_no,font=('Arial', 16,'bold'),fg=other_color, bg=color)
                label21.place(x=310, y=395)

                label22 = Label(admin_report,text=i.account.balance,font=('Arial', 16,'bold'),fg=other_color, bg=color)
                label22.place(x=520, y=395)

                a,b = getstring(i.account)

                label23 = Label(admin_report,text=a ,font=('Arial', 16,'bold'),fg=other_color, bg=color)
                label23.place(x=640, y=380)
                
                label24 = Label(admin_report,text=b ,font=('Arial', 16,'bold'),fg=other_color, bg=color)
                label24.place(x=640, y=410)
            else:
                next_button.destroy()

            if n+1>=length:
                next_button.destroy()
                
            admin_report.mainloop()


        f = open('Admin.txt')
        content = f.read()
        content = content.split('\n')
        content.pop(0) #removing the first line since it contains the template
        f.close()       #closing the file as it is no longer needed
        match = False
        for i in range(len(content)):
            i = content[i].split(',')
            if id_entry.get() == i[0] and pass_entry.get() == i[1]:
                match = True #iD and password had been matched
                break
 
        if match: #checking if match has been found 
            global administrator
            administrator = Tk()
            administrator.title("Administrator Interface")
            administrator.geometry("600x400+290+130")
            administrator.configure(background=color)
            administrator.resizable(0,0)
            admin.destroy()

            lab9 = Label(administrator, text="ADMINISTRATOR", font=("Comic Sans MS", 25,'bold'), fg=color, bg='#8dc43e', pady=20,padx = 250)
            lab9.pack()

            Reportbutton = Button(administrator, text="Generate Report", font=("Arial", 15, 'bold'), fg=color, bg="#8dc43e", relief="raised", bd=10,command=gen_report)
            Reportbutton.pack(anchor='center', pady=40)

            ad_back = Button(administrator, text="Back",font=("Arial", 15, 'bold'), fg=color, bg="#8dc43e", relief="raised", bd=10, command=administrator.destroy)
            ad_back.pack(anchor='center', pady=18)

            administrator.mainloop()
        else:
            showinfo(message='Access Denied')
            id_entry.delete(0,END)
            pass_entry.delete(0,END)

        
    window.destroy()
    admin = Tk()
    admin.geometry("600x360+340+130")
    admin.title("Login")
    admin.configure(background=color)
    admin.resizable(0,0)

    loginLabel = Label(admin, text=" Admin Login", font=("Comic Sans Ms", 20), fg=color, bg="#8dc43e", pady=20,padx=270)
    loginLabel.pack()

    back_button = Button(admin, text="<", font=('Arial Rounded MT Bold', 10,'bold'), bg=color, relief="raised", bd=1, command=admin.destroy)
    back_button.place(x=30,y=34)

    if color=='#ffffff':
        other_color = '#000000'
        back_button.config(fg='#000000')
    else:
        other_color = '#ffffff'
        back_button.config(fg='#ffffff')
        
    id_label = Label(admin, text="Enter ID: ", font=("Arial", 12, 'bold'), fg=other_color, bg=color)
    id_label.place(x=160, y=110)

    id_entry = Entry(admin, width=30, font=("Arial", 12,'bold'), cursor=f'xterm {color}' , fg=color,bg=other_color)
    id_entry.place(x=160, y=135)

    pass_label = Label(admin, text="Enter Password:", font=("Arial", 12, 'bold'), fg=other_color, bg=color)
    pass_label.place(x=160, y=185)

    pass_entry = Entry(admin, width=30, font=("Arial", 12,'bold'),cursor=f'xterm {color}', fg=color,bg=other_color)
    pass_entry.place(x=160, y=210)

    submit = Button(admin, text="Confirm", font=("Arial", 12, 'bold'), fg=color, bg="#8dc43e", relief="raised", bd=7, command=submit)
    submit.place(x=260, y=260)
    admin.mainloop()
    
def settings():
    def faq1():
        lab6.config(text='')
        lab7.config(text='')
        button1.destroy()
        button2.destroy()
        button3.destroy()
        on_.config(state=DISABLED)

        if color == '#ffffff':
            other_color = '#000000'
        else:
            other_color = '#ffffff'
            
        lab8 = Label(win,text='Your Account Number will serve as the username and the password',font=("Arial", 16),fg=other_color,bg=color)
        lab8.place(x=95,y=310)

        lab9 = Label(win,text='provided to you at the time of creation of account will serve as the',font=("Arial", 16),fg=other_color,bg=color)
        lab9.place(x=95,y=335)

        lab10 = Label(win,text='password.',font=("Arial", 16),fg=other_color,bg=color)
        lab10.place(x=95,y=360)

    def faq2():
        lab5.config(text='')
        lab6.config(text='')
        lab7.config(text='')
        button1.destroy()
        button2.destroy()
        button3.destroy()
        on_.config(state=DISABLED)
        
        if color == '#ffffff':
            other_color = '#000000'
        else:
            other_color = '#ffffff'

        lab8 = Label(win, text='When and how the mothly interest will be credited to my account?', bg=color, fg=other_color, font=("Arial", 16))
        lab8.place(x=90,y=270)
        
        lab9 = Label(win,text='The monthly interest will be credited to the account every month',font=("Arial", 16),fg=other_color,bg=color)
        lab9.place(x=95,y=310)

        lab10 = Label(win,text='without your notice.',font=("Arial", 16),fg=other_color,bg=color)
        lab10.place(x=95,y=335)
        
    def faq3():
        lab5.config(text='')
        lab6.config(text='')
        lab7.config(text='')
        button1.destroy()
        button2.destroy()
        button3.destroy()
        on_.config(state=DISABLED)
        
        if color == '#ffffff':
            other_color = '#000000'
        else:
            other_color = '#ffffff'

        lab8 = Label(win, text='When i will have to pay my loan? How can i pay my loan?', bg=color, fg=other_color, font=("Arial", 16))
        lab8.place(x=90,y=270)
        
        lab9 = Label(win,text='The fraction of loan will be debited from your account balance every',font=("Arial", 16),fg=other_color,bg=color)
        lab9.place(x=95,y=300)

        lab10 = Label(win,text='month upto the time loan duration has ended. If your account does not',font=("Arial", 16),fg=other_color,bg=color)
        lab10.place(x=95,y=325)

        lab11 = Label(win,text='contain suficient balance, the next time you deposit any amount',font=("Arial", 16),fg=other_color,bg=color)
        lab11.place(x=95,y=350)        

        lab11 = Label(win,text='the previous remainings will be debited from it.',font=("Arial", 16),fg=other_color,bg=color)
        lab11.place(x=95,y=375)
        
    def button_mode():
        global color
        if color == '#ffffff':      #changing the mode from night to day and day to night
            on_.config(image=night)
            color = '#000000'
            lab2.config(text="Night Mode is On",bg=color)
            lab3.config(bg=color)
            win.config(background=color)
            lab1.config(foreground = color)
            back_button.config(bg=color,fg='#ffffff')
            lab4.config(bg=color)
            lab5.config(fg='#ffffff',bg=color)
            lab6.config(fg='#ffffff',bg=color)
            lab7.config(fg='#ffffff',bg=color)
            button1.config(fg='#ffffff',bg=color)
            button2.config(fg='#ffffff',bg=color)
            button3.config(fg='#ffffff',bg=color)
            if current != '':
                log_button.config(fg=color)
            on_.config(bg=color, activebackground=color)
        else:
            on_.config(image=day)
            color = '#ffffff'
            lab2.config(text="Day Mode is On",bg=color)
            lab4.config(bg=color)
            lab3.config(bg=color)
            win.config(background=color)
            lab1.config(foreground = color)
            back_button.config(bg=color,fg='#000000')
            lab5.config(fg='#000000',bg=color)
            lab6.config(fg='#000000',bg=color)
            lab7.config(fg='#000000',bg=color)
            button1.config(fg='#000000',bg=color)
            button2.config(fg='#000000',bg=color)
            button3.config(fg='#000000',bg=color)
            if current != '':
                log_button.config(fg=color)
            on_.config(bg=color, activebackground=color)

    def logout():
        global current
        current= ''
        showinfo(message='Account has been logged out')
        log_button.destroy()

    window.destroy()     
    win = Tk()
    win.geometry("852x480+180+80")
    win.title("Bank On")
    win.configure(background=color)
    win.resizable(0,0)     #so that window can't be maximize
    
    lab1 = Label(win, text="Settings", font=("Comic Sans MS", 25,'bold'), fg=color, bg='#8dc43e', pady=30,padx = 360)
    lab1.pack()

    lab2 = Label(win, text="", bg=color, fg="#8dc43e", font=("Arial", 18,'bold'))
    lab2.place(x=80,y=145)

    day = PhotoImage(file="day.png")
    night = PhotoImage(file="night.png")

    on_ = Button(win,bg=color, borderwidth=0, command=button_mode, activebackground=color)
    on_.place(x=400,y=142)

    back_button = Button(win, text="<", font=('Arial Rounded MT Bold', 12,'bold'), relief="raised", bd=1, command=win.destroy)
    back_button.place(x=30,y=37)
    
    if color == '#ffffff':            #checking which mode is currently on and customizing the window accordingly
        lab2.config(text="Day Mode is On")
        other_color = '#000000'
        on_.config(image=day)
        back_button.config(fg='#000000', bg=color)
        
    else:
        lab2.config(text="Night Mode is On")
        other_color = '#ffffff'
        on_.config(image=night)
        back_button.config(fg='#ffffff', bg=color)
            
    if current != '' :
        log_button = Button(win, text="Logout", font=('Arial', 12, 'bold'), fg=color, bg="#8dc43e", relief="raised",bd=12,command=logout)
        log_button.place(x=380,y=400)

    lab3 = Label(win, text='Help:', bg=color, fg="#8dc43e", font=("Arial", 18,'bold'))
    lab3.place(x=80,y=195)

    lab4 = Label(win, text='FAQs:', bg=color, fg="#8dc43e", font=("Arial", 16,'bold'))
    lab4.place(x=90,y=235)

    lab5 = Label(win, text='Where can i find my Username and Password?', bg=color, fg=other_color, font=("Arial", 16))
    lab5.place(x=90,y=270)

    lab6 = Label(win, text='When and how the mothly interest will be credited to my account?', bg=color, fg=other_color, font=("Arial", 16))
    lab6.place(x=90,y=315)
    
    lab7 = Label(win, text='When i will have to pay my loan? How can i pay my loan?', bg=color, fg=other_color, font=("Arial", 16))
    lab7.place(x=90,y=360)

    button1 = Button(win, text='V',bg=color,fg=other_color, font=("Arial", 12,'bold'),bd=3,command=faq1)
    button1.place(x=550,y=265)

    button2 = Button(win, text='V',bg=color,fg=other_color, font=("Arial", 12,'bold'),bd=3,command=faq2)
    button2.place(x=725,y=310)

    button3 = Button(win, text='V',bg=color,fg=other_color, font=("Arial", 12,'bold'),bd=3,command=faq3)
    button3.place(x=645,y=355)
    win.mainloop()


def read_accounts():
    f = open('accounts.txt')
    j = 0                   #counter varible just to keep the count of iteration
    for i in f.readlines():
        j += 1       #increamenting j at each iteration
        if j == 1:   #the first line of the file contains the template therefore skiping the iteration for the first line
            continue

        content = i.split(',')     #as the last line is empty the last list will contain \n as one and only element so will skip the last iteration
        if content[0] == '\n':     #skiping the last iteration
            continue
        
        if content[8] == '1':       #content list contains [fname,lname,address,account_no,password,date,bal,strg,type]
            temp = Customer(content[0],content[1],content[2],content[3],content[4],content[5],int(content[6]),content[7],content[8])
            Administrator.all_accounts.append(temp)
            
        elif content[8] == '2':     #content list contains [fname,lname,address,account_no,password,date,bal,strg,type]
            temp = Customer(content[0],content[1],content[2],content[3],content[4],content[5],int(content[6]),content[7],content[8])
            Administrator.all_accounts.append(temp)
            
        elif content[8] == '3':     #content list contains [fname,lname,address,account_no,password,date,bal,strg,type,pricipal_amount, loan_duration
            temp = Customer(content[0],content[1],content[2],content[3],content[4],content[5],int(content[6]),content[7],content[8],int(content[9]),int(content[10]))
            Administrator.all_accounts.append(temp)


def quit_func():
    f = open('accounts.txt','w')
    n = len(Administrator.all_accounts)
    f.write('First Name , Last Name , Address, Account No. , Password, Date, Balance, String, Type, Principal Amount, Loan Duration \n')
    strg = ''
    for i in range(n):
        a = Administrator.all_accounts[i]
        if isinstance(a.account,Saving_account):    #checking the account type and writing to the file accordingly
            strg += a.fname+','+a.lname+','+a.address+','+a.account.account_no+','+ a.account.password +','+ a.account.date +','+ str(a.account.balance)+',' \
                    +a.account.string + ',1, \n'
            
        elif isinstance(a.account,Checking_account):
            strg += a.fname+','+a.lname+','+a.address+','+a.account.account_no+','+ a.account.password +','+ a.account.date + ',' + str(a.account.balance)+',' \
                    +a.account.string + ',2, \n'
            
        elif isinstance(a.account,Loan_account):
            strg += a.fname +','+ a.lname +','+a.address +',' +a.account.account_no +','+ a.account.password +','+ a.account.date + ',' + str(a.account.balance)+','+a.account.string + ',3,' \
                   + str(a.account.principleAmount) + ',' + str(a.account.loanDuration) +',\n'
    f.write(strg)
    f.close()
    quit()


read_accounts() #reading the acounts from the file

while True:
    window = Tk()
    window.geometry("852x480+180+80")
    window.title("Bank On")
    window.configure(background=color)
    window.resizable(False,False)

    lab1 = Label(window, text="WELCOME TO BANK ON", font=("Comic Sans MS", 25,'bold'), fg=color, bg='#8dc43e', pady=30,padx = 250)
    lab1.pack()

    UserButton = Button(window, text="User", font=("Arial", 15, 'bold'), fg=color, bg="#8dc43e", relief="raised", bd=12,command=user)
    UserButton.pack(anchor='center', pady=18)

    AdButton = Button(window, text="Administrator", font=("Arial", 15, 'bold'), fg=color, bg="#8dc43e",relief="raised", bd=12,command=ad_func)
    AdButton.pack(anchor='center', pady=18)

    QButton = Button(window, text="Settings", font=('Arial', 15, 'bold'), fg=color, bg="#8dc43e", relief="raised",bd=12,command=settings)
    QButton.pack(anchor='center',pady=18)

    photo = PhotoImage(file='exit.png')
    exit_button = Button(window,image=photo,relief='raised',command=quit_func,bd=3)
    exit_button.place(x=30,y=35)

    window.mainloop()

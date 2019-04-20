import sqlite3
from getpass import *
from time import *
import json
import os
#from validate_email import validate_email
c=10000
def manager(d):
    m={"Username":"Sasbm123@","Password":"password"}
    print("AUTHENTICATION REQUIRED TO ACCESS DATABASE\n") 
    usern=input("Enter your username")
    pas=input("Enter Your password")
    for i in range(0,5):
        if i==0:
            print("please wait",end="")
            #time.sleep(0.50)
            print(".",end="")
        if usern==m.get("Username") and m.get("Password")==pas:
            print("\nACCESS GRANTED\n")
            print("Welcome Mr. Sahil")
            return
        else:
            print("\nINCORRECT DETAILS\n")
            print("SORRY!!  ")
            return
    
def create(d):
    global c
    c=c+1
    
    name=input("enter your name =")
    user_name=input("enter your user name =")
    acc_type=input("want to open \n\t1. Saving \n\t2. Current ")
    aadhar=input("Enter your aadhar number =")
    while(len(aadhar)!=16):
        aadhar=input("Enter your Correct aadhar number =")
    number=input("Enter your contact number =")
    while(len(number)!=10):
        number=input("Enter your Correct contact number =")
    age=input("Enter your age =")
    mail=input("Enter your E-mail Address =")
    #while(not validate_email()):
      #mail=input("Enter Correct E-mail Address =")
    pas=getpass("Enter your password =")
    amount=int(input("Enter your initial amount (minimum 2000) ="))
    while(amount<2000):
        print("Amount should be greater or equal to 2000")
        amount=int(input("Enter your initial amount (minimum 2000)"))
    data = {c:[name,user_name,acc_type,aadhar,number,age,mail,pas,amount]}
    if type(d)!=dict:
        d={}
    d.update(data)
    return d
def Update():
    pass
def deposite(a):
    A=input("enter your account number")
    for i in a:
        if i==A:
            list=a.get(A)
            x=int(input("Enter Amount You Want To deposite"))
            diff=list[8]+x
            if diff<0:
                print("INSUFFICENT BALANCE!!")
                deposite(a)
            else:
                list[8]=diff
                print("Your Updated Balance Is =",list[8])
         
    di={A:list}
    a.update(di)
    return a
def withdraw(d):
    n=input("enter your account number")
    for i in data:
        list=data.get(n)
        if list[1]==input("enter your user name") and list[7]==input("enter your password"): 
            print("WELCOME ",list[0])
            amount=int(input("Enter Withdrawl Ammount "))
            list[8]=list[8]-amount
            break
        else:
            print("INCORRECT DETAILS",withdraw(d))
            break
    d1={n:list}
    data.update(d1)
    return data

def Detail(d):
    os.system("cls")
    n=input("Enter your account number")
    for i in data:
        if n == i:
            list=data.get(n)
            if list[1]==input("enter your user name") and list[7]==input("enter your password"):
                print("WELCOME ",list[0])
                print("Your account balance is:",list[8])
    
        
fp=open("project.json","r+")
fp.seek(0)
data=json.load(fp)
fp.close()
while(1):
    x=int(input("Enter your choice \n \t 1. Create New Account \n \t 2. Update Your Detail\n \t 3. Deposite Amount \n\t 4. Withdraw Money\n\t 5. Show Detail\n\t 6. Manager Login \n\t 7. Exit \n\t"))
    if x==1:
        data=create(data)
    elif x==2:
        data=Update(data)
    elif x==3:
        data=deposite(data)
    elif x==4:
        data=withdraw(data)
    elif x==5:
        data=Detail(data)
    elif x==6:
        data=manager(data)
    elif x==7:
        fp=open("project.json","w+")
        json.dump(data,fp)
        fp.close()
        print("THANKYOU FOR VISITING US!!")
        break

#INVENTORY MANAGEMENT SYSTEM (Using Function and Binary File-Handling)

import pickle
import sys
import os

dict={}

def write_in_file():
    file=open("item.dat","ab") #a - append, b - binary
    no=int(input("ENTER NO. OF ITEMS - "))
    for i in range(no):
        print("ENTER ITEM ",i+1,"DETAILS")
        dict["ItemNumber"]=int(input("ENTER THE ITEM NO. - "))
        dict["ItemName"]=input("ENTER THE ITEM NAME - ")
        dict["Rate"]=int(input("ENTER THE RATE - "))
        dict["Quantity"]=int(input("ENTER THE QUANTITY - "))
        pickle.dump(dict,file) #dump - to write in student file
    file.close()

def display(): #read from file and display
    file=open("item.dat","rb") #r - read, b - binary
    try:
        while True:
            items=pickle.load(file) #reads from the file
            print(items)
    except EOFError:
        pass
    file.close()

def search():
    file=open("item.dat","rb") #r - read, b - binary
    n=int(input("ENTER THE ITEM NUMBER TO SEARCH - "))
    found=0
    try:
        while True:
            data=pickle.load(file) #reads from file
            if data["ItemNumber"]==n:
                print("Record Found")
                print(data)
                found=1
                break
    except EOFError:
        pass
    if found==0:
        print("Record Not Found")
    file.close()

def update():
    f1=open("item.dat","rb") #r - read, b - binary
    f2=open("temp.dat","ab")
    r=int(input("ENTER THE ITEM NUMBER TO UPDATE - "))
    try:
        while True:
            data=pickle.load(f1) #reads from file
            if data["ItemNumber"]==r:
                print("ENTER NEW DETAILS OF THE ITEM - ")
                data["ItemNumber"]=int(input("ENTER THE ITEM NUMBER - "))
                data["Item"]=input("ENTER THE ITEM NAME - ")
                data["Rate"]=int(input("ENTER THE RATE - "))
                data["Quantity"]=int(input("ENTER THE QUANTITY - "))
                pickle.dump(data,f2)
            else:
                pickle.dump(data,f2)
    except EOFError:
        pass
    f1.close()
    f2.close()
    os.remove("item.dat")
    os.rename("temp.dat","item.dat")
    file=open("item,dat","rb") #r - read, b - binary
    try:
        while True:
            items=pickle.load(file) #reads from file
            print(items)
    except EOFError:
        pass
    file.close()

def delete():
    f1=open("item.dat","rb") #r - read, b - binary
    f2=open("temp.dat","ab")
    r=int(input("ENTER THE ITEM NUMBER TO DELETE - "))
    try:
        while True:
            data=pickle.load(f1) #reads from file
            if data["ItemNumber"]==r:
                pass
            else:
                pickle.dump(data,f2)
    except EOFError:
        pass
    f1.close()
    f2.close()
    os.remove("item.dat")
    os.rename("temp.dat","item.dat")
    file=open("item.dat","rb") #r - read, b - binary
    print("RECORD AFTER DELETION - ")
    try:
        while True:
            items=pickle.load(file) #reads from file
            print(items)
    except EOFError:
        pass
    file.close()

#Main Program
while True:
    print("MENU \n 1. Write in a file \n 2. Display \n 3. Search\n 4. Update \n 5. Delete  \n 6. Exit\n")
    ch=int(input("ENTER YOUR CHOICE - "))
    if ch==1:
        print("TO WRITE")
        write_in_file()
    if ch==2:
        display()
    if ch==3:
        search()
    if ch==4:
        print("UPDATE")
        update()
    if ch==5:
        print("DELETE")
        delete()
    if ch==6:
        print("Thank You! Have a Nice Day.")
        sys.exit()
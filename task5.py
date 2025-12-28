def addcn():
    name=input("Enter name: ")
    phone=input("Enter phone number: ")
    email=input("Enter email address: ")
    address=input("Enter address: ")
    lst.append((name,phone,email,address))
def viewcn():
    i=1
    for cn in lst:
        print(i,". ",end="")
        i+=1
        for dt in cn:
            print(dt)
def searchcn():
    search=input("Enter name or contact number you want to search: ")
    for cn in lst:
        if(search==cn[0]) or (search==cn[1]):
            for dt in cn:
                print(dt)
        break
    else:
            print("Contact doesn't exist.")
def updatecn():
    viewcn()
    num=int(input("Enter contact serial number you want to update: "))
    choose=input("Enter the first letter of detail you want to update(name/phone/email/address): ")
    list1=list(lst[num-1])
    match choose:
        case 'n':
            name=input("Enter new name: ")
            list1[0]=name
        case 'p':
            phone=input("Enter new phone number: ")
            list1[1]=phone
        case 'e':
            email=input("Enter new email address: ")
            list1[2]=email
        case 'a':
            address=input("Enter new address: ")
            list1[3]=address
        case _:
            print("Invalid choice!")
    lst[num-1]=list1
def deletecn():
    viewcn()
    num=int(input("Enter contact serial number you want to delete: "))
    tp1=lst.pop(num-1)
    print("Deleted contact details: ")
    for dt in tp1:
        print(dt)

print("Hello User!\nChoose your option:")
lst=[]
def user():
    print("""1. Add Contact
2. View Contact 
3. Search Contact
4. Update Contact
5. Delete Contact""")
    choice=int(input("Enter your choice(number): "))
    match choice:
        case 1:
            addcn()
        case 2:
            viewcn()
        case 3:
            searchcn()
        case 4:
            updatecn()
        case 5:
            deletecn()
        case _:
            print("Invalid Choice!")
    print("Want to perform operations again?(Type y/n): ")
    ch=input().lower()
    if(ch=='y'):
        user()
    elif(ch=='n'):
        return
    else:
        print("Invalid choice!")
        return
user()
print("Have a Good Day!")

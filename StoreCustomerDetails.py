

def add():
    id = input("Customer ID: ")
    name = input("Customer name: ")
    ad = input("Customer Address: ")
    cnic = input("Customer CNIC: ")
    phone = input("Customer phone_number: ")

    file = open("F:\\Python\\customer.txt", "a")
    file.write(id+"\t")
    file.write(name+"\t")
    file.write(ad+"\t")
    file.write(cnic+"\t")
    file.write(phone+"\t")

    #print("\n")
    print("Record is Added.")
    #file.close()


def delt():
    id = input("Enter ID to remov the record from file.")
    with  open("F:\\Python\\customer.txt", "r") as file:
        all = file.readlines()

    with open("F:\\Python\\customer.txt", "w") as file:
        for data in all:
            d = data.split("\t")
            if(d[0] != id):
                file.writelines(data)
               # print("\n")
    
    print("Record is deleted..")



def update():
    id = input("Enter ID to Update the record from file.")
    with  open("F:\\Python\\customer.txt", "r") as file:
        all = file.readlines()

    with open("F:\\Python\\customer.txt", "w") as file:
        for data in all:
            d = data.split("\t")
            if d[0] == id:
                name = input("Customer name: ")
                ad = input("Customer Address: ")
                cnic = input("Customer CNIC: ")
                phone = input("Customer phone_number: ")
                file.writelines(d[0]+"\t"+name+"\t"+ ad+ "\t"+cnic+"\t"+phone)
            else:
                #print("\n")
                file.writelines(data) 
    
    print("Record is Updated.")



def search():
    id = input("Enter ID to Search the record from file.")
    with  open("F:\\Python\\customer.txt", "r") as file:
        all = file.readlines()

    for data in all:
        d = data.split("\t")
        if d[0] == id:
            print(data)
                 
    
    
    
def showRecords():
    print("All record in the file.")
    with  open("F:\\Python\\customer.txt", "r") as file:
        all = file.readlines()

    for data in all:
       print(data)


while True:
    print("Welcome to customer portal")
    print("1 --> Add new customer")
    print("2 --> Delt customer")
    print("3 --> Update the customer")
    print("4 --> Search customer")
    print("5 --> Show all records")
    print("6 --> exsit the file")

    choice = int(input("Enter your choice: "))

    if ( choice == 1):
        add()
    elif (choice == 2):
        delt()
    elif (choice == 3):
        update()
    elif ( choice == 4):
        search()
    elif ( choice == 5):
        showRecords()
    elif ( choice == 6):
        break
    else:
        print("Your choice is invaild...")



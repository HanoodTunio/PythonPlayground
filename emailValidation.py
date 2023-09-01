
i=1
j = 0

while i != 0:
    email = input("Enter your Email: ")
    if len(email) > 6:
        if email[0].isalpha():
            if ("@" in email) and (email.count("@")==1 and (" " not in email) ):
                for x in email:
                    if (x == "." or x=="@" or x != x.upper()):
                        continue
                    
                    else:
                        print("Email is invaild..")
                        i=1
                        j=1
                        break
                if j != 1:
                    i=0
                    print("Email is Vaild..")
            
            else:
                print("wrong email. according to 3rd condition")
        else:
            print("wrng email. acoording to condition 2:")
    else:
        print("Wrong email. according to 1 condition") 
import time
dict = {}

while True:
    print("Your Choice: ")
    print("C for create account: ")
    print("L for log in: ")
    print("E for exit: ")
    print(" ")
    time.sleep(2)
    user = input("Enter your choice: \n")

    if user == 'c' or user == 'C':
        username = input("Enter username: ")
        password = input("Enter password: ")
        if len(password) > 7:
            pas = input("confirm password: ")
            if password == pas:
                dict[username] = password
                time.sleep(1)
                print(" ")
                print("Your account has created: ")
            else:
                time.sleep(2)
                print("Password does not match")
        else:
            time.sleep(2)
            print("Your password must contains more than 7 letters")

    elif user == 'l' or user == 'L':
        username = input("username: ")
        if username in dict.keys():
            password = input("Password: ")
            username == dict[username]
            dict[username] == password
            if password == dict[username]:
                time.sleep(2)
                print("You are successfully logged in: ")
            else:
                time.sleep(2)
                print("Password is incorrect")
        else:
            print("Username not found")
    elif user == 'e' or user == 'E':
        break

    else:
        time.sleep(2)
        print("Make the correct choice")

    print(" ")
    time.sleep(2)

    for i,j in dict.items():
        print(i,j)

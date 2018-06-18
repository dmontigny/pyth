correct_password = "python123"
name = input("Enter name: ")
password = input("Enter password: ")

while correct_password != password:
    password = input("Wrong password. Please re-enter: ")
    
print("Hi, %s. You are now logged in!" % name)


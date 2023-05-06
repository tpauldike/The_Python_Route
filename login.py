username = 'topman'
pswd = 'pld123'

auth = input("Please enter your password: ")

while (True):
    if auth == pswd:
        print("You're successfully logged in")
        break
    else:
        print("Wrong password")
        auth = input("Please enter your password: ")

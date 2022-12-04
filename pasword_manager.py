master_pwd = input('Enter your master password: ')



def view():
    with open('password.txt','r') as f:
        #print(f.readline().rstrip())
        for line in f.readlines():
            data = line.rstrip() #rstrip() = Return a copy of the string with trailing whitespace removed.
            user,passw = data.split("|")
            print("Username:",user,",","Password:",passw)

def add():
    name = input('Username: ')
    pwd = input('Password: ')
    
    with open('password.txt','a') as f:   #with open('password.txt','a') as f ==== f= open('password.txt','a')
        f.write(name + "|" + pwd + '\n')



while True:
    mode = input('Would you like to add or view password, (q to quit): '.lower())
    if mode == 'q':
        break
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        break




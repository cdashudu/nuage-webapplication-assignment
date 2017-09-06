import requests
import sys



def login(username, password):
    s=requests.Session()

    payload={'inputEmail':username, 'inputPassword':password}
    url='http://54.71.230.219/validateLogin' #Change the URL
    x=s.post(url,data=payload)
    if(x.status_code==200):

        global session_user
        session_user=username
        return s
    else:
        return 0


def signup(name, username, password):
    payloadAddWish={'inputName':name, 'inputEmail':username,'inputPassword':password}
    url='http://54.71.230.219/signUp' #Change the URL
    x=requests.post(url,data=payloadAddWish)
    if(x.status_code==200):
        return "Success"
    else:
        return "Check Input. Email ID should be valid"    
    


def addWish(session,title,description):
    s=session
    payloadAddWish={'inputTitle':title, 'inputDescription':description}
    url='http://54.71.230.219/addWish' #Change the URL
    x=s.post(url,data=payloadAddWish)
    return "Success"



#def deleteWish(title,description):

#def editWish(title,description):

def logout():
    sys.exit(1)



while(True):
    print("Welcome to wish List App")
    print("Press 1 to login")
    print("Press 2 to signup")
    user_input=raw_input()

    if(user_input=='1'):
        print("Enter User name")
        username=raw_input()
        print("Enter your password")
        password=raw_input()
        res=login(username,password)
        if(res!=0):
            print(session_user)
            while(True):
                print("1: Add a wish ")
                print("2: View wishes")
                print("3: Delete a wish")
                print("4: Edit a wish")
                print("5: logout")
                option=raw_input()
                if(option=='1'):
                    print("Enter a wish title")
                    title=raw_input()
                    print("Enter the wish description")
                    description=raw_input()
                    addWish(res,title,description)
                elif(option=='2'):
                    viewWishes()
                elif(option=='3'):
                    print("Enter wish ID to delete")
                    wishID=raw_input()
                    deleteWish(wishID)
                elif(option=='4'):
                    print("Enter wish ID to Edit")
                    wishID=raw_input()
                    editWish(wishID)
                else:
                    logout()
                    break





    else:
        print("Enter your name")
        name=raw_input()
        print("Enter your email")
        email=raw_input()
        print("Enter a password")
        password=raw_input()
        signup(name,email,password)

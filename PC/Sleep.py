import os, getpass, datetime,time

def cheque(time):
    'To avoid you input wrong Minute, so CHEQUE is made to check inputting thing is right or not.'
    if time.isdigit() or time=='0000':
        return True

def password():
    'To avoid someone using this program and shutdown your PC, successfully'\
        +'So, we made a password to protect your PC.'
    for N in range(1,4):
        Password=getpass.getpass("Please input the password to start. ")
        if Password =='4444':
            return True
        else:
            print( "PASSWORD's WORNG!! ")
            if N ==2:
                print("You have ","a","chance to try it.")
            else:
                print("You have ",3-N,"chances to try it.")

if password() ==True:
    "In this block is actually doing Shutdown Computer,the detail is calling PC to Shutdown."
    while True:
        times=input("Please input minutes after that'll shutdown. ")
        if cheque(times) ==True:
            if times=='0000':
                os.system("shutdown -a")
                print("Auto shotdown was canceled successfuiily.")
                break
            
            else:
                times=str(int(times)*60)
                print(f"After {times} seconds,the computer will shutdown.")
                Jigaku=datetime.datetime.now()+datetime.timedelta(minutes=(float(times)/60))
                print(f"The sleep is going to be at {Jigaku}")   
                time.sleep(times)             
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                break
        else:
            print('Wrong,seconds must be a Positive Integer!.')
else:
    print("You try too many times.")

#'Press some key to Continue.'
os.system("pause")

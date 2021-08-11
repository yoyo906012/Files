#To randomly decide which store's food that I eat.
import table ,random,sys,os

table.firstimeresponse()
try:
    time=int(input("請輸入用餐時段"))

except Exception as err:
    print("輸入時段錯誤0~5")

if time == 1:
    print("結果是",table.morthing())
    print("Thanks for using!!")

elif time ==2:
    print("結果是",table.evening())
    print("Thanks for using!!")

elif time ==3:
    print("結果是",table.night())
    print("Thanks for using!!")

elif time ==4:
    print("結果是",table.dim())
    print("Thanks for using!!")

elif time ==5:
    print("結果是",table.drink())
    print("Thanks for using!!")

elif time ==0:
    print("結果是",table.beingornot())
    print("Thanks for using!!")

else:
    print("If you see the respone,that means the input value is error.")
    print("Input value has to between 0 and 5 ,integer.")
    print("Thanks for using!!")
    
table.shutdown()

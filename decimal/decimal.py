# -*- coding: UTF-8 -*-
import os,sys

def twos_comp(val):  #二補數計算機
	if -128<val<0:
		return format((256+val),"b") #計算負值的二補數
	elif 0<=val<128: 
		return '{:0=8d}'.format(int((format((val),"b"))))	#計算零跟正值的二補數	
	else:
		return "數值太大要在±127(含)間"  
N=0 #計數器初始值為零
while True:
	dec = (input("輸入整數數值："))
	try:
		if dec =='exit': #如果輸入exit直接先離開程式
			break
		dec=int(dec)    #宣告值為整數int
	except Exception as err: #如果輸入值不為整數則宣告異常
		print("輸入的內容是",dec,"不為exit或整數")
		continue  #回到迴圈一開始的地方
	print("十進位數為 ： ", dec)
	print("轉換為二進位為 : ", format(dec,"b"))
	print("轉換為二補數為 : ",  twos_comp(dec))
	print("轉換為八進位為 : ",   format(dec,"o"))
	print("轉換為十六進位為:", format(dec,"x"))
	print("=================================")
	N=N+1
print("總共計算出{}次".format(N)) #輸入exit後顯示計算次數
os.system('pause')               #輸入任何鍵以繼續
sys.exit()                       #輸入後來離開

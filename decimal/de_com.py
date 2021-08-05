# -*- coding: UTF-8 -*-
import os,sys

def twos_comp(val):  #二補數計算機
	if -128<val<0:
		return format((256+val),"b") #計算負值的二補數
	elif 0<=val<128: 
		return '{:0=8d}'.format(int(format((val),"b")))	#計算零跟正值的二補數	
	else:
		return "數值太大要在±127(含)間"

def shutdown():
    os.system('pause')               #輸入任何鍵以繼續
    sys.exit()                       #輸入後來離開
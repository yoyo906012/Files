# -*- coding: UTF-8 -*-
import os,sys

def time(value):
	'計算輸出要幾Bit的計算機'
	N=7 #初始值是8bit但第一個是判讀正負號的所以有效位只有七位故N=7
	while True: #當輸入數和被除數相除後的餘數一樣時
		if  abs(value)==abs(value)%(2**N) : #2**N代表多一bit會以2**N增加有效數字
			break #停下來
		N=N+1 #否則N+1繼續除 除到無法除為止
	return N #回傳N值

def twos_comp(val):  #二補數計算機
	if val<0:        #計算負值的二補數
		answer =format((2**(time(val-2))+val),"b") 
		#觀察發現負數的數字和該bit位下最大的數字相減的數字,再去做二進位轉換會剛好為該負數的二補數!
		#減二的原因是下一行的1我們想要挑出來所以8bit的東西變成5bit的輸出
		return '1-'+answer.zfill(time(val))
		#回傳負數固定開頭1- 跟後方上式計算出來的值
	elif val==0:     #計算等於零的二補數
		return("0-0000000")
		#18是複製18個空白以美化版面
	
	elif val>0:     #計算正值的二補數
			return '0-'+(format((val),"b").zfill(time(val)))
		#正值就直接取二補數但要看幾位一樣正值前方固定為0所以....
	
	else: #例外處理,但基本上不會走入此區!
		return "If you see the response that means ERROR!."
		  
def shutdown():
    os.system('pause')               #輸入任何鍵以繼續
    sys.exit()                       #輸入後,來離開
#二補數計算也讓我花了許久時間思考!
# Carmen Alamerl

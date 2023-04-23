# -*- coding: utf-8 -*-
from ftplib import FTP  # 加载ftp模块
from ftplib import error_perm  # 加载ftp模块
from os import listdir
from os.path import isfile, isdir, join
import os
import datetime

#======================================================================================#
#功能選單可控參數在這裡 其餘皆不要做更動為優
#mode=0找相同資料、mode=1找不同資料 mode=3找尋副檔名
mode=0
source=0
#副檔名(大寫全名配小寫全名)
textname=['.jpg',".JPG",'.png',".PNG"]
#source來源source=0本機A+本機B、source=1本機A+FTP-B.

#1:Yes、0:No
#是否輸出匡列的檔案
output=1
#是否將檔名輸出成list.txt
mktxt=1
#0:複寫 1續寫
para_mode=1
#是否先將文件清空 1:是 0:否,注意要和para_mode一起改
cls=0
#是否將匡列檔案做刪除
delete=0

#Pathway
#PART_A 
mypath_A = str('D:\Helmhotz\Maytze\\')  # 本機A
#PART_B
# E:\sd\gg上野B 
mypath_1 = ('E:\sony xpera ii\MOV\\')  # ,"")

# FTP
host=("192.168.124.252") #FTP遠端路徑
user='android' #使用者
passwd='android'#密碼
port=2221 #連接阜
showis=0 #是否先列出內容0否 1是
pwd = ('/DCIM/100ANDRO//')  # 欲前往的資料夾位置
#======================================================================================#

# 取得所有檔案與子目錄名稱
#A區
files = listdir(mypath_A)
file_name_A=[]
dir_name_A=[]

#B區

if source==0:
    mypath_B=mypath_1
elif source==1:
    mypath_B=host
else:
    print("Error: source needs 1 or 0.")

#======================================================================================#
#Add 艾德大臣

file_B = []
dir_B = []
same = []
notsame = []
many=[]

#======================================================================================#
#FTP 發展事務大臣
if source==1:
    #print(mypath_B)
    ftp = FTP()  # 初始化一个对象
    #ftp.set_debuglevel(2)  # 打开调试级别2，显示详细信息
    ftp.connect(host=mypath_B, port=port)  # 链接ftp server 和端口
    ftp.login(user=user, passwd=passwd)  # 登录用户名和密码
    #print(ftp.getwelcome)  # 打印欢迎信息
    if showis==1:
        ftp.retrlines('LIST')
    ftp.cwd(pwd)

    try:
        for i in ftp.nlst():
            if isdir(i):
                dir_B.append(i)  
            else:
                file_B.append(i)
            
    except error_perm as resp:
        if str(resp) == "550 No files found":
            print("No files in this directory")
        else:
            raise

    ftp.quit()
#======================================================================
elif source==0: 
    #path_B = listdir(mypath_B)
    #迴圈執行
    for f in listdir(mypath_B):
        #print(f)
        fullpath = join(mypath_B, f)
            # 判斷 fullpath 是檔案還是目錄
        if isfile(fullpath):
            #print("檔案：", f)
            file_B.append(f)
        elif isdir(fullpath):
            #print("目錄：", f)
            dir_B.append(f)

        #print(file_name_B)
        #print(dir_name_B)
else:
   print('Error:source key needs 0 or 1.')

#======================================================================================#
# 以迴圈處理
for f in files:
  fullpath = join(mypath_A, f)
  # 判斷 fullpath 是檔案還是目錄

  if isfile(fullpath):
    #print("檔案：", f)
    file_name_A.append(f)

  elif isdir(fullpath):
    #print("目錄：", f)
    dir_name_A.append(f)

print("===========================================================")
print(f"A路徑檔案共{len(file_name_A)}個,目錄共{len(dir_name_A)}個")
if source==0:
    print(f"B路徑檔案共{len(file_B)}個,目錄共{len(dir_B)}個")
else:
    print(f"B路徑(FTP遠端)內共{len(file_B)}個項目")
#print(file_name_A)
#print(dir_name_A)

#======================================================================================#

if (len(file_name_A)+len(dir_name_A)) >= (len(file_B)+len(dir_B)):
    main = file_name_A
    seco = file_B
else:
    main = file_B
    seco = file_name_A

print("===========================================================")
#重複檔案開找

if mode==0:
    n= 0
    for i in main:
        for j in seco:
            if mode == 0:
                if i == j:
                    if output == 1:
                        print(f"第{n+1}組,{i}")
                    same.append(str(i))
                    #seco=seco.remove(j)
                    n = n+1
    if mktxt==1:
        if para_mode==0:
            mode='r+'
        else:
            mode='a+'

        fd=open('same_name_list.txt',mode=mode)
        if cls == 1:
            fd.truncate(0)
        print("\n",file=fd)#換行用
        print(datetime.datetime.today(),file=fd)
        print(file=fd)
        print(same, file=fd)
        fd.writelines(f"\n有{n}個檔案重複名稱")
        fd.writelines("\n")
        fd.close()
    print(f"\n有{n}個檔案重複名稱")
    

elif mode==1:
    print("A資料夾不重複的部分")
    n = 0
    for i in main:
        m = 0
        for j in seco:
            if i != j:
                m = m+1
        if m == len(seco):
            print(f"第{n+1}組,{i}")
            n = n+1
    print(f"\nA共有{n}筆資料")

    print("===========================================================\n")

    print("B資料夾不重複的部分")
    n = 0
    for i in seco:
        m = 0
        for j in main:
            if i != j:
                m = m+1
        if m == len(main):
            print(f"第{n+1}組,{i}")
            n = n+1
    print(f"\nB共有{n}筆資料")

elif mode==3:
    for k in textname:
        l = 0
        print(f"\n搜尋副檔名為{k}之檔案")
        for f in file_name_A:
            if k in f:
                l = l+1
                print(f"第{l}個為{f}")#, f"其為{k}")  
        dir_name_A.append(f)
        many.append(l)
    
    print()#空一行用
    for k in range(len(textname)):
        print(f"有{many[k]}相同筆資料副檔名符合搜尋條件{textname[k]}")
    print(f"合計{sum(many)}個",f"且有{len(file_name_A)-sum(many)}個檔案不為要素")
    
    print(f"\nA路徑檔案共{len(file_name_A)}個,目錄共{len(dir_name_A)}個")
    print(f"有{l}相同筆資料副檔名符合搜尋條件")
    
else:
    print("Error:Mode key needs 0 or 1.")

#Delete files
if delete==1:#delete==0不刪除
    print(same)
    n=0
    where=input("要刪除哪個位置的A:輸入a,B:輸入b")
    if where=='a':
        do=os.remove()
    elif where=='b':
        do=ftp.delete()
    else:
        print("Error: To save your files we do not delete any files.")
    for k in same:
      do(k)
      n=n+1
    print(f"{n}次刪除")
    print("Finished")
input("按回車(ENTER)以繼續")#Finally exit key.

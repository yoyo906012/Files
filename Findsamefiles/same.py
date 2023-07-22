# -*- coding: utf-8 -*-
from os.path import join, isfile, isdir
from ftplib import FTP  # 加载ftp模块
from ftplib import error_perm  # 加载ftp模块
from os import listdir
from os.path import isfile, isdir, join
import os
import datetime
import re

#======================================================================================#
#功能選單可控參數在這裡 其餘皆不要做更動為優

#mode=0找相同資料、mode=1找不同資料 mode=3找尋副檔名
mode=0

#source來源source=0本機A+本機B、source=1本機A+FTP-B.
source=1

#副檔名(大寫全名配小寫全名)
textname=['.jpg',".JPG",'.png',".PNG"]


#是否輸出匡列的檔案1:Yes、0:No
output=1

#是否將檔名輸出成list.txt
mktxt=0

#0:複寫 1續寫
para_mode=1

#是否先將文件清空 1:是 0:否,注意要和para_mode一起改
cls=0

#是否將匡列檔案做刪除
delete=0

#Pathway
#PART_A 
path_A = r'E:\sony xpera ii\MOV\20230705'  # 本機A'E:\sd\PHO\\'D:\\

#PART_B
path_B = r'C:\\'  # E:\sd\gg上野B 

# FTP
host=("192.168.137.126") #FTP遠端路徑
user='android' #使用者
passwd='android'#密碼
port=2221 #連接阜
showis=0 #是否先列出內容0否 1是
pwd = ('/')  # 欲前往的資料夾位置100ANDRO/

type_filer =False# ['.jpg', ".JPG", '.png', ".PNG"] # or True #True is all file type #實現附檔名過濾器

#Remove items
delet=0
where='FTP' #path_A path_B FTP 三種
spec = 'all'#[x for x in range(0,10)]#'all'
#======================================================================================#
#演算法

def ftp(host,user,passwd,port,showis,pwd):
    '''FTP站台連線並且找出項目'''
    dir_B=[]
    file_B=[]
    ftp = FTP()  # 初始化一个对象
    #ftp.set_debuglevel(2)  # 打开调试级别2，显示详细信息
    ftp.connect(host, port)  # 链接ftp server 和端口
    ftp.login(user, passwd)  # 登录用户名和密码
    #print(ftp.getwelcome)  # 打印欢迎信息
    if showis == 1:
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
    return file_B,dir_B

def get_files_and_dirs(mypath):
    '''路徑分類器分成資料夾與檔案'''
    files = []
    dirs = []
    for f in listdir(mypath):
        fullpath = join(mypath, f)
        if isfile(fullpath):
            files.append(f)
        elif isdir(fullpath):
            dirs.append(f)
    return files, dirs

def findsame(fileA,fileB,dirA,dirB):
    '''相同名稱的資料夾與檔案查找並蒐集成陣列表'''
    same_file_name=[]
    same_dir_name=[]
    for i in fileA:
        for j in fileB:
            if i==j:
                same_file_name.append(i)
    for i in dirA:
        for j in dirB:
            if i == j:
                same_dir_name.append(i)
    return same_file_name,same_dir_name

def items():
    '''顯示個數'''
    print(f"\n路徑A有{len(dir_name_A)}個資料夾 及{len(file_name_A)}個檔案")
    print(f"路徑B(or FTP)有{len(dir_name_B)}個資料夾及{len(file_name_B)}個檔案")
    print(f"兩者間有{len(same_dir)}個相同資料夾及{len(same_file)}個檔案")
    print(f"\n========================以下顯示項目========================")
    print(f"\n以下為資料夾")
    
    n=1
    for i in (same_dir):
        print(f"第{n}組為,{i}")
        n=n+1

    print(f"\n以下為檔案")

    n=1   
    for i in (same_file):
        print(f"第{n}組為,{i}")
        n=n+1
    print(f"\n")

def export_text():
    '''匯出成txt檔'''
    if para_mode == 0:
        mode = 'r+'
    else:
        mode = 'a+'

    fd = open('same_name_list.txt', mode=mode)
    if cls == 1:
        fd.truncate(0)
    print("\n", file=fd)  # 換行用
    print(datetime.datetime.today(), file=fd)
    print(file=fd)
    print(same_file, file=fd)
    fd.writelines(f"\n有{len(same_file)}個檔案重複名稱")
    fd.writelines("\n")
    fd.close()

def dele(item,where):
    '''刪除函式'''
    '''list:檔案項目,where:判別source'''
    if source ==1:
        pass
    
    def delete_file_from_ftp(host, user, passwd, port, file_path):
        '''刪除FTP上的項目'''
        try:
            ftp = FTP()
            ftp.connect(host=host, port=port)
            ftp.login(user=user, passwd=passwd)

            # Change to the directory containing the file
            directory = file_path.rpartition('/')[0]
            ftp.cwd(directory)

            # Get the file name from the file path
            file_name = file_path.rpartition('/')[-1]
            print(file_name)
            # Delete the file from the FTP server
            ftp.delete(file_name)

            #print(
            #    f"File '{file_name}' has been successfully deleted from the FTP server.")
        except Exception as e:
            print(f"Error {str(e)} can't delete.")

        finally:
            ftp.quit()

    def delete_PC(list):
        '''刪除本地的檔案'''
        os.remove(where+item)
        return f"Done! Removing{len(list)+1} items." 

    if where =='path_A':
        delete_PC(item,path_A)
    elif where =='path_B':
        delete_PC(item,path_B)
    elif where =='FTP' or where =='ftp':
        file_path=pwd+same_file[i]
        delete_file_from_ftp(host,user,passwd,port,file_path=file_path)
    else:
        return f"Error where must be path_A ,path_B, or FTP(ftp)."
# Example usage

#======================================================================================#

if mode==0:
    file_name_A, dir_name_A = get_files_and_dirs(path_A)
    
    if source==0:
        file_name_B, dir_name_B = get_files_and_dirs(path_B)
        same_file, same_dir = findsame(
            file_name_A, file_name_B, dir_name_A, dir_name_B)
    
    elif source==1:
        file_name_B, dir_name_B = (ftp(host,user,passwd,port,showis,pwd))
        same_file, same_dir = findsame(
            file_name_A, file_name_B, dir_name_A, dir_name_B)
    
    else:
        print("Error the source word must be 1 or 0.")
    
    items()
elif mode==1:
    file_name_A, dir_name_A = get_files_and_dirs(path_A)
    file_ftp_B,dir_ftp_B = ftp(host,user,passwd,port,showis)
    same_file, same_dir = findsame(
        file_name_A, file_ftp_B, dir_name_A, dir_ftp_B)
else:
    print("Error the mode is wrong!.")
#======================================================================================#

print("============================================================")

#======================================================================================#
if delet==1 and spec=='all':
    cheque=input(f"確認刪除路徑為,{where}? (y/n)")
    if cheque =='y'or cheque=='Y':
        idx=input(f"確認刪除所有共通檔案於{where}? (y/n)")
        if idx in['y','Y']:
            for i in range(0,len(same_file)):
                dele(same_file[i],where)
                print(f'成功刪除{same_file[i]}')

elif isinstance(spec,list)==True and delet==1:
        cheque =input(f"確認刪除路徑為{where},? (y/n) ")
        if cheque in ['Y','y']:
            index  =print("確認刪除檔名為以下")
            for i in spec:
                print(same_file[i])
            idx=input(f"{len(spec)}個項目 y/n ")
            if idx in['Y','y']:
                for i in spec:
                    dele(same_file[i],where)
                print(f"Successfully delete {len(spec)}files")
else:
    if delet!=0:
        print(f"Error dele must be 0 or 1 and spec must be all or type->[...]\n")

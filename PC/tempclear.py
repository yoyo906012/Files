
import os 
import shutil
import time

#=================================================#

path=('C:/Users/fossine/AppData/Local/Temp/')

#=================================================#

position=os.chdir(path)
#print(os.listdir(path))
all_info=os.listdir(position)
before=len(all_info)
print(f"共{len(os.listdir(position))}個檔案")
if input('確定要刪除嗎?要的話輸入1_: ')=='1':
    start = time.time()
    for i in all_info:
        try:
            if os.path.isdir(i)==True:
                shutil.rmtree(i,ignore_errors=True)
            else:
                os.remove(i)
        except PermissionError as e:
            continue
    end = time.time()
    after = len(os.listdir(position))
    print(f'成功刪除{before-after}個檔案')
else:
    print("不刪除")
print(f"目前尚有{after}個項目")
print(f"執行耗時{round(end - start,4)}時間秒")
input("以上按Enter以跳出、以上")

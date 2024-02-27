import os
import time
dir_path = r"E:\next-blog\10-21-blog1\public\photos" + "\\"

# 获取当前目录下的文件
entries = os.listdir(dir_path)
# entries = set(entries)
num = 1
dir_size = len(entries)
# print(entries)
# print(dir_size)

# for i in entries:
#     num = i.split(".")[0]
#     print(num)
#     os.rename(dir_path+i,dir_path + num + r".png")
print(dir_path+entries[0])
print(dir_path+ str(num) + ".png")
for picName in entries:

    try:
        os.rename(dir_path+picName,dir_path + str(num) + r".png")
        num +=1
        time.sleep(0.3)
        print(f'{picName} 成功改名!')
    except:
        print("重命名失败")



import os

dirname = "文章封面"
dir_path = r"C:\Users\xuhaizhao\Pictures"+"\\"+ dirname + "\\"

# 获取当前目录下的文件
entries = os.listdir(dir_path)
# entries = set(entries)
num = 1
dir_size = len(entries)
print(entries)
# print(dir_size)

for i in entries:
    num = i.split(".")[0]
    print(num)
    os.rename(dir_path+i,dir_path + num + r".png")
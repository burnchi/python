import os

dirname = "文章封面"
dir_path = r"C:\Users\xuhaizhao\Pictures"+"\\"+ dirname + "\\"

# 获取当前目录下的文件
entries = os.listdir(dir_path)
# entries = set(entries)
num = 1
dir_size = len(entries)
# print(entries)
# print(dir_size)
suitable_pic = []

# 筛选目录下的图片
for file in entries:
    if file.endswith(('.jpg','.png')):
        suitable_pic.append(file)

# print(suitable_pic)

for file in suitable_pic:

    # 判断该名字没有被取
    if dirname + str(num)+".jpg" or dirname + str(num)+".png" not in suitable_pic: 
        # 重命名文件 
        os.rename(dir_path+file,dir_path + dirname + str(num)+".png")
        print("[+]"+file+"-->"+str(num)+".png")
        # 刷新一下目录列表
        suitable_pic = os.listdir(dir_path)
        
    # 名字被取了
    else:
        # 找一下有哪个名字没被取
        for n in range(1,dir_size+1):
            # 这个数字没被取
            if dirname + str(n) +".jpg" or dirname + str(n) +".png" not in suitable_pic:
                os.rename(dir_path+file,dir_path + dirname +str(n)+".png")
                print("[+]"+file+"-->"+str(n)+".png")
                suitable_pic = os.listdir(dir_path)
                # print(str(n)+".jpg"+"没有被使用")
                break

    num += 1




import os
import re
import time

# 替换成你的根文件夹路径
root_folder =  r"E:\Nextjs\test\posts" + '\\'  
file_list = []

# 收集根目录下的所有文件路径
for root, dirs, files in os.walk(root_folder):
    for file in files:
        file_path = os.path.join(root, file)
        file_list.append(file_path)
# 遍历所有文件的路径
for file_path in file_list:
    # print(file_path)
    try:
        # 逐个打开并读取内容
        with open(file_path, "r",encoding="utf-8") as file:
            file_content = file.read()
        
        result_string = re.sub(r'(!\[.*?\]\()(E:\\mdpic\\)(.*?)(\))', r'\1/mdpic/\3\4', file_content)
        result_string1 = re.sub(r'(<img src=")(E:\\mdpic\\)(.*?")(.*?/>)', r'\1/mdpic/\3\4',result_string)
        # 写入文件
        with open(file_path, "w",encoding="utf-8") as file:
            file.write(result_string1)
            print(f"{file_path} 写入成功")

        time.sleep(0.5)
    except Exception as e:
        print("发生了异常:", e)

import os
import re
import time
import shutil

# 替换成项目文章路径
root_folder =  r"/home/burnchi/md笔记" + '/'  

file_list = []

# 匹配md中的图片
picpattern = r"!\\\[.*?]\\\(/home/burnchi/mdpic/(.*?)\\\)"
picpattern1 = r"""<img src="e:/mdpic/(.*?)".*?style="(.*?)" />"""

#修改md样式为Next组件
def replacement_function(match):
    image_name = match.group(1)
    return f"""
![{image_name}](/home/burnchi/mdpic/{image_name})
"""

def replacement_function1(match):
    image_name = match.group(1)
    style = match.group(2)
    return f"""
<img src="/home/burnchi/mdpic/{image_name}" alt="{image_name}" style="{style}" />
"""

# 收集文章路径下的所有文件路径
for root, dirs, files in os.walk(root_folder):
    for file in files:
        file_path = os.path.join(root, file)
        file_list.append(file_path)
# print(file_list)


# 遍历所有文件的路径更改样式
for file_path in file_list:
    try:
        # 逐个打开并读取内容
        with open(file_path, "r",encoding="utf-8") as file:
            file_content = file.read()
        
        str = re.findall(picpattern,file_content)
        str1 = re.findall(picpattern1,file_content)
        if  str or str1:
            # 找到md中图片样式后替换成Next组件
            modified_text1 = re.sub(picpattern, replacement_function, file_content)
            modified_text2 = re.sub(picpattern1, replacement_function1, modified_text1)

            # 写入文件
            with open(file_path, "w",encoding="utf-8") as file:
                file.write(modified_text2)
                print(f"{file_path} 改写组件成功")

            time.sleep(0.2)

    except Exception as e:
        print("发生了异常:", e)


